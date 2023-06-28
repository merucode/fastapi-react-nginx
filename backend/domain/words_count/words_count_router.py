from typing import Union
from fastapi import APIRouter, Depends

from database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession 

from domain.words_count import words_count_crud

router = APIRouter(
    prefix="/words-count",
)

@router.get("/")
async def words_count(db:AsyncSession=Depends(get_async_db), 
        stockCode:Union[str,None]=None, 
        startDate:Union[str,None]=None, 
        stopDate:Union[str,None]=None,
        reqCount:Union[int,None]=None,
        ):
    result = await words_count_crud.get_async_words_count(db, stockCode=stockCode, startDate=startDate, stopDate=stopDate, reqCount=reqCount)
    return result
