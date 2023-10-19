
from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from typing import Annotated

from app.database import getDb

import app.category.crud as catCrud
import app.category.models as catModel


def valid_category_id(category_id:int , db:Annotated[Session , Depends(getDb)]):
    category:catModel.ProdCategory = catCrud.get_category_by_id(db , category_id)
    
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")
    
    return category