
from typing import Annotated
from fastapi import APIRouter , Depends , HTTPException , status
from app.database import getDb
from sqlalchemy.orm.session import Session

import app.product.models as prodModel
import app.product.schemas as prodSchema
import app.product.crud as prodCrud
import app.product.dependencies as prodDep
import app.auth.dependencies as authDep
import app.user.models as userModel
import app.category.crud as catCrud
import app.brand.crud as brandCrud


from slugify import slugify



prodRouter = APIRouter(tags=["Product"])


# ----------------------------ADD PRODUCT-------------------------
@prodRouter.post("/product" , response_model=prodSchema.ProductReturn)
def add_Product(
    *,
    data:prodSchema.ProductCreate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    slug = slugify(data.title)
    checkSlug = prodCrud.get_product_by_slug(db=db , slug=slug)
    if checkSlug != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    checkCategory = catCrud.get_category_by_id(db , data.categoryId)
    if checkCategory == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")
        
    checkBrand = brandCrud.get_brand_by_id(db , data.brandId)
    if checkBrand == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")

    newProduct = prodCrud.create_product(db , data)
    return newProduct
# ------------------------------------------------------------------


# ----------------------------GET ALL PRODUCTS-------------------------
@prodRouter.get("/product" , response_model=list[prodSchema.ProductReturn])
def get_All_Products(
    *,
    brandName:str|None = None,
    categoryName:str|None = None,
    minPrice:int|None = None,
    maxPrice:int|None = None,
    sortBy:str|None = None,
    offset:int = 0,
    limit:int = 100,
    db:Annotated[Session , Depends(getDb)]
):
    
    if sortBy!=None:
        if sortBy not in ["title" , "price" , "quantity" , "sold" , "brand"]:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY , detail="invalid sort_by column")

    brand = None
    if brandName != None:
        checkBrand = brandCrud.get_brand_by_name(db , brandName)
        if checkBrand == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='brand not found')
        else:
            brand = checkBrand

    category = None
    if categoryName != None:
        checkCategory = catCrud.get_category_by_name(db , categoryName)
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='category not found')
        else:
            category = checkCategory
    
    allProducts = prodCrud.get_all_products(
        db=db,
        brand=brand,
        category=category,
        minPrice=minPrice,
        maxPrice=maxPrice,
        sortBy=sortBy,
        offset=offset,
        limit=limit
    )

    return allProducts
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC PRODUCTS-------------------------
@prodRouter.get("/product/{id}" , response_model=prodSchema.ProductReturn)
def get_Specific_Product(
    *,
    product:Annotated[prodModel.Product , Depends(prodDep.valid_product_id)],
):
    return product
# ------------------------------------------------------------------


# ----------------------------UPDATE PRODUCT-------------------------
@prodRouter.patch("/product/{id}")
def update_Product(
    *,
    product:Annotated[prodModel.Product , Depends(prodDep.valid_product_id)],
    data:prodSchema.ProductUpdate,
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    if data.title!=None and data.title!=product.title:
        slug = slugify(data.title)

        checkSlug = prodCrud.get_product_by_slug(db , slug)
        if checkSlug != None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="slug already exists")

    if data.categoryId!=None and data.categoryId != product.categoryId:
        checkCategory = catCrud.get_category_by_id(db , data.categoryId)
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.brandId!=None and data.brandId != product.brandId:
        checkBrand = brandCrud.get_brand_by_id(db , data.brandId)
        if checkBrand == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="brand not found")
        
    updatedProduct = prodCrud.update_product(db , product , data)
    return updatedProduct
# ------------------------------------------------------------------


# ----------------------------DELETE PRODUCT-------------------------
@prodRouter.delete("/product/{id}")
def delete_product(
    *,
    product:Annotated[prodModel.Product , Depends(prodDep.valid_product_id)],
    curAdmin:Annotated[userModel.User , Depends(authDep.get_current_admin)],
    db:Annotated[Session , Depends(getDb)]
):
    prodCrud.delete_product(db , product)
    return {"message" : "deleted"}
# ------------------------------------------------------------------


