
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.brandModel import Brand
from app.models.couponModel import Coupon

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_customer, get_current_user
import app.schemas.couponSchema as couponSchema

couponRouter = APIRouter(tags=["Coupon"])

# ----------------------------CREATE COUPON-------------------------
@couponRouter.post("/coupon" , response_model=couponSchema.returnCoupon)
def create_coupon(data:couponSchema.createCouponRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    check = db.query(Coupon).filter(Coupon.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="coupon already exists")

    coupon = Coupon(
        name = data.name,
        discount = data.discount,
        expiry = data.expiry
    )

    db.add(coupon)
    db.commit()
    db.refresh(coupon)

    return coupon
# ------------------------------------------------------------------


# ----------------------------GET ALL COUPONS-------------------------
@couponRouter.get("/coupon" , response_model=list[couponSchema.returnCoupon])
def get_all_coupons(curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    allCoupons = db.query(Coupon).all()
    return allCoupons
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC COUPON-------------------------
@couponRouter.get("/coupon/{id}" , response_model=couponSchema.returnCoupon)
def create_coupon(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    coupon = db.query(Coupon).filter(Coupon.id == id).first()
    if coupon == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="coupon not found")
    
    return coupon
# ------------------------------------------------------------------


# ----------------------------UPDATE COUPON-------------------------
@couponRouter.patch("/coupon/{id}" , response_model=couponSchema.returnCoupon)
def update_coupon(id:int , data:couponSchema.updateCoupon , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    coupon:Coupon = db.query(Coupon).filter(Coupon.id == id).first()
    if coupon == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="coupon not found")

    if data.name != None:
        coupon.name = data.name
    if data.discount != None:
        coupon.discount = data.discount
    if data.expiry != None:
        coupon.expiry = data.expiry

    db.commit()
    db.refresh(coupon)

    return coupon  
# ------------------------------------------------------------------


# ----------------------------DELETE COUPON-------------------------
@couponRouter.delete("/coupon/{id}")
def delete_coupon(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    coupon:Coupon = db.query(Coupon).filter(Coupon.id == id).first()
    if coupon == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="coupon not found")
    
    db.delete(coupon)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------
