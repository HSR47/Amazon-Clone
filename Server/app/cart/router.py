
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from app.database import getDb
from sqlalchemy.orm import Session


import app.cart.models as cartModel
import app.cart.schemas as cartSchema
import app.cart.crud as cartCrud
import app.user.models as userModel
import app.auth.dependencies as authDep
import app.user.dependencies as userDep
import app.cart.dependecies as cartDep
import app.product.models as prodModel
import app.product.dependencies as prodDep


cartRouter = APIRouter(tags=["Cart"])


# ----------------------------ADD TO CART-------------------------
@cartRouter.post("/user/me/product/{product_id}/cart", response_model=cartSchema.CartReturn)
def add_to_cart(
    *,
    product:Annotated[prodModel.Product , Depends(prodDep.valid_product_id)],
    data:cartSchema.CartCreate,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    checkCartItem = cartCrud.get_cart_item_by_product_id_and_user_id(db , product.id , curCust.id)
    if checkCartItem != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="product already added")

    cartItem = cartCrud.create_cart_item(db , curCust.id , product.id , data)
    return cartItem
# ------------------------------------------------------------------


# ----------------------------REMOVE FROM CART-------------------------
@cartRouter.delete("/user/me/cart/{cart_item_id}")
def remove_from_cart(
    *,
    cartItem:Annotated[cartModel.CartItem , Depends(cartDep.valid_cart_item_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if cartItem.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")

    cartCrud.delete_cart_item(db , cartItem)
    return {"message" : "removed"}
# ------------------------------------------------------------------


# ----------------------------GET CART-------------------------
@cartRouter.get("/user/me/cart" , response_model=list[cartSchema.CartReturn])
def get_cart(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    allCartItems = cartCrud.get_all_cart_items_by_user_id(db , curCust.id)
    return allCartItems
# ------------------------------------------------------------------


# ----------------------------UPDATE CART ITEM-------------------------
@cartRouter.patch("/user/me/cart/{cart_item_id}" , response_model=cartSchema.CartReturn)
def update_cart_item(
    *,
    cartItem:Annotated[cartModel.CartItem , Depends(cartDep.valid_cart_item_id)],
    data:cartSchema.CartUpdate,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if cartItem.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    cartItem = cartCrud.update_cart_item(db , cartItem , data)
    return cartItem
# ------------------------------------------------------------------


# ----------------------------CLEAR CART-------------------------
@cartRouter.delete("/user/me/cart")
def clear_cart(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):    
    allCartItems = cartCrud.get_all_cart_items_by_user_id(db , curCust.id)
    for cartItem in allCartItems:
        cartCrud.delete_cart_item(db , cartItem)
    
    return {"message" : "cleared"}
# ------------------------------------------------------------------

