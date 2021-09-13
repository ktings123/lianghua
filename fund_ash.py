import akshare as ak
import pandas as pd


def fund_cn_daily_Report(isList):
    """
    场内基金
    实时行情返回,all
    :param isList: ['sz002714', 'sz000858','sh603288','sz000333','sh600519',..]
    :return:
    """

    fund_etf_fund_df = ak.fund_em_etf_fund_daily()
    fund_etf_daily_report = pd.DataFrame()
    for i in isList:
        fund_etf_daily_report = fund_etf_daily_report.append(fund_etf_fund_df.loc[fund_etf_fund_df['基金代码'] == i],
                                                             ignore_index=True)

    return fund_etf_daily_report


fund_pool = ['515030', '515700', '516760', '161725','513330']

print(fund_cn_daily_Report(fund_pool))

# fund_em_value_estimation=ak.fund_em_value_estimation()
# print(fund_em_value_estimation.loc[fund_em_value_estimation['基金代码']=='161725'])

# fund_em_open_fund_daily=ak.fund_em_open_fund_daily()
# fund_open_fund_daily=fund_em_open_fund_daily.loc[fund_em_open_fund_daily['基金代码']=='161725']
# print(fund_open_fund_daily.loc[2:7])