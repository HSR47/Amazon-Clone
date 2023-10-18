
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session

import app.user.crud as userCrud
import app.user.models as userModel
import app.user.schemas as userSchema
import app.user.dependencies as userDep
import app.auth.dependencies as authDep


userRouter = APIRouter(tags=["User"])


# ----------------------------CREATE USER (ANY)-------------------------
@userRouter.post("/user" , response_model=userSchema.UserOut)
def register_user(
    *,
    data:userSchema.UserIn,
    db:Annotated[Session , Depends(getDb)]
):
    checkEmail = userCrud.get_user_by_email(db , data.email)
    if checkEmail != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="user with this email already exists")
    
    checkMobile = userCrud.get_user_by_mobile(db , data.mobile)
    if checkMobile != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="user with this mobile already exists")
    
    newUser:userModel.User = userCrud.create_user(db , data=data)
    return newUser
# ------------------------------------------------------------------


# ----------------------------GET ALL USERS (ADMIN)-------------------------
@userRouter.get("/user" , response_model=list[userSchema.UserOut])
def get_all_users(
    *,
    offset:int=0,
    limit:int=100,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    allUsers:list[userModel.User] = userCrud.get_all_users(db=db, offset=offset, limit=limit)
    return allUsers
# ------------------------------------------------------------------


# ----------------------------GET MY DETAILS (BOTH)-------------------------
@userRouter.get("/user/me", response_model=userSchema.UserOut)
def get_my_details(
    *,
    curUser:Annotated[userModel.User , Depends(authDep.get_current_user)]
):
    return curUser
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC USER (ADMIN)-------------------------
@userRouter.get("/user/{id}" , response_model=userSchema.UserOut)
def get_specific_user(
    *,
    user:Annotated[userModel.User , Depends(userDep.valid_user_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)]
):  
    return user
# ------------------------------------------------------------------


# ----------------------------DELETE USER (ADMIN)-------------------------
@userRouter.delete("/user/{id}")
def delete_specific_user(
    *,
    user:Annotated[userModel.User , Depends(userDep.valid_user_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    userCrud.delete_user(db , user)

    return {"message" : "deleted"}
# ------------------------------------------------------------------


# ----------------------------UPDATE MY DETAILS (BOTH)-------------------------
@userRouter.patch("/user/me" , response_model=userSchema.UserOut)
def update_my_details(
    *,
    data:userSchema.UserPatch,
    curUser:Annotated[userModel.User , Depends(authDep.get_current_user)],
    db:Annotated[Session , Depends(getDb)]
):
    if data.mobile != None and data.mobile != curUser.mobile:
        checkMobile = userCrud.get_user_by_mobile(db , data.mobile)
        if checkMobile != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="mobile already exists")
    
    if data.email != None and data.email != curUser.email:
        checkEmail = userCrud.get_user_by_email(db , data.email)
        if checkEmail != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="email already exists")
    
    updatedUser = userCrud.update_user(db , curUser , data)
    return updatedUser
# ------------------------------------------------------------------


# ----------------------------UPDATE SPECIFIC USER (ADMIN)-------------------------
@userRouter.patch("/user/{id}" , response_model=userSchema.UserOut)
def update_specific_user(
    *,
    user:Annotated[userModel.User , Depends(userDep.valid_user_id)],
    data:userSchema.UserPatch,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):  
    if data.mobile != None and data.mobile != user.mobile:
        checkMobile = userCrud.get_user_by_mobile(db , data.mobile)
        if checkMobile != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="mobile already exists")
    
    if data.email != None and data.email != user.email:
        checkEmail = userCrud.get_user_by_email(db , data.email)
        if checkEmail != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="email already exists")
    
    updatedUser = userCrud.update_user(db , user , data)
    return updatedUser
# ------------------------------------------------------------------





