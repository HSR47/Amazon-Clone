
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.blogModel import Blog
from app.models.categoryModel import BlogCategory

from app.models.userModel import User
from app.routers.auth import get_current_admin
import app.schemas.categorySchema as categorySchema

blogCatRouter = APIRouter(tags=["Blog Category"])


# ----------------------------ADD BLOG CATEGORY-------------------------
@blogCatRouter.post("/category/blog" , response_model=categorySchema.returnCategory)
def add_Blog_Category(data:categorySchema.addCategoryRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    check = db.query(BlogCategory).filter(BlogCategory.name == data.name).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="category already exists")

    category = BlogCategory(
        name = data.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)

    return category
# ------------------------------------------------------------------


# ----------------------------GET ALL BLOG CATEGORY-------------------------
@blogCatRouter.get("/category/blog" , response_model=list[categorySchema.returnCategory])
def get_All_Blog_Category(curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    allCategory = db.query(BlogCategory).all()
    return allCategory
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC BLOG CATEGORY-------------------------
@blogCatRouter.get("/category/blog/{id}" , response_model=categorySchema.returnCategory)
def get_Specific_Blog_Category(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):
    category = db.query(BlogCategory).filter(BlogCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")
    
    return category
# ------------------------------------------------------------------


# ----------------------------UPDATE BLOG CATEGORY-------------------------
@blogCatRouter.patch("/category/blog/{id}" , response_model=categorySchema.returnCategory)
def update_Blog_Category(id:int , data:categorySchema.updateCategoryRequest , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    category:BlogCategory = db.query(BlogCategory).filter(BlogCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.name != None:
        category.name = data.name
        db.commit()
        db.refresh(category)

    return category
# ------------------------------------------------------------------


# ----------------------------DELETE BLOG CATEGORY-------------------------
@blogCatRouter.delete("/category/blog/{id}")
def delete_Blog_Category(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    category:BlogCategory = db.query(BlogCategory).filter(BlogCategory.id == id).first()
    if category == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    db.delete(category)
    db.commit()
    
    return {"message" : "deleted"}
# ------------------------------------------------------------------