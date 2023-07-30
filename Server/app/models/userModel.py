
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    role = Column(String , nullable=False)
    fname = Column(String , nullable=False)
    lname = Column(String , nullable=False)
    email = Column(String , nullable=False , unique=True)
    mobile = Column(String , nullable=False , unique=True)
    password = Column(String , nullable=False)
    blocked = Column(Boolean , nullable=False , default=False)
    refreshToken = Column(String)
    passResetToken = Column(String)
    passResetTokenExp = Column(DateTime)
    createdAt = Column(DateTime , nullable=False , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    blogs = relationship("Blog" , back_populates="author")