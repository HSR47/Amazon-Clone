from sqlalchemy.orm import Session
from slugify import slugify

import app.product.models as prodModel
import app.product.schemas as prodSchema
import app.brand.models as brandModel
import app.category.models as catModel

# ----------------------------RETIEVE-------------------------
def get_product_by_id(db:Session , id:int):
    product:prodModel.Product = db.query(prodModel.Product).filter(prodModel.Product.id == id).first()
    return product

def get_product_by_slug(db:Session , slug:str):
    product:prodModel.Product = db.query(prodModel.Product).filter(prodModel.Product.slug == slug).first()
    return product

def get_all_products(
    *,
    db:Session,
    brand:brandModel.Brand|None = None,
    category:catModel.ProdCategory|None = None,
    minPrice:int|None = None,
    maxPrice:int|None = None,
    sortBy:str|None = None,
    offset:int = 0,
    limit:int = 100
):
    allProducts = db.query(prodModel.Product)

    if brand!=None:
        allProducts = allProducts.filter(prodModel.Product.brandId == brand.id)
    
    if category != None:
        allProducts = allProducts.filter(prodModel.Product.categoryId == category.id)
    
    if minPrice != None:
        allProducts = allProducts.filter(prodModel.Product.discountPrice >= minPrice)
    
    if maxPrice != None:
        allProducts = allProducts.filter(prodModel.Product.discountPrice <= maxPrice)

    if sortBy != None:
        allProducts = allProducts.order_by(getattr(prodModel.Product , sortBy))

    allProducts = allProducts.offset(offset).limit(limit).all()
    return allProducts
# ------------------------------------------------------------------


# ----------------------------CREATE-------------------------
def create_product(db:Session , data:prodSchema.ProductCreate):
    newProduct = prodModel.Product(
        title = data.title,
        slug = slugify(data.title),
        description = data.description,
        regularPrice = data.regularPrice,
        discountPrice = data.discountPrice,
        quantity = data.quantity,
        categoryId = data.categoryId,
        brandId = data.brandId
    )

    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)

    return newProduct
# ------------------------------------------------------------------


# ----------------------------UPDATE-------------------------
def update_product(db:Session , product:prodModel.Product , data:prodSchema.ProductUpdate):
    if data.title!=None and data.title!=product.title:
        product.title = data.title
        product.slug = slugify(data.title)
    
    if data.description!=None and data.description!=product.description:
        product.description = data.description
    
    if data.regularPrice!=None and data.regularPrice!=product.regularPrice:
        product.regularPrice = data.regularPrice
    
    if data.discountPrice!=None and data.discountPrice!=product.discountPrice:
        product.discountPrice = data.discountPrice

    if data.quantity!=None and data.quantity!=product.quantity:
        product.quantity = data.quantity

    if data.categoryId!=None and data.categoryId!=product.categoryId:
        product.categoryId = data.categoryId

    if data.brandId!=None and data.brandId!=product.brandId:
        product.brandId = data.brandId

    db.commit()
    db.refresh(product)

    return product
# ------------------------------------------------------------------


# ----------------------------DELETE-------------------------
def delete_product(db:Session , product:prodModel.Product):
    db.delete(product)
    db.commit()
# ------------------------------------------------------------------