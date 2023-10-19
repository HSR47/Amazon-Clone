
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.database import getDb

import app.cart.models as cartModel

def valid_cart_item_id(cart_item_id:int , db:Annotated[Session , Depends(getDb)]):
    cartItem = db.query(cartModel.CartItem).filter(cartModel.CartItem.id == cart_item_id).first()
    if cartItem == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="cart-item not found")
    
    return cartItem