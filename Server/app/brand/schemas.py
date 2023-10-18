
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class BrandCreate(BaseModel):
    name : str
    image : str


class BrandInDB(BrandCreate):
    id : int
    createdAt : datetime
    updatedAt : datetime


class BrandReturn(BrandInDB):
    pass

    class Config:
        form_attributes = True


class BrandUpdate(BaseModel):
    name : Optional[str] = None
    image : Optional[str] = None
