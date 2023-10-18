
from sqlalchemy.orm import Session
from . import models , schemas
from app.utils import passlib

# ----------------------------RETRIEVE-------------------------
def get_user_by_id(db:Session , id:int):
    user:models.User = db.query(models.User).filter(models.User.id == id).first()
    return user

def get_user_by_email(db:Session , email:str):
    user:models.User = db.query(models.User).filter(models.User.email == email).first()
    return user

def get_user_by_mobile(db:Session , mobile:str):
    user:models.User = db.query(models.User).filter(models.User.mobile == mobile).first()
    return user

def get_all_users(db:Session , offset:int = 0 , limit:int = 100):
    users:list[models.User] = db.query(models.User).offset(offset).limit(limit).all()
    return users
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_user(db:Session , data:schemas.UserIn):
    newUser = models.User(
        email = data.email,
        password = passlib.hashPassword(data.password),
        fname = data.fname,
        lname = data.lname,
        mobile = data.mobile,
        isAdmin = data.isAdmin
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_user(db:Session , user:models.User , data:schemas.UserPatch):
    if data.fname != None:
        user.fname = data.fname
    
    if data.lname != None:
        user.lname = data.lname
    
    if data.mobile != None:
        user.mobile = data.mobile
    
    if data.email != None:
        user.email = data.email
    
    if data.isAdmin != None:
        user.isAdmin = data.isAdmin
    
    if data.password != None:
        user.password = passlib.hashPassword(data.password)

    db.commit()
    db.refresh(user)

    return user
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_user(db:Session , user:models.User):
    db.delete(user)
    db.commit()
# ------------------------------------------------------------------