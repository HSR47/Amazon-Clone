

from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime , event
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class Color(Base):
    __tablename__ = "colors"
    
    name = Column(String , nullable=False , unique=True)

    id = Column(Integer , primary_key=True)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)