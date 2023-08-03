
from fastapi import APIRouter , Depends, File , HTTPException, UploadFile , status

from app.database import getDb
from sqlalchemy.orm.session import Session
from app.models.blogModel import Blog
from app.models.categoryModel import BlogCategory
from app.models.imageModel import BlogImage
from app.models.likeDislikeModel import Dislike, Like

from app.models.userModel import User
from app.routers.auth import get_current_admin, get_current_user
import app.schemas.blogSchema as blogSchema
from app.utils.cloudinary import deleteImage, uploadImage

blogRouter = APIRouter(tags=["Blog"])


# ----------------------------CREATE BLOG-------------------------
@blogRouter.post("/blog" , response_model=blogSchema.returnBlog)
def createBlog(data:blogSchema.createBlogRequest , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    if data.categoryId != None:
        checkCategory = db.query(BlogCategory).filter(BlogCategory.id == data.categoryId).first()
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    blog = Blog(
        userId = curUser.id,
        title = data.title,
        description = data.description,
        categoryId = data.categoryId
    )

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog
# ------------------------------------------------------------------


# ----------------------------GET ALL BLOGS-------------------------
@blogRouter.get("/blog" , response_model=list[blogSchema.returnBlog])
def getAllBlogs(curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):
    allBlogs = db.query(Blog).all()
    return allBlogs
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC BLOG-------------------------
@blogRouter.get("/blog/{id}" , response_model=blogSchema.returnBlog)
def getSpecificBlog(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")
    
    blog.views += 1
    db.commit()
    
    return blog
# ------------------------------------------------------------------


# ----------------------------UPDATE BLOG-------------------------
@blogRouter.patch("/blog/{id}" , response_model=blogSchema.returnBlog)
def updateBlog(id:int , data:blogSchema.updateBlogRequest , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")

    if blog.userId != curUser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not allowed")

    if data.categoryId != None:
        checkCategory = db.query(BlogCategory).filter(BlogCategory.id == data.categoryId).first()
        if checkCategory == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="category not found")

    if data.title != None:
        blog.title = data.title
    if data.description != None:
        blog.description = data.description
    if data.categoryId != None:
        blog.category = data.categoryId
    
    db.commit()
    db.refresh(blog)

    return blog
# ------------------------------------------------------------------


# ----------------------------DELETE BLOG-------------------------
@blogRouter.delete("/blog/{id}")
def deleteBlog(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")

    if blog.userId != curUser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not allowed")
    
    db.delete(blog)
    db.commit()

    return {"message" : "deleted"}
# ------------------------------------------------------------------


# ----------------------------LIKE A BLOG-------------------------
@blogRouter.put("/blog/like/{id}")
def likeABlog(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")


    Liked = db.query(Like).filter((Like.userId == curUser.id) & (Like.blogId == blog.id)).first()

    if Liked:
        db.delete(Liked)
        db.commit()

        return {"message" : "removed like"}

    elif not Liked:
        Disliked = db.query(Dislike).filter((Dislike.userId == curUser.id) & (Dislike.blogId == blog.id)).first()
        if Disliked:
            db.delete(Disliked)
            db.commit()
        
        like = Like(
            userId = curUser.id,
            blogId = blog.id
        )

        db.add(like)
        db.commit()

        return {"message" : "liked"}
# ------------------------------------------------------------------


# ----------------------------DISLIKE A BLOG-------------------------
@blogRouter.put("/blog/dislike/{id}")
def dislikeABlog(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")


    Disliked = db.query(Dislike).filter((Dislike.userId == curUser.id) & (Dislike.blogId == blog.id)).first()

    if Disliked:
        db.delete(Disliked)
        db.commit()

        return {"message" : "removed dislike"}

    elif not Disliked:
        Liked = db.query(Like).filter((Like.userId == curUser.id) & (Like.blogId == blog.id)).first()
        if Liked:
            db.delete(Liked)
            db.commit()
        
        dislike = Dislike(
            userId = curUser.id,
            blogId = blog.id
        )

        db.add(dislike)
        db.commit()

        return {"message" : "disliked"}
# ------------------------------------------------------------------


# ----------------------------ADD IMAGE-------------------------
@blogRouter.post("/blog-image/{id}")
def add_image(id:int , images:list[UploadFile] = File(...) , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    blog:Blog = db.query(Blog).filter(Blog.id == id).first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="blog not found")

    if blog.userId != curUser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not allowed")

    try:
        for img in images:
            url , publicId = uploadImage(img.file)
            
            image = BlogImage(
                blogId = id,
                name = img.filename,
                url = url,
                publicId = publicId
            )

            db.add(image)
        
        db.commit()

        return {"message" : "added"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail="unexpected error occured")
# ------------------------------------------------------------------


# ----------------------------REMOVE IMAGE-------------------------
@blogRouter.delete("/blog-image/{id}")
def remove_image(id:int , curUser:User = Depends(get_current_user) , db:Session = Depends(getDb)):

    image:BlogImage = db.query(BlogImage).filter(BlogImage.id == id).first()
    if image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="image not found")
    
    if image.blog.userId != curUser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not allowed")

    deleteImage(image.publicId)

    db.delete(image)
    db.commit()

    return {"message" : "removed"}
# ------------------------------------------------------------------