from typing import Annotated
from fastapi import APIRouter , HTTPException , status , Depends
from app.address.models import Address
from app.database import getDb

import app.address.models as addressModel
import app.address.schemas as addressSchema
import app.address.crud as addressCrud
import app.user.models as userModel
import app.auth.dependencies as authDep
import app.user.dependencies as userDep
import app.address.dependecies as addressDep

from sqlalchemy.orm.session import Session

addressRouter = APIRouter(tags=["Address"])


# ----------------------------CREATE ADDRESS-------------------------
@addressRouter.post("/user/me/address" , response_model=addressSchema.AddressReturn)
def create_address(
    *,
    data:addressSchema.AddressCreate,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    newAddress = addressCrud.create_address(db , curCust.id , data)
    return newAddress
# ------------------------------------------------------------------


# ----------------------------GET ALL ADDRESS-------------------------
@addressRouter.get("/user/me/address" , response_model=list[addressSchema.AddressReturn])
def get_all_address(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    allCustAddress = addressCrud.get_all_address_by_user_id(db , curCust.id)
    return allCustAddress
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC ADDRESS-------------------------
@addressRouter.get("/user/me/address/{address_id}" , response_model=addressSchema.AddressReturn)
def get_specific_address(
    *,
    address:Annotated[addressModel.Address , Depends(addressDep.valid_address_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
):
    if address.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")

    return address
# ------------------------------------------------------------------


# ----------------------------UPDATE ADDRESS-------------------------
@addressRouter.put("/user/me/address/{address_id}" , response_model=addressSchema.AddressReturn)
def update_address(
    *,
    address:Annotated[addressModel.Address , Depends(addressDep.valid_address_id)],
    data:addressSchema.AddressUpdate,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if address.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")

    updatedAddress = addressCrud.update_address(db , address , data)
    return updatedAddress
# ------------------------------------------------------------------


# ----------------------------DELETE ADDRESS-------------------------
@addressRouter.delete("/user/me/address/{address_id}")
def delete_address(
    *,
    address:Annotated[addressModel.Address , Depends(addressDep.valid_address_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if address.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    addressCrud.delete_address(db , address)

    return {"message" : "deleted"}
# ------------------------------------------------------------------