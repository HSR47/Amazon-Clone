
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime
from app.schemas.productSchema import returnProduct

from app.schemas.ratingSchema import returnRating


class addToCartRequest(BaseModel):
    count : int = Field(... , ge=1)


class returnCart(BaseModel):
    id : int
    product : returnProduct
    count : int
    price : int
    disPrice : float
    couponId : int | None

    class Config():
        form_attributes = True


class updateCartRequest(BaseModel):
    count : Optional[int] = Field(default=None , ge=1)