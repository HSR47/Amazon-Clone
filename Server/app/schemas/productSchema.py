
from typing import List, Optional
from pydantic import BaseModel , EmailStr , Field, validator
from datetime import datetime
from app.models.brandModel import Brand
from app.models.cartModel import CartItem
from app.models.categoryModel import ProdCategory
from app.models.imageModel import ProductImage
from app.models.orderModel import OrderItem
from app.models.ratingModel import Rating
from app.models.wishlistModel import Wishlist

from app.schemas.ratingSchema import returnRating


class addProduct(BaseModel):
    title : str
    description : str
    regularPrice : int
    discountPrice : int
    quantity : int
    brandId : int
    categoryId : int

    @validator("title" , "description")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()
    




class updateProduct(BaseModel):
    title : str
    description : str
    regularPrice : int
    discountPrice : int
    quantity : int
    sold : int
    brandId : int
    categoryId : int

    @validator("title" , "description")
    def validateStrip(cls , value:str):
        if value == None:
            return value
        return value.strip()

    @validator("title" , "description")
    def validateLowerCase(cls , value:str):
        if value == None:
            return value
        return value.lower()




class returnImageInProduct(BaseModel):
    id : int
    name : str
    url : str

    class config:
        from_attributes = True
        

class returnProduct(BaseModel):
    id : int
    title : str
    slug : str
    description : str
    regularPrice : int
    discountPrice : int
    quantity : int
    sold : int | None
    createdAt : datetime
    updatedAt : datetime
    
    images : list[returnImageInProduct]

    # ratings : list
    # brandName : str | None
    # categoryName : str | None
    # ratings : list[returnRating]
    # avgRating : float

    class config:
        from_attributes = True







# class returnProduct2(BaseModel):
#     id : int
#     title : str
#     slug : str
#     description : str
#     regularPrice : int
#     discountPrice : int
#     quantity : int
#     sold : int | None
#     createdAt : datetime
#     updatedAt : datetime

#     category: ProdCategory
#     brand: Brand
#     wishlists: List[Wishlist]
#     ratings: List[Rating]
#     images: List[ProductImage]
#     cartItems: List[CartItem]
#     orderItems: List[OrderItem]

#     class config:
#         from_attributes = True