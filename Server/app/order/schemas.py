
from enum import Enum
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class placeOrderRequest(BaseModel):
    method : str = Field(pattern=r"^(cod)$")



class updateOrderRequest(BaseModel):
    status : str = Field(pattern=r"^(pending|processing|shipped|delivered|cancelled)$")






class returnPaymentInOrder(BaseModel):
    id : int
    method : Enum
    amount : int

    class config:
        form_attributes = True


class returnOrderItemsInOrder(BaseModel):
    # product : returnProduct
    count : int
    price : int

    class config:
        form_attributes = True


class returnOrder(BaseModel):
    id : int
    userId : int
    status : Enum
    payment : returnPaymentInOrder
    createdAt : datetime
    updatedAt : datetime
    orderItems : list[returnOrderItemsInOrder]

    class config:
        form_attributes = True







