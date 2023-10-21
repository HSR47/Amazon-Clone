
from sqlalchemy import Column, Enum, ForeignKey , Integer, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from enum import Enum as pyEnum


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    status = Column(String , nullable=False , default="pending")
    addressLine1 = Column(String)
    addressLine2 = Column(String)
    postalCode = Column(String , nullable=False)
    country = Column(String , nullable=False)
    state = Column(String , nullable=False)
    city = Column(String , nullable=False)
    mobile = Column(String , nullable=False)
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    user = relationship("User" , back_populates="orders")

    orderItems = relationship("OrderItem" , back_populates="order" , cascade="all, delete")
    payment = relationship("Payment" , back_populates="order" , uselist=False , cascade="all, delete")



class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer , primary_key=True)
    orderId = Column(Integer , ForeignKey("orders.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    count = Column(Integer , nullable=False)
    price = Column(Integer , nullable=False)

    order = relationship("Order" , back_populates="orderItems")
    product = relationship("Product" , back_populates="orderItems")

