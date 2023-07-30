
from fastapi import APIRouter , Depends , HTTPException , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.blogModel import Blog

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user
import app.schemas.blogSchema as blogSchema
import app.schemas.userSchema as userSchema
import app.utils.passlib as passlib

blogRouter = APIRouter(tags=["Blog"])


# ----------------------------CREATE BLOG-------------------------
@blogRouter.post("/blog")
def createBlog(data:blogSchema.createBlogRequest , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog = Blog(
        userId = curUser.id,
        title = data.title,
        description = data.description,
        category = data.category,
        views = data.views,
        isLiked = data.isLiked,
        isDisliked = data.isDisliked,
        image = data.image
    )
# ------------------------------------------------------------------