
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base
from app.models.blogModel import Blog
from app.models.likeDislikeModel import Like , Dislike
from app.models.wishlistModel import Wishlist
from app.models.ratingModel import Rating
from app.models.cartModel import CartItem

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

    blogs = relationship("Blog" , back_populates="author" , cascade="all, delete")
    likes = relationship("Like" , back_populates="user" , cascade="all, delete")
    dislikes = relationship("Dislike" , back_populates="user" , cascade="all, delete")
    ratings = relationship("Rating" , back_populates="user" , cascade="all, delete")

    wishlists = relationship("Wishlist" , back_populates="user" , cascade="all, delete")
    @property
    def wishlistProducts(self):
        return [wishlist.productId for wishlist in self.wishlists]
    

    cartItems = relationship("CartItem" , back_populates="user" , cascade="all, delete")