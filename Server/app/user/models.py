
from sqlalchemy import Column , Integer , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    email = Column(String , nullable=False , unique=True)
    hashed_password = Column(String , nullable=False)
    fname = Column(String , nullable=False)
    lname = Column(String , nullable=False)
    mobile = Column(String , nullable=False , unique=True)
    is_admin = Column(Boolean , nullable=False)

    refresh_token = Column(String)
    pass_reset_token = Column(String)
    pass_reset_token_exp = Column(DateTime)
    created_at = Column(DateTime , nullable=False , default=datetime.utcnow)
    updated_at = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)


    address = relationship("Address" , back_populates="user" , cascade="all, delete")
    ratings = relationship("Rating" , back_populates="user" , cascade="all, delete")
    orders = relationship("Order" , back_populates="user" , cascade="all, delete")
    wishlists = relationship("Wishlist" , back_populates="user" , cascade="all, delete")
    cartItems = relationship("CartItem" , back_populates="user" , cascade="all, delete")
    