from fastapi import APIRouter, Depends

from database import get_async_db # Async
from sqlalchemy.ext.asyncio import AsyncSession # Async

from domain.test import test_crud

router = APIRouter(
    prefix="/test",
)

@router.get("/")
async def test_get_data(db:AsyncSession=Depends(get_async_db)):
    result = await test_crud.get_data(db)
    return result
