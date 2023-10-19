
from typing import Annotated, Optional
from pydantic import BaseModel , EmailStr , Field, constr, validator
from datetime import datetime

class ProductCreate(BaseModel):
    title : str = Field(min_length=1)
    description : str = Field(min_length=1)
    regularPrice : int = Field(ge=0)
    discountPrice : int = Field(ge=0)
    quantity : int = Field(ge=0)
    categoryId : int
    brandId : int


class ProductInDB(ProductCreate):
    id : int
    slug : str
    sold : int
    createdAt : datetime
    updatedAt : datetime


class ProductReturn(ProductInDB):
    pass 

    class Config:
        form_attributes = True


class ProductUpdate(ProductCreate):
    title : Annotated[Optional[str] , Field(min_length=1)] = None
    description : Annotated[Optional[str] , Field(min_length=1)] = None
    regularPrice : Annotated[Optional[int] , Field(ge=0)] = None
    discountPrice : Annotated[Optional[int] , Field(ge=0)] = None
    quantity : Annotated[Optional[int] , Field(ge=0)] = None
    categoryId : Optional[int] = None
    brandId : Optional[int] = None


# class addProduct(BaseModel):
#     title : str
#     description : str
#     regularPrice : int
#     discountPrice : int
#     quantity : int
#     brandId : int
#     categoryId : int

#     @validator("title" , "description")
#     def validateStrip(cls , value:str):
#         if value == None:
#             return value
#         return value.strip()

#     @validator("title" , "description")
#     def validateLowerCase(cls , value:str):
#         if value == None:
#             return value
#         return value.lower()
    




# class updateProduct(BaseModel):
#     title : str
#     description : str
#     regularPrice : int
#     discountPrice : int
#     quantity : int
#     sold : int
#     brandId : int
#     categoryId : int

#     @validator("title" , "description")
#     def validateStrip(cls , value:str):
#         if value == None:
#             return value
#         return value.strip()

#     @validator("title" , "description")
#     def validateLowerCase(cls , value:str):
#         if value == None:
#             return value
#         return value.lower()




# class returnImageInProduct(BaseModel):
#     id : int
#     name : str
#     url : str

#     class config:
#         from_attributes = True
        

# class returnProduct(BaseModel):
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
    
#     images : list[returnImageInProduct]

#     # ratings : list
#     # brandName : str | None
#     # categoryName : str | None
#     # ratings : list[returnRating]
#     # avgRating : float

#     class config:
#         from_attributes = True







# # class returnProduct2(BaseModel):
# #     id : int
# #     title : str
# #     slug : str
# #     description : str
# #     regularPrice : int
# #     discountPrice : int
# #     quantity : int
# #     sold : int | None
# #     createdAt : datetime
# #     updatedAt : datetime

# #     category: ProdCategory
# #     brand: Brand
# #     wishlists: List[Wishlist]
# #     ratings: List[Rating]
# #     images: List[ProductImage]
# #     cartItems: List[CartItem]
# #     orderItems: List[OrderItem]

# #     class config:
# #         from_attributes = True