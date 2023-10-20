
from pydantic import BaseModel , EmailStr, Field


class loginUser(BaseModel):
    email : EmailStr
    password : str
    