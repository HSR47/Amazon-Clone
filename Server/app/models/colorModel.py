
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime , event
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Color(Base):
    __tablename__ = "colors"

    name = Column(String , nullable=False , unique=True)

    id = Column(Integer , primary_key=True)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    productColors = relationship("ProductColor" , back_populates="color" , cascade="all, delete")




class ProductColor(Base):
    __tablename__ = "product_colors"

    id = Column(Integer , primary_key=True)
    productId = Column(Integer , ForeignKey("products.id"))
    colorId = Column(Integer , ForeignKey("colors.id"))
    createdAt = Column(DateTime , default=datetime.utcnow)

    product = relationship("Product" , back_populates="productColors")
    color = relationship("Color" , back_populates="productColors")