import functools, operator, collections
from datetime import datetime, timedelta

### Extract commom word and count as much as reqCount
# To access commom word : common_words_count_lst[0][0], common_words_count_lst[1][0] ...
# To access common word count : common_words_count_lst[0][1], common_words_count_lst[1][1] ...
def common_words_count(result_data_from_sql, reqCount) -> list:
    words_dict_list = []
    for row in result_data_from_sql:
        row_words_count_dict = dict(row.words_count)
        words_dict_list.append(row_words_count_dict)
    
    # Add dict with sum value if same key
    result_dict = dict(functools.reduce(operator.add,
        map(collections.Counter, words_dict_list)))

    # Remove stopwords 
    result_dict_remove_stopwords = dict()    
    stopwords = ['col2', 'col6']
    for key, value in result_dict.items():
        if key not in stopwords:
            result_dict_remove_stopwords[key] = value
    
    # Sort by value
    result_sorted_dict = sorted(result_dict_remove_stopwords.items(), key=lambda item: item[1], reverse = True) 

    # Handling case when reqCount is bigger than common word
    if len(result_sorted_dict) < reqCount:
        reqCount = len(result_sorted_dict)
        
    return result_sorted_dict[:reqCount]


### Make response list of dict fom json data only containing common words 
# response_dict_lst : list of dictionary that have key of date, common words 
# db_date_lst       : date which exist in database
def make_response_data(result_data_from_sql, common_words_count_lst):
    response_dict_lst = []
    db_date_lst = []
    for row in result_data_from_sql:
        date = row.date
        db_date_lst.append(datetime.strptime(date, "%Y-%m-%d").date())
        word_dict = dict(row.words_count)
        
        data_dict = {"date":date}
        for i, (word, count) in enumerate(common_words_count_lst):
            try:
                data_dict[common_words_count_lst[i][0]] = word_dict[word] 
            except:
                data_dict[common_words_count_lst[i][0]] = 0

        response_dict_lst.append(data_dict)
    return response_dict_lst, db_date_lst



### Fill data of null date
def fill_null_data(response_dict_lst, db_date_lst, common_words_count_lst, startdate, stopdate):
    startdate = datetime.strptime(startdate, "%Y-%m-%d").date()
    stopdate = datetime.strptime(stopdate, "%Y-%m-%d").date()
    response_dict_lst_total = []
    k = 0   # for count append response_dict_lst to response_dict_lst_total
    while startdate <= stopdate:
        if startdate not in db_date_lst:
            replace_data = {"date":datetime.strftime(startdate, "%Y-%m-%d")}
            for i in range(0,len(common_words_count_lst)):
                replace_data[common_words_count_lst[i][0]] = 0
            response_dict_lst_total.append(replace_data)        
        else:   # Already exsist data
            response_dict_lst_total.append(response_dict_lst[k])
            k += 1
        startdate = startdate + timedelta(days=1)
    return response_dict_lst_total
