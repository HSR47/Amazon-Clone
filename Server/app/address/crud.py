
from sqlalchemy.orm import Session

import app.address.models as addressModel
import app.address.schemas as addressSchema


# ----------------------------RETRIEVE-------------------------
def get_address_by_id(db:Session , address_id:int):
    address = db.query(addressModel.Address).filter(addressModel.Address.id == address_id).first()
    return address

def get_all_address_by_user_id(db:Session , user_id:int):
    allUserAddress = db.query(addressModel.Address).filter(addressModel.Address.userId == user_id).all()
    return allUserAddress

def get_all_address(db:Session):
    allAddress = db.query(addressModel.Address)
    return allAddress
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_address(db:Session , userId:int , data:addressSchema.AddressCreate):
    newAddress = addressModel.Address(
        userId = userId,
        addressLine1 = data.addressLine1,
        addressLine2 = data.addressLine2,
        postalCode = data.postalCode,
        country = data.country,
        state = data.state,
        city = data.city,
        mobile = data.mobile
    )

    db.add(newAddress)
    db.commit()
    db.refresh(newAddress)

    return newAddress
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_address(db:Session , address:addressModel.Address , data:addressSchema.AddressUpdate):
    if data.addressLine1 != None:
        address.addressLine1 = data.addressLine1
    
    if data.addressLine2 != None:
        address.addressLine2 = data.addressLine2
    
    if data.postalCode != None:
        address.postalCode = data.postalCode
    
    if data.country != None:
        address.country = data.country
    
    if data.state != None:
        address.state = data.state
    
    if data.city != None:
        address.city = data.city
    
    if data.mobile != None:
        address.mobile = data.mobile
    
    db.commit()
    db.refresh(address)

    return address
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_address(db:Session , address:addressModel.Address):
    db.delete(address)
    db.commit()
# ------------------------------------------------------------------