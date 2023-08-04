
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime
from app.schemas.productSchema import returnProduct

from app.schemas.ratingSchema import returnRating


class addToCartRequest(BaseModel):
    count : int = Field(... , ge=1)

class updateCartRequest(BaseModel):
    count : Optional[int] = Field(default=None , ge=1)



class returnCartItem(BaseModel):
    id : int
    product : returnProduct
    count : int
    price : int
    disPrice : float

    class Config():
        form_attributes = True

