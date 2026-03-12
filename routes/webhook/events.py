from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
)

@router.get("/")
async def root():
    return {"message": "Hello events"}
