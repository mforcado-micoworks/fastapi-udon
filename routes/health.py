"""
Health check routes
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
)

@router.get("/")
async def root():
    """
    Health check endpoint
    """

    return {"message": "ok"}
