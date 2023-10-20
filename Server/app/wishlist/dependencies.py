
from sqlalchemy.orm import Session
from app.database import getDb
from fastapi import Depends, HTTPException, status
from typing import Annotated

import app.wishlist.models as wishlistModel
import app.wishlist.crud as wishlistCrud

def valid_wishlist_id(wishlist_id:int , db:Annotated[Session , Depends(getDb)]):
    wishlist = wishlistCrud.get_wishlist_by_id(db , wishlist_id)
    if wishlist == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="wishlist-item not found")
    
    return wishlist