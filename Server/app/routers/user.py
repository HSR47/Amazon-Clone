
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user
import app.schemas.userSchema as userSchema
import app.utils.passlib as passlib

userRouter = APIRouter(tags=["User"])


# ----------------------------CREATE USER-------------------------
@userRouter.post("/user" , response_model=userSchema.returnUser)
def register_User(data:userSchema.registerUser , db:Session = Depends(getDb)):

    check = db.query(User).filter((User.email==data.email) | (User.mobile==data.mobile)).first()
    if check != None:
        if check.email == data.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="email already exists")
        elif check.mobile == data.mobile:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="mobile already exists")
    
    newUser = User(
        fname = data.fname,
        lname = data.lname,
        role = data.role,
        email = data.email,
        mobile = data.mobile,
        password = passlib.hashPassword(data.password)
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser
# ------------------------------------------------------------------



# ----------------------------GET ALL USERS-------------------------
@userRouter.get("/user" , response_model=list[userSchema.returnUser])
def get_All_Users(curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):
    allUsers = db.query(User).all()
    return allUsers
# ------------------------------------------------------------------



# ----------------------------GET SPECIFIC USER-------------------------
@userRouter.get("/user/{id}" , response_model=userSchema.returnUser)
def get_Specific_User(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    user:User = db.query(User).filter(User.id == id).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    return user
# ------------------------------------------------------------------



# ----------------------------DELETE USER-------------------------
@userRouter.delete("/user/{id}")
def delete_User(id:int , db:Session = Depends(getDb)):

    user = db.query(User).filter(User.id == id).first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    db.delete(user)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------



# ----------------------------UPDATE USER-------------------------
@userRouter.patch("/user" , response_model=userSchema.returnUser)
def update_User(data:userSchema.updateUser , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    user:User = curUser

    if data.fname != None:
        user.fname = data.fname
    if data.lname != None:
        user.lname = data.lname
    if data.mobile != None:
        check = db.query(User).filter(User.mobile == data.mobile).first()
        if check != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="mobile already registered")
        user.mobile = data.mobile
    
    db.commit()
    db.refresh(user)

    return user
# ------------------------------------------------------------------



# ----------------------------BLOCK USER-------------------------
@userRouter.put("/user/block/{id}")
def block_User(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    
    userToBlock:User = db.query(User).filter(User.id == id).first()

    if userToBlock == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    if userToBlock.role == "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="admin cannot be blocked")
    
    if userToBlock.blocked == True:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="already blocked")
    
    userToBlock.blocked = True

    db.commit()
    
    return {"message" : "blocked"}
# ------------------------------------------------------------------



# ----------------------------UNBLOCK USER-------------------------
@userRouter.put("/user/unblock/{id}")
def unblock_User(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    
    userToBlock:User = db.query(User).filter(User.id == id).first()

    if userToBlock == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    if userToBlock.blocked == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="already unblocked")
    
    userToBlock.blocked = False

    db.commit()
    
    return {"message" : "unblocked"}
# ------------------------------------------------------------------