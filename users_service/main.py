import asyncio
from fastapi import FastAPI
from src.database import init_db
from src.router import router


app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == "__main__":
    asyncio.run(app.main())
