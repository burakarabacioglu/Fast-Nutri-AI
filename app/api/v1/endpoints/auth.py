from fastapi import APIRouter

router = APIRouter()

@router.get("/display")
async def display():
    return "Hello World"