from fastapi import FastAPI

from routes import health
from routes.webhook import (
    events
)

app = FastAPI()

app.include_router(health.router)

app.include_router(events.router, prefix="/webhook")
