
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False , unique=True)
    expiry = Column(DateTime , nullable=False)
    discount = Column(Integer , nullable=False)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)