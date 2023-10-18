

from sqlalchemy import Column, Integer , String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False , unique=True)
    image = Column(String)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    products = relationship("Product" , back_populates="brand" , cascade="all, delete")
