from fastapi import FastAPI
from routes import base
from routes import data
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from helper.config import get_settings
app=FastAPI()

@asynccontextmanager
async def lifespan(app : FastAPI):
    settings=get_settings()

    app.mongo_conn=AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client=app.mongo_conn[settings.MONGODB_DATABASE]

    yield

    app.mongo_conn.close()

app = FastAPI(lifespan=lifespan)
app.include_router(base.base_router)
app.include_router(data.data_router)



