
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime , event
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.cartModel import CartItem

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False , unique=True)
    expiry = Column(DateTime , nullable=False)
    discount = Column(Integer , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    users = relationship("User" , back_populates="coupon")



def handle_coupon_delete(mapper, connection, target:Coupon):
    for user in target.users:
        user.couponId = None

event.listen(Coupon, "before_delete", handle_coupon_delete)