
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

from app.rating.schemas import returnRating

class CartCreate(BaseModel):
    count : int = Field(... , ge=1)


class CartInDB(CartCreate):
    id : int
    userId : int
    productId : int
    createdAt : datetime
    updatedAt : datetime


class CartReturn(CartInDB):
    pass

    class Config():
        form_attributes = True


class CartUpdate(BaseModel):
    count : Optional[int] = None



# class addToCartRequest(BaseModel):
#     count : int = Field(... , ge=1)


# class updateCartRequest(BaseModel):
#     count : int = Field(... , ge=1)


# class returnCartItem(BaseModel):
#     id : int
#     count : int
#     createdAt : datetime
#     updatedAt : datetime

#     class Config():
#         form_attributes = True

