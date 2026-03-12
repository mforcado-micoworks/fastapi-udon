"""
Webhook events routes
"""

from fastapi import APIRouter
from oban_workers.send_email import send_email

router = APIRouter(
    prefix="/events",
)

@router.get("/")
async def root():
    """
    Webhook events endpoint
    """

    await send_email.enqueue("test@email.com")

    return {"message": "Hello events"}
