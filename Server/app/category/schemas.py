
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CategoryCreate(BaseModel):
    name : str
    image : str


class CategoryInDB(CategoryCreate):
    id : int
    createdAt : datetime
    updatedAt : datetime


class CategoryReturn(CategoryInDB):
    pass

    class Config:
        form_attributes = True


class CategoryUpdate(BaseModel):
    name : Optional[str] = None
    image : Optional[str] = None

