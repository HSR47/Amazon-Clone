from sqlalchemy.orm import Session

import app.brand.models as brandModel
import app.brand.schemas as brandSchema


# ----------------------------RETRIEVE-------------------------
def get_brand_by_id(db:Session , id:int):
    brand:brandModel.Brand = db.query(brandModel.Brand).filter(brandModel.Brand.id == id).first()
    return brand

def get_brand_by_name(db:Session , name:str):
    brand:brandModel.Brand = db.query(brandModel.Brand).filter(brandModel.Brand.name == name).first()
    return brand

def get_all_brands(db:Session , offset:int = 0 , limit:int = 100):
    allBrands = db.query(brandModel.Brand).offset(offset).limit(limit).all()
    return allBrands
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_brand(db:Session , data:brandSchema.BrandCreate):
    newBrand = brandModel.Brand(
        name = data.name,
        image = data.image
    )

    db.add(newBrand)
    db.commit()
    db.refresh(newBrand)

    return newBrand
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_brand(db:Session , brand:brandModel.Brand , data:brandSchema.BrandUpdate):
    if data.name != None:
        brand.name = data.name

    if data.image != None:
        brand.image = data.image
    
    db.commit()
    db.refresh(brand)

    return brand
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_brand(db:Session , brand:brandModel.Brand):
    db.delete(brand)
    db.commit()
# ------------------------------------------------------------------