
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime


class addColorRequest(BaseModel):
    name : str

class updateColorRequest(BaseModel):
    name : Optional[str] = Field(default=None)


class returnColor(BaseModel):
    id : int
    name : str
    createdAt : datetime
    updatedAt : datetime

    class config:
        form_attributes = True