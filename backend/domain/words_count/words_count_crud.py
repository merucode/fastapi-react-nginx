from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.responses import JSONResponse

from models import WordsCount
from domain.words_count.words_count_util import common_words_count, make_response_data, fill_null_data

async def get_async_words_count(db: AsyncSession, stockCode, startDate, stopDate, reqCount):
    data = await db.execute(select(WordsCount).
            filter(WordsCount.code==stockCode).
            filter(WordsCount.date.between(startDate, stopDate)))
    load_data = data.scalars().fetchall()   # Load data from PG
    
    
    # Extract commom word and count as much as reqCount
    common_words_count_lst = common_words_count(load_data, reqCount)

    # Make response list of dict fom json data only containing common words 
    response_dict_lst, db_date_lst  = make_response_data(load_data, common_words_count_lst)
    
	# Fill data of null date
    response_dict_lst = fill_null_data(response_dict_lst, db_date_lst, common_words_count_lst, startDate, stopDate)

    return JSONResponse(content={"data":response_dict_lst, "comWords":common_words_count_lst})

