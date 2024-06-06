from fastapi import FastAPI

from src.database import engine
from src.models import Base

app = FastAPI()

@app.get("/orders")
async def get_all_orders():
    return


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


