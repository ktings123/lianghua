import akshare as ak
import pandas as pd

''' 
example:
        df.loc[df['shield'] > 6, ['max_speed']] 指定列where
        df.loc[['viper', 'sidewinder']]  指定行
        df.loc['cobra', 'shield']   行,列定位数据

'''


# stock_fund_flow_individual_df = ak.stock_fund_flow_individual(symbol="3日排行")


def big_deal_check(isStr):
    """
    关键词搜素 大笔买入,大笔卖出...
    :param  isStr:string
    :return:
    :rtype: pandas.DataFrame
    """
    if isinstance(isStr, str):
        stock_changes_df = ak.stock_changes_em(symbol=isStr).drop_duplicates(['代码'], keep='last')
        return stock_changes_df
    else:
        print('plz str !')


def daily_Report(isList):
    """
    实时行情返回,all
    :param isList: ['sz002714', 'sz000858','sh603288','sz000333','sh600519',..]
    :return:
    """

    stock_zh_a_spot_df = ak.stock_zh_a_spot()
    daily_report = pd.DataFrame()
    for i in isList:
        daily_report = daily_report.append(stock_zh_a_spot_df.loc[stock_zh_a_spot_df['代码'] == i], ignore_index=True)

    return daily_report.loc[:, ['代码', '名称', '最新价', '涨跌幅', '买入', '卖出', '成交量']]


# print(stock_changes_df.loc[:,'代码':'板块'])
# print(stock_changes_df.loc[1, '代码'])
# print(stock_changes_df.loc[stock_changes_df["代码"]=='688663',['名称']])

# 个股历史数据,频率period,后10条,筛选字段
# stock_zh_a_min_df=ak.stock_zh_a_minute(symbol='sz000858',period='60',adjust='qfq').tail(10).loc[:,'day':'low']


# stock_zh_a_daily_df =ak.stock_zh_a_daily(symbol='sz002714 ',adjust='qfq')
# print(stock_zh_a_spot_df.loc[stock_zh_a_spot_df['名称']=='牧原股份'])
code_pool = ['sz002714', 'sz000858', 'sh603288', 'sz000333', 'sh600519']
# 'sz00858'
print(daily_Report(code_pool))

a = pd.DataFrame()
b = pd.DataFrame([[10, 29, 2, 7], [1, 2, 3, 4], [2, 5, 7, 0]], columns=list('ABCD'), index=['x', 'y', 'z'])

# for i in [10,1]:
#     a=a.append(b.loc[b['A']== i ],ignore_index=True)
# print(a.loc[:,['A','C']])
