
from fastapi import APIRouter , Depends , HTTPException , status
from httpx import delete

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.brandModel import Brand
from app.models.cartModel import CartItem
from app.models.productModel import Product

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_customer, get_current_user
import app.schemas.brandSchema as brandSchema
from app.schemas.cartSchema import addToCartRequest, returnCartItem, updateCartRequest

cartRouter = APIRouter(tags=["Cart"])


# ----------------------------ADD TO CART-------------------------
@cartRouter.post("/cart/{id}")
def add_to_cart(id:int , data:addToCartRequest , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):
    
    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    check:CartItem = db.query(CartItem).filter((CartItem.userId==curCust.id) & (CartItem.productId==id)).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="product already added")
    
    cartItem = CartItem(
        userId = curCust.id,
        productId = id,
        count = data.count,
    )

    db.add(cartItem)
    db.commit()
    db.refresh(cartItem)

    return {"message" : "added"}
# ------------------------------------------------------------------


# ----------------------------REMOVE FROM CART-------------------------
@cartRouter.delete("/cart/{id}")
def remove_from_cart(id:int , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):
    
    cartItem:CartItem = db.query(CartItem).filter(CartItem.id == id).first()
    if cartItem == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="cart-item not found")
    
    db.delete(cartItem)
    db.commit()

    return {"message" : "removed"}
# ------------------------------------------------------------------


# ----------------------------GET CART-------------------------
@cartRouter.get("/cart" , response_model=list[returnCartItem])
def get_cart(curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    allItems = db.query(CartItem).filter(CartItem.userId == curCust.id).all()
    
    return allItems
# ------------------------------------------------------------------


# ----------------------------UPDATE CART ITEM-------------------------
@cartRouter.patch("/cart/{id}")
def update_cart(id:int , data:updateCartRequest , curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    cartItem:CartItem = db.query(CartItem).filter(CartItem.id == id).first()
    if cartItem == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="cart-item not found")
    
    cartItem.count = data.count
    
    db.commit()

    return {"message" : "updated"}
# ------------------------------------------------------------------


# ----------------------------CLEAR CART-------------------------
@cartRouter.delete("/clear-cart")
def clear_cart(curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):
    
    allCartItems = db.query(CartItem).filter(CartItem.userId == curCust.id).all()
    for i in allCartItems:
        db.delete(i)
    db.commit()

    return {"message" : "cleared"}
# ------------------------------------------------------------------

