
from sqlalchemy.orm import Session

import app.order.models as orderModel
import app.order.schemas as orderSchema
import app.address.models as addressModel
import app.user.models as userModel
import app.product.models as prodModel
import app.cart.models as cartModel


# ----------------------------RETRIEVE-------------------------
def get_order_by_id(db:Session , order_id:int):
    order:orderModel.Order = db.query(orderModel.Order).filter(orderModel.Order.id == order_id).first()
    return order

def get_all_orders_by_user_id(db:Session , user_id:int, offset:int = 0 , limit:int = 100):
    orders:list[orderModel.Order] = db.query(orderModel.Order).filter(orderModel.Order.userId == user_id).offset(offset).limit(limit).all()
    return orders

def get_all_order_by_status(db:Session , status:str, offset:int = 0 , limit:int = 100):
    orders:list[orderModel.Order] = db.query(orderModel.Order).filter(orderModel.Order.status == status).offset(offset).limit(limit).all()
    return orders

def get_all_orders(db:Session , offset:int = 0 , limit:int = 100):
    orders:list[orderModel.Order] = db.query(orderModel.Order).offset(offset).limit(limit).all()
    return orders
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_order(db:Session, address:addressModel.Address, user_id:int):
    newOrder = orderModel.Order(
        userId = user_id,
        status = "pending",
        addressLine1 = address.addressLine1,
        addressLine2 = address.addressLine2,
        postalCode = address.postalCode,
        country = address.country,
        state = address.state,
        city = address.city,
        mobile = address.mobile
    )

    db.add(newOrder)
    db.commit()

    return newOrder

def create_order_item(db:Session, order:orderModel.Order , product:prodModel.Product, cartItem:cartModel.CartItem):
    product.quantity -= cartItem.count

    newOrderItem = orderModel.OrderItem(
        orderId = order.id,
        productId = product.id,
        count = cartItem.count,
        price = product.discountPrice
    )

    db.add(newOrderItem)
    db.commit()
    return newOrderItem
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_order_status(db:Session, order:orderModel.Order , status:str):
    order.status = status
    db.commit()

    return order
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_order_item(db:Session, order_item:orderModel.OrderItem):
    product:prodModel.Product = order_item.product
    product.quantity += order_item.count

    db.delete(order_item)
    db.commit()

def delete_order(db:Session, order:orderModel.Order):
    for i in order.orderItems:
        orderItem:orderModel.OrderItem = i
        delete_order_item(db , orderItem)
    db.delete(order)
    db.commit()
# ------------------------------------------------------------------