
from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import getDb

import app.brand.crud as brandCrud
import app.brand.models as brandModel


def valid_brand_id(id:int , db:Annotated[Session , Depends(getDb)]):
    brand:brandModel.Brand = brandCrud.get_brand_by_id(db , id)
    
    if brand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")
    
    return brand