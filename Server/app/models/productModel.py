
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.ratingModel import Rating


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    slug = Column(String , nullable=False , unique=True)
    description = Column(String , nullable=False)
    price = Column(Integer , nullable=False)
    quantity = Column(Integer , nullable=False)
    sold = Column(Integer , default=0)
    color = Column(String)
    # images
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    ratings = relationship("Rating" , back_populates="product")

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