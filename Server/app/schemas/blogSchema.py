
from typing import Any
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class createBlogRequest(BaseModel):
    title : str
    description : str
    category : str
    views : int | None
    isLiked : bool | None
    isDisliked : bool | None
    image : str | None

    @validator("title" , "description" , "category")
    def validateStrip(cls , value:str):
        return value.strip()

    @validator("title" , "description" , "category")
    def validateLowerCase(cls , value:str):
        return value.lower()



class returnBlog(BaseModel):
    id : int
    userId : int
    title : str
    description : str
    category : str
    views : int | None
    isLiked : bool | None
    isDisliked : bool | None
    image : str | None
    author : Any
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True