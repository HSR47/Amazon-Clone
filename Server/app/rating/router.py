
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from app.database import getDb

import app.rating.models as ratingModel
import app.rating.schemas as ratingSchema
import app.rating.crud as ratingCrud
import app.product.models as productModel
import app.auth.dependencies as authDep
import app.user.models as userModel
import app.product.dependencies as prodDep
import app.rating.dependencies as ratingDep

rateRouter = APIRouter(tags=["Rating"])


# ----------------------------GET SPECIFIC RATING-------------------------
@rateRouter.get("/user/me/rating/{rating_id}" , response_model=ratingSchema.RatingReturn)
def get_specific_rating(
    *,
    rating:Annotated[ratingModel.Rating , Depends(ratingDep.valid_rating_id)],
    curCustomer:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if rating.userId != curCustomer.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    return rating
# ------------------------------------------------------------------


# ----------------------------GET ALL CUSTOMER RATINGS-------------------------
@rateRouter.get("/user/me/rating" , response_model=list[ratingSchema.RatingReturn])
def get_all_ratings(
    *,
    curCustomer:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    ratings = ratingCrud.get_all_ratings_by_user_id(db , curCustomer.id)
    return ratings
# ------------------------------------------------------------------


# ----------------------------RATE A PRODUCT-------------------------
@rateRouter.post("/user/me/product/{product_id}/rating" , response_model=ratingSchema.RatingReturn)
def rate_a_product(
    *,
    product:Annotated[productModel.Product , Depends(prodDep.valid_product_id)],
    data:ratingSchema.RatingCreate,
    curCustomer:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    checkRating = ratingCrud.get_rating_by_user_id_and_product_id(db , curCustomer.id , product.id)
    if checkRating != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="already rated")

    rating = ratingCrud.create_rating(db , curCustomer.id , product.id , data)
    return rating
# ------------------------------------------------------------------


# ----------------------------UPDATE RATING-------------------------
@rateRouter.put("/user/me/rating/{rating_id}" , response_model=ratingSchema.RatingReturn)
def update_rating(
    *,
    rating:Annotated[ratingModel.Rating , Depends(ratingDep.valid_rating_id)],
    data:ratingSchema.RatingUpdate,
    curCustomer:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if rating.userId != curCustomer.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    updatedRating = ratingCrud.update_rating(db , rating , data)
    return updatedRating
# ------------------------------------------------------------------


# ----------------------------REMOVE RATING-------------------------
@rateRouter.delete("/user/me/rating/{rating_id}")
def delete_rating(
    *,
    rating:Annotated[ratingModel.Rating , Depends(ratingDep.valid_rating_id)],
    curCustomer:Annotated[userModel.User , Depends(authDep.get_current_customer)],
    db:Annotated[Session , Depends(getDb)]
):
    if rating.userId != curCustomer.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="forbidden")
    
    ratingCrud.delete_rating(db , rating)
    return {"message" : "deleted"}
# ------------------------------------------------------------------