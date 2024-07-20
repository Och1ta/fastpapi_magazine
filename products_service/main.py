from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.router import router as product_router

app = FastAPI()

app.include_router(product_router, prefix="/products")

Base.metadata.create_all(bind=engine)
