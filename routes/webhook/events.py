"""
Webhook events routes
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
)

@router.get("/")
async def root():
    """
    Webhook events endpoint
    """

    return {"message": "Hello events"}
