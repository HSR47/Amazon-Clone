
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from app.database import getDb
from sqlalchemy.orm.session import Session

import app.category.models as catModel
import app.category.crud as catCrud
import app.category.schemas as catSchema
import app.category.dependecies as catDep
import app.user.models as userModel
import app.auth.dependencies as authDep

prodCatRouter = APIRouter(tags=["Product Category"])


# ----------------------------ADD PRODUCT CATEGORY-------------------------
@prodCatRouter.post("/category" , response_model=catSchema.CategoryReturn)
def add_product_category(
    *,
    data:catSchema.CategoryCreate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    checkCategory = catCrud.get_category_by_name(db , data.name)
    if checkCategory != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="category already exists")

    newCategory = catCrud.create_category(db , data)

    return newCategory
# ------------------------------------------------------------------


# ----------------------------GET ALL PRODUCT CATEGORY-------------------------
@prodCatRouter.get("/category" , response_model=list[catSchema.CategoryReturn])
def get_all_product_category(
    *,
    offset:int = 0,
    limit:int = 100,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    allCategory = catCrud.get_all_categories(db , offset , limit)
    return allCategory
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC PRODUCT CATEGORY-------------------------
@prodCatRouter.get("/category/{category_id}" , response_model=catSchema.CategoryReturn)
def get_specific_product_category(
    *,
    category:Annotated[catModel.ProdCategory , Depends(catDep.valid_category_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
):
    return category
# ------------------------------------------------------------------


# ----------------------------UPDATE PRODUCT CATEGORY-------------------------
@prodCatRouter.patch("/category/{category_id}" , response_model=catSchema.CategoryReturn)
def update_Product_Category(
    *,
    category:Annotated[catModel.ProdCategory , Depends(catDep.valid_category_id)],
    data:catSchema.CategoryUpdate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    if data.name != None and data.name != category.name:
        checkCategory = catCrud.get_category_by_name(db , data.name)
        if checkCategory != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="category already exists")
    
    newCategory = catCrud.update_category(db , category , data)
    
    return newCategory
# ------------------------------------------------------------------


# ----------------------------DELETE PRODUCT CATEGORY-------------------------
@prodCatRouter.delete("/category/{category_id}")
def delete_Product_Category(
    *, 
    category:Annotated[catModel.ProdCategory , Depends(catDep.valid_category_id)], 
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    catCrud.delete_category(db , category)
    
    return {"message" : "deleted"}
# ------------------------------------------------------------------

