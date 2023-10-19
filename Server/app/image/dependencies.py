
from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import getDb

import app.image.models as imgModel
import app.image.schemas as imgSchema
import app.image.crud as imgCrud

def valid_image_id(image_id:int , db:Annotated[Session , Depends(getDb)]):
    image = imgCrud.get_image_by_id(db , image_id)
    if image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="image not found")
    return image