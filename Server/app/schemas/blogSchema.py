
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

from app.schemas.userSchema import returnUser


class createBlogRequest(BaseModel):
    title : str
    description : str
    categoryId : Optional[int] = Field(default=None)

    @validator("title" , "description")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()



class returnBlog(BaseModel):
    id : int
    userId : int
    title : str
    description : str
    categoryName : str | None
    image : str
    views : int
    author : returnUser
    createdAt : datetime
    updatedAt : datetime
    likedBy : list[int]
    dislikedBy : list[int]

    class Config():
        from_attributes = True



class updateBlogRequest(BaseModel):
    title : Optional[str] = Field(default=None)
    description : Optional[str] = Field(default=None)
    categoryId : Optional[int] = Field(default=None)

    @validator("title" , "description")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()