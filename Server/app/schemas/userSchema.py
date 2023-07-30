
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class registerUser(BaseModel):
    fname : str
    lname : str
    role : str = Field(pattern=r"^(customer|admin)$")
    email : EmailStr
    mobile : str = Field(pattern=r"^[0-9]{10}$")
    password : str = Field(pattern=r"^.{6,20}$")

    @validator("fname" , "lname" , "email" , "mobile")
    def validateStrip(cls , value:str):
        return value.strip()

    @validator("fname" , "lname")
    def validateOneWord(cls , value:str):
        if " " in value:
            raise ValueError("fname and lname must contain only one word")
        
        return value

    @validator("fname" , "lname" , "email")
    def validateLowerCase(cls , value:str):
        return value.lower()



class returnUser(BaseModel):
    id : int
    fname : str
    lname : str
    role : str
    email : EmailStr
    mobile : str
    blocked : bool
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True



class updateUser(BaseModel):
    fname : str | None
    lname : str | None
    mobile : str | None  = Field(pattern=r"^[0-9]{10}$")

    @validator("fname" , "lname" , "mobile")
    def validateStrip(cls , value:str):
        return value.strip()

    @validator("fname" , "lname")
    def validateOneWord(cls , value:str):
        if " " in value:
            raise ValueError("fname and lname must contain only one word")
        
        return value

    @validator("fname" , "lname")
    def validateLowerCase(cls , value:str):
        return value.lower()
