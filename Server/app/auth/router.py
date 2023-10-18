from secrets import token_urlsafe
from fastapi import APIRouter, BackgroundTasks, Request , status , HTTPException , Depends
from datetime import datetime , timedelta

from fastapi.responses import JSONResponse

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.config import settings
from app.user.models import User
from app.utils.email import sendMail
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.passlib import hashPassword, verifyPassword
import app.auth.schemas as authSchema
from app.auth.dependencies import get_current_user


authRouter = APIRouter(tags=["Authentication"])


# ----------------------------LOG IN-------------------------
@authRouter.post("/login")
def login(data:authSchema.loginUser , db:Session = Depends(getDb)):
    
    user:User = db.query(User).filter(User.email == data.email).first()

    if (user==None)  or  (not verifyPassword(data.password , user.hashed_password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")

    accessToken = create_access_token({"id" : user.id})
    refreshToken = create_refresh_token({"id" : user.id})

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
def refresh_access_token(req:Request , db:Session = Depends(getDb)):
    refreshToken = req.cookies.get("refreshToken" , None)
    if refreshToken == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
        
    payload = verify_token(refreshToken)
    userId = payload["id"]

    user:User = db.query(User).filter(User.id == userId).first()
    if user==None or user.refresh_token!=refreshToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
    
    accessToken = create_access_token({"id" : user.id})

    return {
        "token" : accessToken,
        "token_type" : "bearer"
    }
# ------------------------------------------------------------------


# ----------------------------LOG OUT-------------------------
@authRouter.get("/logout")
def logout_User(curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    curUser.refresh_token = None
    db.commit()

    res = JSONResponse(content={
        "message" : "logged out"
    })
    res.delete_cookie("refreshToken")

    return res
# ------------------------------------------------------------------


# ----------------------------CHANGE PASSWORD-------------------------
@authRouter.put("/password")
def change_Password(data:authSchema.changePassword , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):
    curUser.hashed_password = hashPassword(data.password)
    db.commit()
    db.refresh(curUser)

    return {"message" : "password changed"}
# ------------------------------------------------------------------


# ----------------------------GENERATE PASSWORD RESET TOKEN-------------------------
@authRouter.post("/forgot-password")
def generate_Pass_Reset_Token(bgtask:BackgroundTasks , data:authSchema.forgotPassRequest , db:Session = Depends(getDb)):
    user:User = db.query(User).filter(User.email == data.email).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    passResetToken = token_urlsafe(32)
    passResetTokenExp = datetime.utcnow() + timedelta(minutes=settings.PASS_RESET_TOKEN_EXP_MINUTES)

    user.pass_reset_token = passResetToken
    user.pass_reset_token_exp = passResetTokenExp
    db.commit()

    bgtask.add_task(sendPassResetToken , data.email , passResetToken)

    return {"message" : "mail sent"}

async def sendPassResetToken(email , passResetToken):
    subject = "Reset Password"
    recipients = [email]
    html = f"""Your secret code is {passResetToken}"""

    await sendMail(recipients=recipients , subject=subject , html=html)
# ------------------------------------------------------------------


# ----------------------------RESET PASSWORD-------------------------
@authRouter.post("/reset-password/{secret}")
def reset_Password(secret:str , data:authSchema.resetPassRequest , db:Session = Depends(getDb)):

    user:User = db.query(User).filter(User.email == data.email).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")

    if user.pass_reset_token != secret:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="invalid password reset token")
    
    if datetime.utcnow() > user.pass_reset_token_exp:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="password reset token expired")
    
    user.hashed_password = hashPassword(data.password)
    user.pass_reset_token = None
    user.pass_reset_token_exp = None
    user.refresh_token = None
    db.commit()

    return {"message" : "password reset"}
# ------------------------------------------------------------------