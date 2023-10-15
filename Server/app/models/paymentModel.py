
from sqlalchemy import Column, Enum, Float, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from enum import Enum as pyEnum


class PaymentMethod(pyEnum):
    cod = "cod"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer , primary_key=True)
    orderId = Column(Integer , ForeignKey("orders.id") , nullable=False)
    method = Column(Enum(PaymentMethod) , default=PaymentMethod.cod , nullable=False) 
    createdAt = Column(DateTime , default=datetime.utcnow)

    order = relationship("Order" , back_populates="payment")