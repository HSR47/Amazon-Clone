
from turtle import back
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime , event
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.ratingModel import Rating
from app.models.wishlistModel import Wishlist
from app.models.ratingModel import Rating
from app.models.imageModel import ProductImage
from app.models.cartModel import CartItem
from app.models.orderModel import OrderItem
from app.models.colorModel import ProductColor

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    slug = Column(String , nullable=False , unique=True)
    description = Column(String , nullable=False)
    price = Column(Integer , nullable=False)
    quantity = Column(Integer , nullable=False)
    sold = Column(Integer , default=0)
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    productColors = relationship("ProductColor" , back_populates="product" , cascade="all, delete")
    @property
    def colors(self):
        result = []
        for productColor in self.productColors:
            result.append({
                "id" : productColor.color.id,
                "name" : productColor.color.name
            })

        return result

    brandId = Column(Integer , ForeignKey("brands.id"))
    brand = relationship("Brand" , back_populates="products")
    @property
    def brandName(self):
        if self.brand == None:
            return None
        return self.brand.name

    categoryId = Column(Integer , ForeignKey("product_categories.id"))
    category = relationship("ProdCategory" , back_populates="products")
    @property
    def categoryName(self):
        if self.categoryId == None:
            return None
        return self.category.name
    
    wishlists = relationship("Wishlist" , back_populates="product" , cascade="all, delete")

    ratings = relationship("Rating" , back_populates="product" , cascade="all, delete")
    @property
    def avgRating(self):
        allStars = [rating.star for rating in self.ratings]
        if allStars == []:
            return 0
        result:float = sum(allStars)/len(allStars)
        result = result.__round__(1)
        return result
    

    images = relationship("ProductImage" , back_populates="product" , cascade="all, delete")

    cartItems = relationship("CartItem" , back_populates="product" , cascade="all, delete")
    orderItems = relationship("OrderItem" , back_populates="product" , cascade="all, delete")



def updateCartItemPrice(target:Product , value:int , oldValue:int , initiator):
    for cartItem in target.cartItems:
        cartItem.price = value


event.listen(Product.price , "set" , updateCartItemPrice)