
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator

class ratingRequest(BaseModel):
    star : int = Field(... , le=5 , ge=1)
    comment : Optional[str] = Field(default=None)

    @validator("comment")
    def stripAndLower(cls , value:str):
        if value == None:
            return None
        value = value.strip()
        value = value.lower()

        return value

class returnRating(BaseModel):
    userId : int
    productId : int
    star : int
    comment : str | None

    class Config():
        form_attributes = True

class updateRating(BaseModel):
    star : Optional[int] = Field(default=None , le=5 , ge=1)
    comment : Optional[str] = Field(default=None)