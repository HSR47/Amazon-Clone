
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.userModel import User

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    title = Column(String , nullable=False)
    description = Column(String , nullable=False)
    category = Column(String , nullable=False)
    views = Column(Integer , default=0)
    isLiked = Column(Boolean , default=False)
    isDisliked = Column(Boolean , default=False)
    image = Column(String , default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNxBxiKZqG4BAs_d-V7ZVbkLLmDpQWk5zzgb-BOn5QuO7GJjncZpnIFdM7QPz0194eNfI&usqp=CAU")
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)

    author = relationship("User" , back_populates="blogs")