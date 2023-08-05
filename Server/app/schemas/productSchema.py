
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

from app.schemas.ratingSchema import returnRating


class addProduct(BaseModel):
    title : str
    description : str
    price : int
    quantity : int
    sold : Optional[int] = Field(default=0)
    colors : Optional[list[int]] = Field(default=None)
    brandId : Optional[int] = Field(default=None)
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
    
    @validator("colors")
    def validateUniqueColor(cls , value:list[int]):
        if value == None:
            return None

        return list(set(value))






class updateProduct(BaseModel):
    title : str | None
    description : str | None
    price : int | None
    quantity : int | None
    sold : Optional[int] = Field(default=0)
    colors : Optional[list[int]] = Field(default=None)
    brandId : Optional[int] = Field(default=None)
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

    @validator("colors")
    def validateUniqueColor(cls , value:list[int]):
        if value == None:
            return None

        return list(set(value))




class returnImageInProduct(BaseModel):
    id : int
    name : str
    url : str

    class config:
        from_attributes = True
        
class returnColorInProduct(BaseModel):
    id : int
    name : str

class returnProduct(BaseModel):
    id : int
    title : str
    slug : str
    description : str
    price : int
    quantity : int
    sold : int | None
    colors : list[returnColorInProduct]
    ratings : list
    brandName : str | None
    categoryName : str | None
    createdAt : datetime
    updatedAt : datetime
    ratings : list[returnRating]
    avgRating : float
    images : list[returnImageInProduct]

    class config:
        from_attributes = True


