
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime, Uuid
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    star = Column(Integer , nullable=False)
    comment = Column(String)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    product = relationship("Product" , back_populates="ratings")
    user = relationship("User" , back_populates="ratings")