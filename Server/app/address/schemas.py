
from datetime import datetime
from pydantic import BaseModel , EmailStr, Field


class createAddress(BaseModel):
    addressLine1 : str
    addressLine2 : str
    postalCode : str = Field(pattern=r"^[0-9]{6}$")
    country : str
    state : str
    city : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")


class updateAddress(BaseModel):
    addressLine1 : str
    addressLine2 : str
    postalCode : str = Field(pattern=r"^[0-9]{6}$")
    country : str
    state : str
    city : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")


class returnAddress(BaseModel):
    id : int
    userId : int
    addressLine1 : str
    addressLine2 : str
    postalCode : str
    country : str
    state : str
    city : str
    mobile : str
    createdAt : datetime
    updatedAt : datetime

    class Config:
        form_attributes = True
