
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class addCategoryRequest(BaseModel):
    name : str
    image : str | None

    @validator("name")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("name")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()


class returnCategory(BaseModel):
    id : int
    name : str
    image : str | None
    createdAt : datetime
    updatedAt : datetime

    class Config():
        form_attributes = True


class updateCategoryRequest(BaseModel):
    name : str
    image : str | None

    @validator("name")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("name")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()