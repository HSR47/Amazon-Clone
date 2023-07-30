

from sqlalchemy import Column, ForeignKey , Integer, PrimaryKeyConstraint , String , Boolean , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models import Base


class Rating(Base):
    __tablename__ = "ratings"

    userId = Column(Integer , ForeignKey("users.id"))
    productId = Column(Integer , ForeignKey("products.id"))
    stars = Column(Integer , nullable=False)

    product = relationship("Product" , back_populates="ratings")

    __table_args__ = (
        PrimaryKeyConstraint("userId" , "productId"),
    )