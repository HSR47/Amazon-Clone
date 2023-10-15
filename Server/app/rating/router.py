
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.product.models import Product
from app.rating.models import Rating

from app.user.models import User
from app.auth.dependencies import get_current_customer
import app.rating.schemas as ratingSchema

rateRouter = APIRouter(tags=["Rating"])

# ----------------------------RATE A PRODUCT-------------------------
@rateRouter.post("/rating/{id}" , response_model=ratingSchema.returnRating)
def rate_a_product(id:int , data:ratingSchema.ratingRequest , curCustomer:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    rating:Rating = db.query(Rating).filter((Rating.userId==curCustomer.id) & (Rating.productId==id)).first()
    if rating != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="product already rated")

    rating = Rating(
        userId = curCustomer.id,
        productId = id,
        star = data.star,
        comment = data.comment
    )    

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating
# ------------------------------------------------------------------


# ----------------------------UPDATE RATING-------------------------
@rateRouter.put("/rating/{id}" , response_model=ratingSchema.returnRating)
def update_rating(id:int , data:ratingSchema.ratingRequest , curCustomer:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    rating:Rating = db.query(Rating).filter((Rating.userId==curCustomer.id) & (Rating.productId==id)).first()
    if rating == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not rated")

    rating.star = data.star
    rating.comment = data.comment
    
    db.commit()
    db.refresh(rating)

    return rating
# ------------------------------------------------------------------


# ----------------------------REMOVE RATING-------------------------
@rateRouter.delete("/rating/{id}")
def delete_rating(id:int , curCustomer:User = Depends(get_current_customer) , db:Session = Depends(getDb)):

    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    rating:Rating = db.query(Rating).filter((Rating.userId==curCustomer.id) & (Rating.productId==id)).first()
    if rating == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not rated")
    
    db.delete(rating)
    db.commit()

    return {"message" : "removed"}
# ------------------------------------------------------------------