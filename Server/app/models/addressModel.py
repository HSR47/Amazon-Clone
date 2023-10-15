
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Address(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    addressLine1 = Column(String)
    addressLine2 = Column(String)
    postalCode = Column(String , nullable=False)
    country = Column(String , nullable=False)
    state = Column(String , nullable=False)
    city = Column(String , nullable=False)
    mobile = Column(String , nullable=False)
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    user = relationship("User" , back_populates="address")