from secrets import token_urlsafe
from fastapi import APIRouter, BackgroundTasks, Request , status , HTTPException , Depends
from datetime import datetime , timedelta

from fastapi.responses import JSONResponse

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.config import settings
from app.models.userModel import User
from app.schemas.userSchema import returnUser
from app.utils.email import sendMail
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.passlib import hashPassword, verifyPassword
import app.schemas.authSchema as authSchema

from fastapi.security import OAuth2PasswordBearer


authRouter = APIRouter(tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# ----------------------------GET CURRENT USER-------------------------
def get_current_user(token:str = Depends(oauth2_scheme) , db:Session = Depends(getDb)):
    payload = verify_token(token)
    userId = payload["id"]

    user:User = db.query(User).filter(User.id == userId).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")

    return user
# ------------------------------------------------------------------


# ----------------------------GET CURRENT CUSTOMER-------------------------
def get_current_customer(user:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    if user.role != "customer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="not authorized")

    return user
# ------------------------------------------------------------------


# ----------------------------GET CURRENT ADMIN-------------------------
def get_current_admin(user:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="not authorized")

    return user
# ------------------------------------------------------------------


# ----------------------------LOG IN-------------------------
@authRouter.post("/login")
def login(data:authSchema.loginUser , db:Session = Depends(getDb)):
    
    user:User = db.query(User).filter(User.email == data.email).first()

    if (user==None)  or  (not verifyPassword(data.password , user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")

    accessToken = create_access_token({"id" : user.id})
    refreshToken = create_refresh_token({"id" : user.id})

    user.refreshToken = refreshToken
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
def refreshAccessToken(req:Request , db:Session = Depends(getDb)):
    refreshToken = req.cookies.get("refreshToken" , None)
    if refreshToken == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
        
    payload = verify_token(refreshToken)
    userId = payload["id"]

    user:User = db.query(User).filter(User.id == userId).first()
    if user==None or user.refreshToken!=refreshToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="invalid credentials")
    
    accessToken = create_access_token({"id" : user.id})

    return {
        "token" : accessToken,
        "token_type" : "bearer"
    }
# ------------------------------------------------------------------


# ----------------------------LOG OUT-------------------------
@authRouter.get("/logout")
def logoutUser(curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    curUser.refreshToken = None
    db.commit()

    res = JSONResponse(content={
        "message" : "logged out"
    })
    res.delete_cookie("refreshToken")

    return res
# ------------------------------------------------------------------


# ----------------------------CHANGE PASSWORD-------------------------
@authRouter.put("/password")
def changePassword(data:authSchema.changePassword , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):
    curUser.password = hashPassword(data.password)
    db.commit()
    db.refresh(curUser)

    return {"message" : "password changed"}
# ------------------------------------------------------------------


# ----------------------------GENERATE PASSWORD RESET TOKEN-------------------------
@authRouter.post("/forgot-password")
def generatePassResetToken(bgtask:BackgroundTasks , data:authSchema.forgotPassRequest , db:Session = Depends(getDb)):
    user:User = db.query(User).filter(User.email == data.email).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    passResetToken = token_urlsafe(32)
    passResetTokenExp = datetime.utcnow() + timedelta(minutes=settings.PASS_RESET_TOKEN_EXP_MINUTES)

    user.passResetToken = passResetToken
    user.passResetTokenExp = passResetTokenExp
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
def resetPassword(secret:str , data:authSchema.resetPassRequest , db:Session = Depends(getDb)):

    user:User = db.query(User).filter(User.email == data.email).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")

    if user.passResetToken != secret:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="invalid password reset token")
    
    if datetime.utcnow() > user.passResetTokenExp:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="password reset token expired")
    
    user.password = hashPassword(data.password)
    user.passResetToken = None
    user.passResetTokenExp = None
    user.refreshToken = None
    db.commit()

    return {"message" : "password reset"}
# ------------------------------------------------------------------