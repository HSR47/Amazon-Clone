
from fastapi import APIRouter , Depends , HTTPException, Query , status
from httpx import delete

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.brandModel import Brand
from app.models.cartModel import CartItem
from app.models.couponModel import Coupon
from app.models.orderModel import Order, OrderItem
from app.models.productModel import Product

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_customer, get_current_user
import app.schemas.brandSchema as brandSchema
from app.schemas.cartSchema import addToCartRequest, returnCart, updateCartRequest
from app.schemas.orderSchema import returnOrder, updateOrderRequest

orderRouter = APIRouter(tags=["Order"])


# ----------------------------PLACE ORDER-------------------------
@orderRouter.get("/place-order")
def place_order(curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    if curCust.cartItems == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="cart is empty")

    order = Order(
        userId = curCust.id
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for cartItem in curCust.cartItems:
        orderItem = OrderItem(
            orderId = order.id,
            productId = cartItem.productId,
            count = cartItem.count,
            price = (cartItem.disPrice).__ceil__()
        )

        db.add(orderItem)
    
    db.commit()
    db.refresh(order)

    return {"message" : "order placed"}
# ------------------------------------------------------------------


# ----------------------------GET ALL ORDERS-------------------------
@orderRouter.get("/order" , response_model=list[returnOrder])
def get_all_orders(id:int = Query(default=None) , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    
    allOrders = db.query(Order)

    if id != None:
        customer = db.query(User).filter((User.id == id) & (User.role=="customer")).first()
        if customer == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="customer not found")
    
        allOrders = allOrders.filter(Order.userId == id)
    
    allOrders = allOrders.all()
    
    return allOrders
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC ORDER-------------------------
@orderRouter.get("/order/{id}" , response_model=returnOrder)
def get_specific_order(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    order = db.query(Order).filter(Order.id == id).first()
    if order == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="order not found")
    
    return order
# ------------------------------------------------------------------


# ----------------------------GET CUSTOMER ORDER-------------------------
@orderRouter.get("/cust-order" , response_model=list[returnOrder])
def get_customer_order(curCust:User = Depends(get_current_customer) , db:Session = Depends(getDb)):
    allOrders = db.query(Order).filter(Order.userId == curCust.id).all()
    return allOrders
# ------------------------------------------------------------------


# ----------------------------UPDATE ORDER STATUS-------------------------
@orderRouter.put("/order/{id}")
def update_order_status(id:int , data:updateOrderRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    
    order:Order = db.query(Order).filter(Order.id == id).first()
    if order == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="order not found")
    
    order.status = data.status
    db.commit()
    
    return {"message" : "updated"}
# ------------------------------------------------------------------