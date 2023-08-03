
from fastapi import FastAPI
from app.routers.user import userRouter
from app.routers.auth import authRouter
from app.routers.product import prodRouter
from app.routers.blog import blogRouter
from app.routers.productCategory import prodCatRouter
from app.routers.blogCategory import blogCatRouter
from app.routers.brand import brandRouter
from app.routers.wishlist import wishRouter
from app.routers.rating import rateRouter
from app.routers.coupon import couponRouter
from app.routers.cart import cartRouter

import app.database

app = FastAPI()
app.include_router(userRouter)
app.include_router(authRouter)
app.include_router(prodRouter)
app.include_router(blogRouter)
app.include_router(prodCatRouter)
app.include_router(blogCatRouter)
app.include_router(brandRouter)
app.include_router(wishRouter)
app.include_router(rateRouter)
app.include_router(couponRouter)
app.include_router(cartRouter)

@app.get("/")
def home():
    return {"message" , "Hello World"}