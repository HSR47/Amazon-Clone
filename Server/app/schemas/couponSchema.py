
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

class createCouponRequest(BaseModel):
    name : str
    discount : int = Field(le=100 , ge=0)
    expiry : datetime

    @validator("name")
    def validateName(cls , value:str):
        value = value.strip()
        value = value.upper()
        return value
    

class returnCoupon(BaseModel):
    id : int
    name : str
    discount : int
    expiry : datetime

    class Config():
        form_attributes = True


class updateCoupon(BaseModel):
    name : Optional[str] = Field(default=None)
    discount : Optional[int] = Field(default=None , ge=0 , le=100)
    expiry : Optional[datetime] = Field(default=None)

    @validator("name")
    def validateName(cls , value:str):
        value = value.strip()
        value = value.upper()
        return value