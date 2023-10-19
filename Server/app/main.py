
from fastapi import FastAPI
from app.auth.router import authRouter
from app.user.router import userRouter
from app.scrape.router import scrapeRouter
from app.product.router import prodRouter
from app.image.router import imageRouter
from app.category.router import prodCatRouter
from app.brand.router import brandRouter
from app.wishlist.router import wishRouter
from app.rating.router import rateRouter
from app.cart.router import cartRouter
from app.order.router import orderRouter
from app.address.router import addressRouter

import app.database

app = FastAPI()
app.include_router(authRouter)
app.include_router(userRouter)
app.include_router(prodRouter)
app.include_router(imageRouter)
app.include_router(brandRouter)
app.include_router(prodCatRouter)
app.include_router(wishRouter)
app.include_router(rateRouter)
app.include_router(cartRouter)
# app.include_router(orderRouter)
app.include_router(addressRouter)
# app.include_router(scrapeRouter)
# app.include_router(blogRouter)
# app.include_router(blogCatRouter)
# app.include_router(couponRouter)
# app.include_router(colorRouter)

@app.get("/")
def home():
    return {"message" , "Hello World"}


