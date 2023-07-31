
from typing import Optional
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
    wishlistProducts : list[int]

    class Config:
        from_attributes = True



class updateUser(BaseModel):
    fname : Optional[str] = Field(default=None)
    lname : Optional[str] = Field(default=None)
    mobile : Optional[str] = Field(default=None , pattern=r"^[0-9]{10}$")

    @validator("fname" , "lname" , "mobile")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("fname" , "lname")
    def validateOneWord(cls , value:str):
        if value == None:
            return value
        if " " in value:
            raise ValueError("fname and lname must contain only one word")
        
        return value

    @validator("fname" , "lname")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()
