from fastapi import FastAPI

from src.database import engine
from src.models import Base
from src.router import router

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)
