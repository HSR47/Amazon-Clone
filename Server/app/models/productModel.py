
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime , event
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    slug = Column(String , nullable=False , unique=True)
    description = Column(String , nullable=False)
    regularPrice = Column(Integer , nullable=False)
    discountPrice = Column(Integer , nullable=False)
    quantity = Column(Integer , nullable=False)
    sold = Column(Integer , default=0)
    categoryId = Column(Integer , ForeignKey("product_categories.id"))
    brandId = Column(Integer , ForeignKey("brands.id"))
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)


    category = relationship("ProdCategory" , back_populates="products")
    brand = relationship("Brand" , back_populates="products")
    

    wishlists = relationship("Wishlist" , back_populates="product" , cascade="all, delete")
    ratings = relationship("Rating" , back_populates="product" , cascade="all, delete")
    images = relationship("ProductImage" , back_populates="product" , cascade="all, delete")
    cartItems = relationship("CartItem" , back_populates="product" , cascade="all, delete")
    orderItems = relationship("OrderItem" , back_populates="product" , cascade="all, delete")

