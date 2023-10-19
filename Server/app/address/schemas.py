
from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel , EmailStr, Field


class AddressCreate(BaseModel):
    addressLine1 : str | None = None
    addressLine2 : str | None = None
    postalCode : str = Field(pattern=r"^[0-9]{6}$")
    country : str
    state : str
    city : str
    mobile : str = Field(pattern=r"^[0-9]{10}$")


class AddressInDB(AddressCreate):
    id : int
    userId : int
    createdAt : datetime
    updatedAt : datetime


class AddressReturn(AddressInDB):
    pass

    class Config:
        form_attributes = True


class AddressUpdate(BaseModel):
    addressLine1 : Optional[str] = None
    addressLine2 : Optional[str] = None
    postalCode : Annotated[Optional[str] , Field(pattern=r"^[0-9]{6}$")] = None
    country : Optional[str] = None
    state : Optional[str] = None
    city : Optional[str] = None
    mobile : Annotated[Optional[str] , Field(pattern=r"^[0-9]{10}$")] = None
