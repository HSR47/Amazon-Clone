
from fastapi import FastAPI
from app.routers.user import userRouter
from app.routers.auth import authRouter
from app.routers.product import prodRouter
import app.database

app = FastAPI()
app.include_router(userRouter)
app.include_router(authRouter)
app.include_router(prodRouter)

@app.get("/")
def home():
    return {"message" , "Hello World"}