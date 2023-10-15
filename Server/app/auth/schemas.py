
from pydantic import BaseModel , EmailStr, Field


class loginUser(BaseModel):
    email : EmailStr
    password : str
    

class changePassword(BaseModel):
    password : str = Field(pattern=r"^.{6,20}$")

class forgotPassRequest(BaseModel):
    email : EmailStr

class resetPassRequest(BaseModel):
    email : EmailStr
    password : str = Field(pattern=r"^.{6,20}$")