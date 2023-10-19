
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

from app.rating.schemas import returnRating


class addToCartRequest(BaseModel):
    count : int = Field(... , ge=1)


class updateCartRequest(BaseModel):
    count : int = Field(... , ge=1)


class returnCartItem(BaseModel):
    id : int
    count : int
    createdAt : datetime
    updatedAt : datetime

    class Config():
        form_attributes = True

