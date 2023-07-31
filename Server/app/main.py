
from fastapi import FastAPI
from app.routers.user import userRouter
from app.routers.auth import authRouter
from app.routers.product import prodRouter
from app.routers.blog import blogRouter
from app.routers.category import catRouter
from app.routers.brand import brandRouter

import app.database

app = FastAPI()
app.include_router(userRouter)
app.include_router(authRouter)
app.include_router(prodRouter)
app.include_router(blogRouter)
app.include_router(catRouter)
app.include_router(brandRouter)

@app.get("/")
def home():
    return {"message" , "Hello World"}