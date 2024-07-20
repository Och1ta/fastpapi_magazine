from fastapi import FastAPI

from app.router import router as user_router


app = FastAPI()

app.include_router(user_router, prefix="/user")
