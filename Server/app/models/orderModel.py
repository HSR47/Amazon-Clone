
from sqlalchemy import Column, Enum, Float, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from enum import Enum as pyEnum

class OrderStatus(pyEnum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "orders"
    
    userId = Column(Integer , ForeignKey("users.id"))

    id = Column(Integer , primary_key=True)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)
    status = Column(Enum(OrderStatus) , nullable=False , default=OrderStatus.pending)


    user = relationship("User" , back_populates="orders")
    orderItems = relationship("OrderItem" , back_populates="order" , cascade="all, delete")

    @property
    def total(self):
        result = 0
        for orderItem in self.orderItems:
            result += orderItem.price
        return int(result)



class OrderItem(Base):
    __tablename__ = "order_items"

    orderId = Column(Integer , ForeignKey("orders.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    count = Column(Integer , nullable=False)
    price = Column(Integer , nullable=False)

    id = Column(Integer , primary_key=True)
    createdAt = Column(DateTime , default=datetime.utcnow)

    order = relationship("Order" , back_populates="orderItems")
    product = relationship("Product" , back_populates="orderItems")
