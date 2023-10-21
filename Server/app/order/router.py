
from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, status

from app.database import getDb
from sqlalchemy.orm.session import Session

import app.order.models as orderModel
import app.cart.models as cartModel
import app.user.models as userModel
import app.auth.dependencies as authDep
import app.order.schemas as orderSchema
import app.address.dependecies as addressDep
import app.address.models as addressModel
import app.order.crud as orderCrud
import app.product.models as prodModel
import app.order.dependencies as orderDep
import app.cart.crud as cartCrud
import app.user.dependencies as userDep

orderRouter = APIRouter(tags=["Order"])


# ----------------------------PLACE ORDER-------------------------
@orderRouter.post("/user/me/address/{address_id}/order" , response_model=orderSchema.OrderReturn)
def place_order(
    *,
    address:Annotated[addressModel.Address , Depends(addressDep.valid_address_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)],
):

    if curCust.cartItems == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="cart is empty")

    newOrder:orderModel.Order = orderCrud.create_order(db , address , curCust.id)
    
    for i in curCust.cartItems:
        cartItem:cartModel.CartItem = i
        product:prodModel.Product = cartItem.product

        if product.quantity < cartItem.count:
            orderCrud.delete_order(db , newOrder)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail=f"not enough quantity for product-id {product.id}")

        newOrderItem:orderModel.OrderItem = orderCrud.create_order_item(db , newOrder , product , cartItem)
    
    db.refresh(newOrder)

    for i in curCust.cartItems:
        cartCrud.delete_cart_item(db , i)
    
    return newOrder
# ------------------------------------------------------------------


# ----------------------------GET CUSTOMER ORDER-------------------------
@orderRouter.get("/user/me/order" , response_model=list[orderSchema.OrderReturn])
def get_customer_order(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)],
):
    allCustomerOrders = orderCrud.get_all_orders_by_user_id(db , curCust.id)
    return allCustomerOrders
# ------------------------------------------------------------------


# ----------------------------GET CUSTOMER SPECIFIC ORDER-------------------------
@orderRouter.get("/user/me/order/{order_id}" , response_model=orderSchema.OrderReturn)
def get_customer_specific_order(
    *,
    order:Annotated[orderModel.Order , Depends(orderDep.valid_order_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)],
):
    if order.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    return order
# ------------------------------------------------------------------


# ----------------------------GET ALL ORDERS (ADMIN)-------------------------
@orderRouter.get("/admin/me/order" , response_model=list[orderSchema.OrderReturn])
def get_all_orders(
    *,
    offset:int = 0,
    limit:int = 100,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)],
):
    allOrders = orderCrud.get_all_orders(db, offset, limit)    
    return allOrders
# ------------------------------------------------------------------


# -----------------------GET ALL ORDERS OF A CUSTOMER (ADMIN)-------------------
@orderRouter.get("/admin/me/user/{user_id}/order" , response_model=list[orderSchema.OrderReturn])
def get_all_orders_of_a_customer(
    *,
    user:Annotated[userModel.User , Depends(userDep.valid_user_id)],
    offset:int = 0,
    limit:int = 100,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    allCustomerOrders = orderCrud.get_all_orders_by_user_id(db , user.id, offset, limit)
    return allCustomerOrders
# ------------------------------------------------------------------



# ----------------------------GET SPECIFIC ORDER (ADMIN)-------------------------
@orderRouter.get("/admin/me/order/{order_id}" , response_model=orderSchema.OrderReturn)
def get_specific_order(
    *,
    order:Annotated[orderModel.Order , Depends(orderDep.valid_order_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
):    
    return order
# ------------------------------------------------------------------


# ----------------------------UPDATE ORDER STATUS (ADMIN)-------------------------
@orderRouter.put("/admin/me/order/{order_id}" , response_model=orderSchema.OrderReturn)
def update_order_status(
    *,
    order:Annotated[orderModel.Order , Depends(orderDep.valid_order_id)],
    status:Annotated[str , Body(embed=True)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    updatedOrder = orderCrud.update_order_status(db , order , status)
    return updatedOrder
# ------------------------------------------------------------------