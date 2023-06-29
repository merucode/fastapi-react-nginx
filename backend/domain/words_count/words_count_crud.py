from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.responses import JSONResponse
import pandas as pd

from models import WordsCount, StockOHLCV, IndexOHLCV
from domain.words_count.words_count_util import common_words_count, make_response_data, fill_null_data
from domain.words_count.stock_index_util import convert_to_dataframe, fill_null_data_stock_index, merge_list_df

async def get_async_words_count(db: AsyncSession, stockCode, startDate, stopDate, reqCount):
    data_words_count = await db.execute(select(WordsCount).
            filter(WordsCount.code==stockCode).
            filter(WordsCount.date.between(startDate, stopDate)))
    load_data_words_count = data_words_count.scalars().fetchall()   # Load data from PG
    
    data_stock_ohlcv = await db.execute(select(StockOHLCV).
            filter(StockOHLCV.code==stockCode).
            filter(StockOHLCV.date.between(startDate, stopDate)))
    load_data_stock_ohlcv = data_stock_ohlcv.scalars().fetchall()
    df_stock = convert_to_dataframe(load_data_stock_ohlcv, ['date', 'close'], stockCode)
    
    data_index_ohlcv = await db.execute(select(IndexOHLCV).
            filter(IndexOHLCV.code=="KOSPI").
            filter(IndexOHLCV.date.between(startDate, stopDate)))
    load_data_index_ohlcv = data_index_ohlcv.scalars().fetchall() 
    df_index= convert_to_dataframe(load_data_index_ohlcv, ['date', 'close'], 'KOSPI')
    
    # Merge index and stock data and fill null data in stock index data
    df_stock_index = pd.merge(df_stock, df_index, on='date', how='outer')
    df_stock_index = fill_null_data_stock_index(df_stock_index, startDate, stopDate)
    
    # Extract commom word and count as much as reqCount
    common_words_count_lst = common_words_count(load_data_words_count, reqCount)

    # Make response list of dict fom json data only containing common words 
    response_dict_lst, db_date_lst  = make_response_data(load_data_words_count, common_words_count_lst)
    
	# Fill data of null date in words_count_dict_lst
    response_dict_lst = fill_null_data(response_dict_lst, db_date_lst, common_words_count_lst, startDate, stopDate)

    # Merge words_count_data and stock_index_data
    response_dict_lst = merge_list_df(response_dict_lst, df_stock_index, [stockCode])  

    return JSONResponse(content={"data":response_dict_lst, "comWords":common_words_count_lst})

