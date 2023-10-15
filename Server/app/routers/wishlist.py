
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.productModel import Product

from app.models.userModel import User
from app.models.wishlistModel import Wishlist
from app.routers.auth import get_current_admin, get_current_customer, get_current_user

wishRouter = APIRouter(tags=["Wishlist"])


# ----------------------------ADD TO WISHLIST-------------------------
@wishRouter.put("/wishlist/{id}")
def add_To_Wishlist(id:int , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    check = db.query(Wishlist).filter((Wishlist.userId==curCust.id) & (Wishlist.productId==id)).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="already added")

    wishlist = Wishlist(
        userId = curCust.id,
        productId = id
    )

    db.add(wishlist)
    db.commit()

    return {"message" : "added"}
# ------------------------------------------------------------------


# ----------------------------REMOVE FROM WISHLIST-------------------------
@wishRouter.delete("/wishlist/{id}")
def remove_From_Wishlist(id:int , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    check = db.query(Wishlist).filter((Wishlist.userId==curCust.id) & (Wishlist.productId==id)).first()
    if check == None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="product not added to wishlist")
    
    db.delete(check)
    db.commit()

    return {"message" : "removed"}
# ------------------------------------------------------------------