
from enum import Enum
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime



# ----------------------------ORDER ITEM-------------------------
class OrderItemCreate(BaseModel):
    pass


class OrderItemInDB(OrderItemCreate):
    id : int
    orderId : int
    productId : int
    count : int
    price : int


class OrderItemReturn(OrderItemInDB):
    pass

    class Config():
        form_attributes = True
# ------------------------------------------------------------------



# ----------------------------ORDER-------------------------
class OrderCreate(BaseModel):
    pass


class OrderInDB(OrderCreate):
    id : int
    userId : int
    status : str
    addressLine1 : str
    addressLine2 : str
    postalCode : str
    country : str
    state : str
    city : str
    mobile : str
    createdAt : datetime
    updatedAt : datetime


class OrderReturn(OrderInDB):
    pass

    orderItems : list[OrderItemReturn]

    class Config():
        form_attributes = True
# ------------------------------------------------------------------



