from typing import Annotated
from fastapi import Depends , HTTPException , status
from sqlalchemy.orm import Session

import app.user.models as userModel
import app.user.schemas as userSchema
import app.user.crud as userCrud

from app.database import getDb


def valid_user_id(id:int , db:Annotated[Session , Depends(getDb)]):
    user:userModel.User = userCrud.get_user_by_id(db , id)

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user not found")
    
    return user