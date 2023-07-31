
from fastapi import APIRouter , Depends , HTTPException, Query , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.categoryModel import ProdCategory
from app.models.productModel import Product
from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user

import app.schemas.productSchema as productSchema

from slugify import slugify

prodRouter = APIRouter(tags=["Product"])


# ----------------------------ADD PRODUCT-------------------------
@prodRouter.post("/product" , response_model=productSchema.returnProduct)
def addProduct(data:productSchema.addProduct , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    slug = slugify(data.title)

    check = db.query(Product).filter(Product.slug == slug).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    if data.categoryId != None:
        checkCategory = db.query(ProdCategory).filter(ProdCategory.id == data.categoryId).first()
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    newProduct:Product = Product(
        title = data.title,
        slug = slug,
        description = data.description,
        price = data.price,
        quantity = data.quantity,
        sold = data.sold,
        color = data.color,
        brand = data.brand,
        categoryId = data.categoryId
    )

    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)

    return newProduct
# ------------------------------------------------------------------


# ----------------------------GET ALL PRODUCTS-------------------------
@prodRouter.get("/product" , response_model=list[productSchema.returnProduct])
def getAllProducts(color:str=Query(None) , brand:str=Query(None) , category:str=Query(None) , minPrice:int=Query(None) , maxPrice:int=Query(None) , sortBy:str=Query(None) , page:int=Query(1) , limit:int=Query(10) , db:Session = Depends(getDb)):
    
    if sortBy!=None:
        if sortBy not in ["id" , "title" , "price" , "quantity" , "sold" , "brand"]:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY , detail="invalid sort_by column")

    allProducts = db.query(Product)
    if color != None:
        allProducts = allProducts.filter(Product.color == color)

    if brand != None:
        allProducts = allProducts.filter(Product.brand == brand)

    if category != None:
        allProducts = allProducts.filter(Product.category == category)
    
    if minPrice!=None:
        allProducts = allProducts.filter(Product.price >= minPrice)

    if maxPrice!=None:
        allProducts = allProducts.filter(Product.price <= maxPrice)
    
    if sortBy!=None:
        allProducts = allProducts.order_by(getattr(Product , sortBy))
    
    offset = (page-1)*limit
    allProducts = allProducts.offset(offset).limit(limit).all()

    return allProducts
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC PRODUCTS-------------------------
@prodRouter.get("/product/{id}" , response_model=productSchema.returnProduct)
def getSpecificProduct(id:int , db:Session = Depends(getDb)):
    specificProduct = db.query(Product).filter(Product.id == id).first()
    if specificProduct == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    return specificProduct
# ------------------------------------------------------------------


# ----------------------------UPDATE PRODUCT-------------------------
@prodRouter.patch("/product/{id}" , response_model=productSchema.returnProduct)
def updateProduct(id:int , data:productSchema.updateProduct , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    

    slug = None
    if data.title != None:
        slug = slugify(data.title)

        check = db.query(Product).filter(Product.slug == slug).first()
        if check != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    if data.categoryId != None:
        checkCategory = db.query(ProdCategory).filter(ProdCategory.id == data.categoryId).first()
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.title != None:
        product.title = data.title
        product.slug = slug
    
    if data.description != None:
        product.description = data.description
    
    if data.price != None:
        product.price = data.price

    if data.quantity != None:
        product.quantity = data.quantity

    if data.color != None:
        product.color = data.color

    if data.brand != None:
        product.brand = data.brand

    if data.sold != None:
        product.sold = data.sold
    
    if data.categoryId != None:
        product.categoryId = data.categoryId

    db.commit()
    db.refresh(product)

    return product
# ------------------------------------------------------------------


# ----------------------------DELETE PRODUCT-------------------------
@prodRouter.delete("/product/{id}")
def deleteProduct(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    db.delete(product)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------