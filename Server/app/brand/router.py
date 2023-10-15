
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.brand.models import Brand

from app.user.models import User
from app.auth.dependencies import get_current_admin, get_current_user
import app.brand.schemas as brandSchema

brandRouter = APIRouter(tags=["Brand"])


# ----------------------------ADD BRAND-------------------------
@brandRouter.post("/brand" , response_model=brandSchema.returnBrand)
def add_Brand(data:brandSchema.addBrandRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    check = db.query(Brand).filter(Brand.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="brand already exists")

    brand = Brand(
        name = data.name,
        image = data.image
    )
    db.add(brand)
    db.commit()
    db.refresh(brand)

    return brand
# ------------------------------------------------------------------


# ----------------------------GET ALL BRAND-------------------------
@brandRouter.get("/brand" , response_model=list[brandSchema.returnBrand])
def get_All_Brand(curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    allBrands = db.query(Brand).all()
    return allBrands
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC BRAND-------------------------
@brandRouter.get("/brand/{id}" , response_model=brandSchema.returnBrand)
def get_Specific_Brand(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    brand = db.query(Brand).filter(Brand.id == id).first()
    if brand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")
    
    return brand
# ------------------------------------------------------------------


# ----------------------------UPDATE BRAND-------------------------
@brandRouter.put("/brand/{id}" , response_model=brandSchema.returnBrand)
def update_Brand(id:int , data:brandSchema.updateBrandRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    brand:Brand = db.query(Brand).filter(Brand.id == id).first()
    if brand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")

    brand.name = data.name
    brand.image = data.image

    db.commit()
    db.refresh(brand)

    return brand
# ------------------------------------------------------------------


# ----------------------------DELETE BRAND-------------------------
@brandRouter.delete("/brand/{id}")
def delete_Brand(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    brand:Brand = db.query(Brand).filter(Brand.id == id).first()
    if brand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")

    db.delete(brand)
    db.commit()
    
    return {"message" : "deleted"}
# ------------------------------------------------------------------

