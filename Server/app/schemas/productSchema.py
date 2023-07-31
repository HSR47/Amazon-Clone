
from typing import Optional
from click import Option
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class addProduct(BaseModel):
    title : str
    description : str
    price : int
    quantity : int
    sold : Optional[int] = Field(default=0)
    color : Optional[str] = Field(default=None)
    brand : Optional[str] = Field(default=None)
    categoryId : Optional[int] = Field(default=None)

    @validator("title" , "description" , "color" , "brand")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description" , "color" , "brand")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()


class returnProduct(BaseModel):
    id : int
    title : str
    slug : str
    description : str
    price : int
    quantity : int
    sold : int | None
    color : str | None
    brand : str | None
    ratings : list
    # categoryId : int | None
    categoryName : str | None
    createdAt : datetime
    updatedAt : datetime

    class config:
        from_attributes = True


class updateProduct(BaseModel):
    title : str | None
    description : str | None
    price : int | None
    quantity : int | None
    sold : Optional[int] = Field(default=0)
    color : Optional[str]
    brand : Optional[str]
    categoryId : Optional[int] = Field(default=None)

    @validator("title" , "description" , "color" , "brand")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description" , "color" , "brand")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()