

from sqlalchemy.orm import Session

import app.cart.models as cartModel
import app.cart.schemas as cartSchema


# ----------------------------RETRIEVE-------------------------
def get_cart_item_by_id(db:Session , cart_item_id:int):
    cart_item = db.query(cartModel.CartItem).filter(cartModel.CartItem.id == cart_item_id).first()
    return cart_item

def get_cart_item_by_product_id_and_user_id(db:Session , product_id:int , user_id:int):
    cartItem = db.query(cartModel.CartItem).filter((cartModel.CartItem.userId==user_id) & (cartModel.CartItem.productId==product_id)).first()
    return cartItem

def get_all_cart_items_by_user_id(db:Session , user_id:int):
    allUserCartItems = db.query(cartModel.CartItem).filter(cartModel.CartItem.userId == user_id).all()
    return allUserCartItems

def get_all_cart_items(db:Session):
    allCartItems = db.query(cartModel.CartItem)
    return allCartItems
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_cart_item(db:Session , userId:int , productId:int , data:cartSchema.CartCreate):
    newCartItem = cartModel.CartItem(
        userId = userId,
        productId = productId,
        count = data.count
    )

    db.add(newCartItem)
    db.commit()
    db.refresh(newCartItem)

    return newCartItem
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_cart_item(db:Session , cart_item:cartModel.CartItem , data:cartSchema.CartUpdate):
    if data.count != None:
        cart_item.count = data.count

    db.commit()

    return cart_item
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_cart_item(db:Session , cart_item:cartModel.CartItem):
    db.delete(cart_item)
    db.commit()
# ------------------------------------------------------------------