
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from app.database import getDb
from sqlalchemy.orm.session import Session

import app.brand.models as brandModel
import app.brand.schemas as brandSchema
import app.brand.crud as brandCrud
import app.brand.dependecies as brandDep
import app.user.models as userModel
import app.auth.dependencies as authDep


brandRouter = APIRouter(tags=["Brand"])


# ----------------------------ADD BRAND-------------------------
@brandRouter.post("/brand" , response_model=brandSchema.BrandReturn)
def add_Brand(
    *,
    data:brandSchema.BrandCreate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    checkBrand = brandCrud.get_brand_by_name(db , data.name)
    if checkBrand != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="brand already exists")

    newBrand = brandCrud.create_brand(db , data)

    return newBrand
# ------------------------------------------------------------------


# ----------------------------GET ALL BRAND-------------------------
@brandRouter.get("/brand" , response_model=list[brandSchema.BrandReturn])
def get_all_brand(
    *,
    offset:int = 0,
    limit:int = 100,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    allBrands = brandCrud.get_all_brands(db , offset , limit)
    return allBrands
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC BRAND-------------------------
@brandRouter.get("/brand/{brand_id}" , response_model=brandSchema.BrandReturn)
def get_specific_brand(
    *,
    brand:Annotated[brandModel.Brand , Depends(brandDep.valid_brand_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
):
    return brand
# ------------------------------------------------------------------


# ----------------------------UPDATE BRAND-------------------------
@brandRouter.put("/brand/{brand_id}" , response_model=brandSchema.BrandReturn)
def update_Brand(
    *,
    brand:Annotated[brandModel.Brand , Depends(brandDep.valid_brand_id)],
    data:brandSchema.BrandUpdate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    if data.name != None and data.name != brand.name:
        checkBrand = brandCrud.get_brand_by_name(db , data.name)
        if checkBrand != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="brand already exists")
        
    newBrand = brandCrud.update_brand(db , brand , data)

    return newBrand
# ------------------------------------------------------------------


# ----------------------------DELETE BRAND-------------------------
@brandRouter.delete("/brand/{brand_id}")
def delete_Brand(
    *,
    brand:Annotated[brandModel.Brand , Depends(brandDep.valid_brand_id)], 
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    brandCrud.delete_brand(db , brand)
    
    return {"message" : "deleted"}
# ------------------------------------------------------------------

