
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.blogModel import Blog
from app.models.categoryModel import BlogCategory, ProdCategory

from app.models.userModel import User
from app.routers.auth import get_current_admin
import app.schemas.categorySchema as categorySchema

prodCatRouter = APIRouter(tags=["Product Category"])


# ----------------------------ADD PRODUCT CATEGORY-------------------------
@prodCatRouter.post("/category/product" , response_model=categorySchema.returnCategory)
def addProductCategory(data:categorySchema.addCategoryRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    check = db.query(ProdCategory).filter(ProdCategory.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="category already exists")

    category = ProdCategory(
        name = data.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)

    return category
# ------------------------------------------------------------------


# ----------------------------GET ALL PRODUCT CATEGORY-------------------------
@prodCatRouter.get("/category/product" , response_model=list[categorySchema.returnCategory])
def getAllProductCategory(curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    allCategory = db.query(ProdCategory).all()
    return allCategory
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC PRODUCT CATEGORY-------------------------
@prodCatRouter.get("/category/product/{id}" , response_model=categorySchema.returnCategory)
def getSpecificProductCategory(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    category = db.query(ProdCategory).filter(ProdCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")
    
    return category
# ------------------------------------------------------------------


# ----------------------------UPDATE PRODUCT CATEGORY-------------------------
@prodCatRouter.patch("/category/product/{id}" , response_model=categorySchema.returnCategory)
def updateProductCategory(id:int , data:categorySchema.updateCategoryRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    category:ProdCategory = db.query(ProdCategory).filter(ProdCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.name != None:
        category.name = data.name
        db.commit()
        db.refresh(category)

    return category
# ------------------------------------------------------------------


# ----------------------------DELETE PRODUCT CATEGORY-------------------------
@prodCatRouter.delete("/category/product/{id}")
def deleteProductCategory(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    category:ProdCategory = db.query(ProdCategory).filter(ProdCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    db.delete(category)
    db.commit()
    
    return {"message" : "deleted"}
# ------------------------------------------------------------------
