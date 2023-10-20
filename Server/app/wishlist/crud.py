from sqlalchemy.orm import Session

import app.wishlist.models as wishlistModel

# ----------------------------RETRIEVE-------------------------
def get_wishlist_by_id(db:Session , wishlist_id:int):
    wishlist = db.query(wishlistModel.Wishlist).filter(wishlistModel.Wishlist.id == wishlist_id).first()
    return wishlist

def get_wishlist_by_product_id_and_user_id(db:Session , product_id:int , user_id:int):
    wishlist = db.query(wishlistModel.Wishlist).filter((wishlistModel.Wishlist.productId == product_id) & (wishlistModel.Wishlist.userId == user_id)).first()
    return wishlist

def get_all_wishlist_by_user_id(db:Session , user_id:int):
    wishlist = db.query(wishlistModel.Wishlist).filter(wishlistModel.Wishlist.userId == user_id).all()
    return wishlist

def get_all_wishlist_by_product_id(db:Session , product_id:int):
    wishlist = db.query(wishlistModel.Wishlist).filter(wishlistModel.Wishlist.productId == product_id).all()
    return wishlist

def get_all_wishlist(db:Session):
    wishlist = db.query(wishlistModel.Wishlist)
    return wishlist
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_wishlist(db:Session , user_id:int , product_id:int):
    wishlist = wishlistModel.Wishlist(
        userId = user_id,
        productId = product_id
    )

    db.add(wishlist)
    db.commit()
    db.refresh(wishlist)

    return wishlist
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_wishlist(db:Session , wishlist:wishlistModel.Wishlist):
    db.delete(wishlist)
    db.commit()
# ------------------------------------------------------------------