from fastapi import FastAPI
from contextlib import asynccontextmanager
from oban import Oban

from routes import health
from routes.webhook import (
    events
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    pool = await Oban.create_pool()
    oban = Oban(pool=pool, queues={"default": 10})

    async with oban:
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(health.router)

app.include_router(events.router, prefix="/webhook")
