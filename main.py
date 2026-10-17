from contextlib import asynccontextmanager
from fastapi import FastAPI

from database.db import engine
from database.models import Base

from routers.user import router as users_router
from routers.task import router as items_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(items_router)
