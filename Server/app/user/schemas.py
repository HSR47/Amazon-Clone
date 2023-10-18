
from typing import Optional
from pydantic import BaseModel , EmailStr, Field , constr
from datetime import datetime

class UserBase(BaseModel):
    fname : constr(pattern=r"^[A-Za-z]+$" , to_lower=True)
    lname : constr(pattern=r"^[A-Za-z]+$" , to_lower=True)
    mobile : constr(pattern=r"^[0-9]{10}$")
    email : EmailStr
    is_admin : bool



class UserCreate(UserBase):
    password : constr(pattern=r"^.{6,20}$")



class UserInDB(UserBase):
    id : int
    hashed_password : str
    created_at : datetime
    updated_at : datetime



class UserReturn(UserInDB):
    hashed_password:str = Field(exclude=True)

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    fname : Optional[constr(pattern=r"^[A-Za-z]+$" , to_lower=True)] = None
    lname : Optional[constr(pattern=r"^[A-Za-z]+$" , to_lower=True)] = None
    mobile : Optional[constr(pattern=r"^[0-9]{10}$")] = None
    email : Optional[EmailStr] = None
    is_admin : Optional[bool] = None
    password : Optional[constr(pattern=r"^.{6,20}$")] = None

