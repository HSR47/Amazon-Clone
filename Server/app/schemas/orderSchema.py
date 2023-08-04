
from enum import Enum
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

from app.schemas.productSchema import returnProduct


class returnOrderItemsInOrder(BaseModel):
    product : returnProduct
    count : int
    price : int

    class config:
        form_attributes = True

class returnOrder(BaseModel):
    id : int
    userId : int
    status : Enum
    total : int
    createdAt : datetime
    updatedAt : datetime
    orderItems : list[returnOrderItemsInOrder]

    class config:
        form_attributes = True

class updateOrderRequest(BaseModel):
    status : str = Field(pattern=r"^(pending|processing|shipped|delivered|cancelled)$")
