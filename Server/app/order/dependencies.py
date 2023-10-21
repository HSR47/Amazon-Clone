from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import getDb

import app.order.models as orderModel
import app.order.schemas as orderSchema
import app.order.crud as orderCrud


def valid_order_id(order_id:int , db:Annotated[Session , Depends(getDb)]):
    order:orderModel.Order = orderCrud.get_order_by_id(db , order_id)
    
    if order == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="order not found")
    
    return order