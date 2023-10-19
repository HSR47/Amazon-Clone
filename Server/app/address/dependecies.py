
from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import getDb

import app.address.models as addressModel
import app.address.schemas as addressSchema


def valid_address_id(address_id:int , db:Annotated[Session , Depends(getDb)]):
    address = db.query(addressModel.Address).filter(addressModel.Address.id == address_id).first()
    if address == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="address not found")
    
    return address