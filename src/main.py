from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import engine
from database.models import Base
from handlers.task import router as tasks_router
from handlers.task_user import router as task_user_router
from handlers.user import router as users_router

import logging.config
from logger import LoggerConf


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        logging.config.dictConfig(LoggerConf().model_dump())

    yield

    await engine.dispose()

logger = logging.getLogger("task_manager")
app = FastAPI(lifespan=lifespan)

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(tasks_router)
app.include_router(task_user_router)

@app.get("/")
def main_page():
    return {"status": "ok"}