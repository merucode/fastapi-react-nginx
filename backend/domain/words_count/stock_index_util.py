import pandas as pd
from datetime import datetime, timedelta

### Conver model object to dataframe
def convert_to_dataframe(model_data, col_names, code):
    data = [row.__dict__ for row in model_data]
    df = pd.DataFrame(data)
    df = df[col_names]

    # Column Name Custom
    df = df.rename(columns={'close':code})
    return df


### Fill null data
def fill_null_data_stock_index(df, startdate, stopdate):
    date_range = pd.date_range(start=startdate, end=stopdate, freq='D')    # Create date range
    # Add startdate, stopdate to DataFrame
    df = pd.concat([pd.DataFrame({'date': [startdate]}), df, pd.DataFrame({'date': [stopdate]})], ignore_index=True)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date') # Sort by date

    df = df.groupby('date').first().reindex(date_range).reset_index()   # Resampling as Date
    df = df.rename(columns={'index':'date'})
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    df = df.fillna(method='ffill')  # Fill NaN Data using data(pre:ffill, after:bfill)
    df = df.fillna(0)
    return df


### Merge df and list of dictionary
def merge_list_df(lst_data, df_data, stockCode) -> list:
    result_dict_lst = []
    codes = [stockCode[0], 'KOSPI']

    for row in lst_data:
        dict = row
        date = dict['date']
        for code in codes:
            dict[code] = df_data[df_data['date']==date][[code]].iat[0,0]
        result_dict_lst.append(dict)
    return result_dict_lst
