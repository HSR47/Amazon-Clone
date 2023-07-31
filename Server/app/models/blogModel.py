
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.likeDislikeModel import Like , Dislike

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer , primary_key=True)
    title = Column(String , nullable=False)
    description = Column(String , nullable=False)
    image = Column(String , nullable=False , default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNxBxiKZqG4BAs_d-V7ZVbkLLmDpQWk5zzgb-BOn5QuO7GJjncZpnIFdM7QPz0194eNfI&usqp=CAU")
    views = Column(Integer , default=0)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)


    userId = Column(Integer , ForeignKey("users.id"))
    author = relationship("User" , back_populates="blogs")
    

    categoryId = Column(Integer , ForeignKey("blog_categories.id"))
    category = relationship("BlogCategory" , back_populates="blogs")
    @property
    def categoryName(self):
        if self.categoryId == None:
            return None
        return self.category.name

    
    likes = relationship("Like" , back_populates="blog")
    @property
    def likedBy(self):
        return [like.userId for like in self.likes]
    
    
    dislikes = relationship("Dislike" , back_populates="blog")
    @property
    def dislikedBy(self):
        return [dislike.userId for dislike in self.dislikes]