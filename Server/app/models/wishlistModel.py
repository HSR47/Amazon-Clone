
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    createdAt = Column(DateTime , default=datetime.utcnow)

    user = relationship("User" , back_populates="wishlists")
    product = relationship("Product" , back_populates="wishlists")