
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from app.database import getDb


import app.wishlist.models as wishlistModel
import app.wishlist.crud as wishlistCrud
import app.wishlist.schemas as wishlistSchema
import app.wishlist.dependencies as wishlistDep
import app.product.models as prodModel
import app.user.models as userModel
import app.product.dependencies as prodDep
import app.auth.dependencies as authDep


wishRouter = APIRouter(tags=["Wishlist"])

# ----------------------------GET SPECIFIC WISHLIST-------------------------
@wishRouter.get("/user/me/wishlist/{wishlist_id}" , response_model=wishlistSchema.WishlistReturn)
def get_specific_wishlist(
    *,
    wishlist:Annotated[wishlistModel.Wishlist , Depends(wishlistDep.valid_wishlist_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
):
    if wishlist.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    return wishlist
# ------------------------------------------------------------------


# ----------------------------GET CUSTOMER WISHLIST-------------------------
@wishRouter.get("/user/me/wishlist" , response_model=list[wishlistSchema.WishlistReturn])
def get_all_customer_wishlist(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    wishlist = wishlistCrud.get_all_wishlist_by_user_id(db , curCust.id)
    return wishlist
# ------------------------------------------------------------------


# ----------------------------ADD TO WISHLIST-------------------------
@wishRouter.post("/user/me/product/{product_id}/wishlist" , response_model=wishlistSchema.WishlistReturn)
def add_To_Wishlist(
    *,
    product:Annotated[prodModel.Product , Depends(prodDep.valid_product_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    checkWishlist = wishlistCrud.get_wishlist_by_product_id_and_user_id(db , product.id , curCust.id)
    if checkWishlist != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="already added to wishlist")
    
    wishlistItem = wishlistCrud.create_wishlist(db , curCust.id , product.id)
    return wishlistItem
# ------------------------------------------------------------------


# ----------------------------REMOVE FROM WISHLIST-------------------------
@wishRouter.delete("/user/me/wishlist/{wishlist_id}")
def remove_From_Wishlist(
    *,
    wishlist:Annotated[wishlistModel.Wishlist , Depends(wishlistDep.valid_wishlist_id)],
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if wishlist.userId != curCust.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    wishlistCrud.delete_wishlist(db , wishlist)
    return {"message" : "deleted"}
# ------------------------------------------------------------------


# ----------------------------CLEAR WISHLIST-------------------------
@wishRouter.delete("/user/me/wishlist")
def clear_Wishlist(
    *,
    curCust:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    allWishlist = wishlistCrud.get_all_wishlist_by_user_id(db , curCust.id)
    
    for wishlist in allWishlist:
        wishlistCrud.delete_wishlist(db , wishlist)

    return {"message" : "deleted"}
# ------------------------------------------------------------------