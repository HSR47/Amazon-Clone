
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class addBrandRequest(BaseModel):
    name : str
    image : Optional[str] = Field(default=None)

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


class returnBrand(BaseModel):
    id : int
    name : str
    image : str | None
    createdAt : datetime
    updatedAt : datetime

    class Config():
        form_attributes = True


class updateBrandRequest(BaseModel):
    name : Optional[str] = Field(default=None)
    image : Optional[str] = Field(default=None)

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