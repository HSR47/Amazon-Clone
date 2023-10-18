
from typing import Optional
from pydantic import BaseModel , EmailStr , constr
from datetime import datetime


class UserBase(BaseModel):
    fname : constr(pattern=r"^[A-Za-z]+$" , to_lower=True)
    lname : constr(pattern=r"^[A-Za-z]+$" , to_lower=True)
    mobile : constr(pattern=r"^[0-9]{10}$")
    email : EmailStr
    isAdmin : bool


class UserIn(UserBase):
    password : constr(pattern=r"^.{6,20}$")


class UserOut(UserBase):
    id : int
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True


class UserPatch(UserBase):
    fname : Optional[constr(pattern=r"^[A-Za-z]+$" , to_lower=True)] = None
    lname : Optional[constr(pattern=r"^[A-Za-z]+$" , to_lower=True)] = None
    mobile : Optional[constr(pattern=r"^[0-9]{10}$")] = None
    email : Optional[EmailStr] = None
    isAdmin : Optional[bool] = None
    password : Optional[constr(pattern=r"^.{6,20}$")] = None

