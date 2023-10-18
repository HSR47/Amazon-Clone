from sqlalchemy.orm import Session

import app.category.models as catModel
import app.category.schemas as catSchema


# ----------------------------RETRIEVE-------------------------
def get_category_by_id(db:Session , id:int):
    category:catModel.ProdCategory = db.query(catModel.ProdCategory).filter(catModel.ProdCategory.id == id).first()
    return category

def get_category_by_name(db:Session , name:str):
    category:catModel.ProdCategory = db.query(catModel.ProdCategory).filter(catModel.ProdCategory.name == name).first()
    return category

def get_all_categories(db:Session , offset:int = 0 , limit:int = 100):
    allCategories = db.query(catModel.ProdCategory).offset(offset).limit(limit).all()
    return allCategories
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_category(db:Session , data:catSchema.CategoryCreate):
    newCategory = catModel.ProdCategory(
        name = data.name,
        image = data.image
    )

    db.add(newCategory)
    db.commit()
    db.refresh(newCategory)

    return newCategory
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_category(db:Session , category:catModel.ProdCategory , data:catSchema.CategoryUpdate):
    if data.name != None:
        category.name = data.name

    if data.image != None:
        category.image = data.image
    
    db.commit()
    db.refresh(category)

    return category
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_category(db:Session , category:catModel.ProdCategory):
    db.delete(category)
    db.commit()
# ------------------------------------------------------------------