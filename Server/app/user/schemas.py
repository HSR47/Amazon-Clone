
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class UserBase(BaseModel):
    email : EmailStr
    fname : str
    lname : str
    isAdmin : bool
    mobile : str = Field(pattern=r"^[0-9]{10}$")

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


class UserIn(UserBase):
    password : str = Field(pattern=r"^.{6,20}$")


class UserOut(UserBase):
    id : int
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True



class UserPatch(BaseModel):
    pass


class updateUser(BaseModel):
    fname : str
    lname : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")

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


class registerUser(BaseModel):
    email : EmailStr
    password : str = Field(pattern=r"^.{6,20}$")
    fname : str
    lname : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")
    isAdmin : bool

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
    isAdmin : bool
    email : EmailStr
    mobile : str
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True



class updateUser(BaseModel):
    fname : str
    lname : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")

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
