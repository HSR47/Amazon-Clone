from secrets import token_urlsafe
from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Body, Request , status , HTTPException , Depends
from datetime import datetime , timedelta

from fastapi.responses import JSONResponse
from pydantic import EmailStr

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.config import settings
import app.user.models as userModel
import app.user.crud as userCrud
import app.auth.dependencies as authDep
from app.utils.email import sendMail
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.passlib import hashPassword, verifyPassword


authRouter = APIRouter(tags=["Authentication"])


# ----------------------------LOG IN-------------------------
@authRouter.post("/login")
def login(
    *,
    email:Annotated[EmailStr , Body()],
    password:Annotated[str , Body()],
    db:Annotated[Session , Depends(getDb)]
):
    user:userModel.User = userCrud.get_user_by_email(db , email)

    if (user==None)  or  (not verifyPassword(password , user.hashed_password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")

    accessToken = create_access_token({"user_id" : user.id})
    refreshToken = create_refresh_token({"user_id" : user.id})

    user.refresh_token = refreshToken
    db.commit()

    response = JSONResponse(content={
        "token" : accessToken,
        "token_type" : "bearer"
    })

    response.set_cookie(key="refreshToken" , value=refreshToken)
    
    return response
# ------------------------------------------------------------------


# ----------------------------REFRESH ACCESS TOKEN-------------------------
@authRouter.post("/token/refresh")
def refresh_access_token(
    *,
    req:Request,
    db:Session = Depends(getDb)
):
    refreshToken = req.cookies.get("refreshToken" , None)
    if refreshToken == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
        
    payload = verify_token(refreshToken)
    userId = payload["user_id"]

    user:userModel.User = userCrud.get_user_by_id(db , userId)
    if user==None or user.refresh_token!=refreshToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
    
    accessToken = create_access_token({"user_id" : user.id})

    return {
        "token" : accessToken,
        "token_type" : "bearer"
    }
# ------------------------------------------------------------------


# ----------------------------LOG OUT-------------------------
@authRouter.get("/logout")
def logout_User(
    *,
    curUser:Annotated[userModel.User , Depends(authDep.get_current_user)],
    db:Annotated[Session , Depends(getDb)]
):
    curUser.refresh_token = None
    db.commit()

    res = JSONResponse(content={
        "message" : "logged out"
    })
    res.delete_cookie("refreshToken")

    return res
# ------------------------------------------------------------------


# ----------------------------GENERATE PASSWORD RESET TOKEN-------------------------
@authRouter.post("/password/forgot")
def generate_Pass_Reset_Token(
    *,
    bgtask:BackgroundTasks,
    email:Annotated[EmailStr , Body(embed=True)],
    db:Annotated[Session , Depends(getDb)]
):
    user:userModel.User = userCrud.get_user_by_email(db , email)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    passResetToken = token_urlsafe(32)
    passResetTokenExp = datetime.utcnow() + timedelta(minutes=settings.PASS_RESET_TOKEN_EXP_MINUTES)

    user.pass_reset_token = passResetToken
    user.pass_reset_token_exp = passResetTokenExp
    db.commit()

    bgtask.add_task(sendPassResetToken , email , passResetToken)

    return {"message" : "mail sent"}

async def sendPassResetToken(email , passResetToken):
    subject = "Reset Password"
    recipients = [email]
    html = f"""Your secret code is {passResetToken}"""

    await sendMail(recipients=recipients , subject=subject , html=html)
# ------------------------------------------------------------------


# ----------------------------RESET PASSWORD-------------------------
@authRouter.post("/password/reset/{secret}")
def reset_Password(
    *,
    secret:str,
    email:Annotated[EmailStr , Body()],
    newPassword:Annotated[str , Body(pattern=r"^.{6,20}$")],
    db:Session = Depends(getDb)
):

    user:userModel.User = userCrud.get_user_by_email(db , email)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")

    if user.pass_reset_token != secret:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="invalid password reset token")
    
    if datetime.utcnow() > user.pass_reset_token_exp:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="password reset token expired")
    
    user.hashed_password = hashPassword(newPassword)
    user.pass_reset_token = None
    user.pass_reset_token_exp = None
    user.refresh_token = None
    db.commit()

    return {"message" : "password reset"}
# ------------------------------------------------------------------