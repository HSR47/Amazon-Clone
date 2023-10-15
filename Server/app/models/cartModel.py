
from sqlalchemy import Column, ForeignKey , Integer , DateTime, Uuid
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    count = Column(Integer , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    user = relationship("User" , back_populates="cartItems")
    product = relationship("Product" , back_populates="cartItems")
