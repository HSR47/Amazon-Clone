

from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer , primary_key=True)
    productId = Column(Integer , ForeignKey("products.id"))
    name = Column(String , nullable=False)
    url = Column(String , nullable=False)
    publicId = Column(String , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)

    product = relationship("Product" , back_populates="images")


class BlogImage(Base):
    __tablename__ = "blog_images"

    id = Column(Integer , primary_key=True)
    blogId = Column(Integer , ForeignKey("blogs.id"))
    name = Column(String , nullable=False)
    url = Column(String , nullable=False)
    publicId = Column(String , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)

    blog = relationship("Blog" , back_populates="images")