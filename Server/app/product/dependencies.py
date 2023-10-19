from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import getDb

import app.product.crud as prodCrud
import app.product.models as prodModel

def valid_product_id(id:int , db:Annotated[Session , Depends(getDb)]):
    product = prodCrud.get_product_by_id(db , id)

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    return product