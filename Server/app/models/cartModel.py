
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime, Uuid
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    productId = Column(Integer , ForeignKey("products.id"))

    count = Column(Integer , nullable=False)
    price = Column(Integer , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    user = relationship("User" , back_populates="cartItems")
    product = relationship("Product" , back_populates="cartItems")

    @property
    def disPrice(self):
        if self.user.couponId == None:
            return self.price
        
        result:float = (self.price * (100 - self.user.coupon.discount))/100
        return result.__round__(2)