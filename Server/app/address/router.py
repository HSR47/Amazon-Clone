from fastapi import APIRouter , HTTPException , status , Depends
from app.address.models import Address
from app.user.models import User
from app.auth.dependencies import get_current_customer

from app.address.schemas import createAddress, returnAddress, updateAddress

from app.database import getDb
from sqlalchemy.orm.session import Session

addressRouter = APIRouter(tags=["Address"])


# ----------------------------CREATE ADDRESS-------------------------
@addressRouter.post("/address")
def create_address(data:createAddress , curCust:User = Depends(get_current_customer) , db:Session =  Depends(getDb)):

    address = Address(
        userId = curCust.id,
        addressLine1 = data.addressLine1,
        addressLine2 = data.addressLine2,
        postalCode = data.postalCode,
        country = data.country,
        state = data.state,
        city = data.city,
        mobile = data.mobile
    )

    db.add(address)
    db.commit()

    return {"message" : "created"}
# ------------------------------------------------------------------


# ----------------------------GET ALL ADDRESS-------------------------
@addressRouter.get("/address" , response_model=list[returnAddress])
def get_all_address(curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    allAddresses = db.query(Address).filter(Address.userId == curCust.id).all()
    return allAddresses
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC ADDRESS-------------------------
@addressRouter.get("/address/{id}" , response_model=returnAddress)
def get_specific_address(id:int , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):
    
    address = db.query(Address).filter((Address.id == id) & (Address.userId == curCust.id)).first()
    if address == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="address not found")
    
    return address
# ------------------------------------------------------------------


# ----------------------------UPDATE ADDRESS-------------------------
@addressRouter.put("/address/{id}" , response_model=returnAddress)
def update_address(id:int , data:updateAddress , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    address = db.query(Address).filter((Address.id == id) & (Address.userId == curCust.id)).first()
    if address == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="address not found")
    
    address.addressLine1 = data.addressLine1
    address.addressLine2 = data.addressLine2
    address.postalCode = data.postalCode
    address.country = data.country
    address.state = data.state
    address.city = data.city
    address.mobile = data.mobile

    db.commit()
    db.refresh(address)

    return address
# ------------------------------------------------------------------


# ----------------------------DELETE ADDRESS-------------------------
@addressRouter.delete("/address/{id}")
def delete_address(id:int , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    address = db.query(Address).filter((Address.id == id) & (Address.userId == curCust.id)).first()
    if address == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="address not found")
    
    db.delete(address)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------