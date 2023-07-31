

from typing import Optional
from click import Option
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime

class wishlistRequest(BaseModel):
    productId : int