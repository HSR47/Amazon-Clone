# wishlist schemas.py

from pydantic import BaseModel, Field
from datetime import datetime

import app.product.schemas as prodSchema

class WishlistCreate(BaseModel):
    pass

class WishlistInDB(WishlistCreate):
    id : int
    userId : int
    productId : int
    createdAt : datetime

class WishlistReturn(WishlistInDB):
    pass

    class Config():
        form_attributes = True

