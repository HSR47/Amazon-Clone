

from datetime import datetime
from pydantic import BaseModel, Field


class ImageCreate(BaseModel):
    productId : int
    thumbnail : bool


class ImageInDB(ImageCreate):
    id : int
    name : str
    url : str
    createdAt : datetime
    publicId : str


class ImageReturn(ImageInDB):
    publicId : str = Field(exclude=True)

    class Config:
        form_attributes = True

