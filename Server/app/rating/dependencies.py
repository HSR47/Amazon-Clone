from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import getDb

import app.rating.models as ratingModel
import app.rating.schemas as ratingSchema
import app.rating.crud as ratingCrud

def valid_rating_id(rating_id:int , db:Annotated[Session , Depends(getDb)]):
    rating = ratingCrud.get_rating_by_id(db , rating_id)
    if rating == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="rating not found")
    
    return rating