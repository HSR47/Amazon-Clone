
from typing import Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

class scrapeRequest(BaseModel):
    category : str
    maxPage : int