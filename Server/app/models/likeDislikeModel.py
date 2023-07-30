
from sqlalchemy import Column, ForeignKey , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    blogId = Column(Integer , ForeignKey("blogs.id"))

    user = relationship("User" , back_populates="likes")
    blog = relationship("Blog" , back_populates="likes")


class Dislike(Base):
    __tablename__ = "dislikes"

    id = Column(Integer , primary_key=True)
    userId = Column(Integer , ForeignKey("users.id"))
    blogId = Column(Integer , ForeignKey("blogs.id"))

    user = relationship("User" , back_populates="dislikes")
    blog = relationship("Blog" , back_populates="dislikes")