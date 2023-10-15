
from fastapi import APIRouter , Depends, File , HTTPException, Query, UploadFile , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.brandModel import Brand
from app.models.categoryModel import ProdCategory
from app.models.imageModel import ProductImage
from app.models.productModel import Product
from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user

import app.schemas.productSchema as productSchema

from slugify import slugify

from app.utils.cloudinary import deleteImage, uploadImage

prodRouter = APIRouter(tags=["Product"])


# ----------------------------ADD PRODUCT-------------------------
@prodRouter.post("/product" , response_model=productSchema.returnProduct)
def add_Product(data:productSchema.addProduct , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    slug = slugify(data.title)

    check = db.query(Product).filter(Product.slug == slug).first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    checkCategory = db.query(ProdCategory).filter(ProdCategory.id == data.categoryId).first()
    if checkCategory == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")
        
    checkBrand = db.query(Brand).filter(Brand.id == data.brandId).first()
    if checkBrand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")

    newProduct:Product = Product(
        title = data.title,
        slug = slug,
        description = data.description,
        regularPrice = data.regularPrice,
        discountPrice = data.discountPrice,
        quantity = data.quantity,
        brandId = data.brandId,
        categoryId = data.categoryId
    )

    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)

    return newProduct
# ------------------------------------------------------------------


# ----------------------------GET ALL PRODUCTS-------------------------
@prodRouter.get("/product" , response_model=list[productSchema.returnProduct])
def get_All_Products(brand:str=Query(None) , category:str=Query(None) , minPrice:int=Query(None) , maxPrice:int=Query(None) , sortBy:str=Query(None) , page:int=Query(1) , limit:int=Query(15) , db:Session = Depends(getDb)):
    
    if sortBy!=None:
        if sortBy not in ["id" , "title" , "price" , "quantity" , "sold" , "brand"]:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY , detail="invalid sort_by column")

    allProducts = db.query(Product)

    if brand != None:
        brnd = db.query(Brand).filter(Brand.name.ilike(brand)).first()
        if brnd == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='brand not found')
        allProducts = allProducts.filter(Product.brandId == brnd.id)

    if category != None:
        cat = db.query(ProdCategory).filter(ProdCategory.name==category).first()
        if cat == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='category not found')
        allProducts = allProducts.filter(Product.categoryId == cat.id)
    
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
def get_Specific_Product(id:int , db:Session = Depends(getDb)):
    specificProduct = db.query(Product).filter(Product.id == id).first()
    if specificProduct == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    return specificProduct
# ------------------------------------------------------------------


# ----------------------------UPDATE PRODUCT-------------------------
@prodRouter.patch("/product/{id}")
def update_Product(id:int , data:productSchema.updateProduct , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    slug = product.slug
    if data.title != product.title:
        slug = slugify(data.title)

        check = db.query(Product).filter(Product.slug == slug).first()
        if check != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    if data.categoryId != product.categoryId:
        checkCategory = db.query(ProdCategory).filter(ProdCategory.id == data.categoryId).first()
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.brandId != product.brandId:
        checkBrand = db.query(Brand).filter(Brand.id == data.brandId).first()
        if checkBrand == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")
        

    product.title = data.title
    product.slug = slug
    product.description = data.description
    product.regularPrice = data.regularPrice
    product.discountPrice = data.discountPrice
    product.quantity = data.quantity
    product.brandId = data.brandId
    product.sold = data.sold
    product.categoryId = data.categoryId

    db.commit()

    return {"message" : "updated"}
# ------------------------------------------------------------------


# ----------------------------DELETE PRODUCT-------------------------
@prodRouter.delete("/product/{id}")
def delete_Product(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")
    
    db.delete(product)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------


# ----------------------------ADD IMAGE-------------------------
@prodRouter.post("/product-image/{id}")
def add_image(id:int , images:list[UploadFile] = File(...) , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    product:Product = db.query(Product).filter(Product.id == id).first()
    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="product not found")

    try:
        for img in images:
            url , publicId = uploadImage(img.file)
            
            image = ProductImage(
                productId = id,
                name = img.filename,
                url = url,
                publicId = publicId
            )

            db.add(image)
        
        db.commit()

        return {"message" : "added"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="unexpected error occured")
# ------------------------------------------------------------------


# ----------------------------REMOVE IMAGE-------------------------
@prodRouter.delete("/product-image/{id}")
def remove_image(id:int , curAdmin:User = Depends(get_current_admin) , db:Session = Depends(getDb)):

    image:ProductImage = db.query(ProductImage).filter(ProductImage.id == id).first()
    if image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="image not found")
    
    deleteImage(image.publicId)

    db.delete(image)
    db.commit()

    return {"message" : "removed"}
# ------------------------------------------------------------------