
from typing import Optional , Annotated
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

class RatingCreate(BaseModel):
    star : int = Field(le=5 , ge=1)
    comment : str = Field(min_length=1)


class RatingInDb(RatingCreate):
    id : int
    userId : int
    productId : int
    createdAt : datetime
    updatedAt : datetime


class RatingReturn(RatingInDb):
    pass

    class config:
        form_attributes = True


class RatingUpdate(BaseModel):
    star : Annotated[Optional[int] , Field(le=5 , ge=1)] = None
    comment : Annotated[Optional[str] , Field(min_length=1)] = None

