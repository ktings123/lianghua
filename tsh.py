import tushare as ts


pr=ts.pro_api("387276e8d62e008b201ae4c7314283c849843864b04dc722e9d2cf8e")

print(pr.query('daily',ts_code='002714.SZ',start_date='20210809',end_date='20210810'))