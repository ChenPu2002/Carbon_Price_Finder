import gd
import nation as na
import hb
import tj

import re
import os
import pandas as pd
import numpy as np
from tabulate import tabulate
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
os.system('clear')
# 读取Excel文件
data = pd.read_excel('中国碳交易数据-202307.xlsx')

# 使用正则表达式过滤掉包含中文字符的行
filtered_data = data[~data['TradingDate'].astype(str).str.contains(r'[\u4e00-\u9fff]')]
filtered_data.loc[:, 'TradingDate'] = filtered_data['TradingDate'].apply(pd.to_datetime)

# 按照"CityName"分组并获取每个分组中"time"列的最大值
latest_time = filtered_data.groupby('CityName')['TradingDate'].max()
# print(latest_time)
gd_date = latest_time['广东']
compare_date = pd.to_datetime(gd.data['日期'])
data = []
data_insert = []
# 比较日期并打印结果
if gd_date < compare_date:
    data.append([gd.data['日期'], '广东', gd.data['开盘价：'], gd.data['最高价：'], gd.data['最低价：'], round(float(re.sub(r'[\u4e00-\u9fff]+', '', gd.data['成交金额：']))/float(re.sub(r'[\u4e00-\u9fff]+', '', gd.data['成交数量：'])), 2), gd.data['当前价：'], '', gd.data['涨跌幅：'], gd.data['成交数量：'], gd.data['成交金额：'], '', '', '', ''])
    data_insert.append([gd.data['日期'], '广东', 'GDEA',float(gd.data['开盘价：']), float(gd.data['最高价：']), float(gd.data['最低价：']), round(float(re.sub(r'[\u4e00-\u9fff]+', '', gd.data['成交金额：']))/float(re.sub(r'[\u4e00-\u9fff]+', '', gd.data['成交数量：'])), 2), float(gd.data['当前价：']), '', float(gd.data['涨跌幅：']), float(gd.data['成交数量：']), float(gd.data['成交金额：']), '', '', '', ''])
na_date = latest_time['中国']
compare_date = pd.to_datetime(na.data['日期'])
if na_date < compare_date:
    data.append([na.data['日期'], '中国', na.data['开盘价'], na.data['最高价'], na.data['最低价'], round(float(re.sub(r'[\u4e00-\u9fff]+', '', na.data['碳排放配额总成交额']))/float(re.sub(r'[\u4e00-\u9fff]+', '', na.data['碳排放配额总成交量'])), 2), na.data['收盘价'], '', na.data['收盘价较前一日上涨'], na.data['碳排放配额总成交量'], na.data['碳排放配额总成交额'], na.data['挂牌协议交易成交量'], na.data['碳排放配额总成交额'], na.data['大宗协议交易成交量'], na.data['大宗协议交易成交额']])
    data_insert.append([na.data['日期'], '中国', 'CEA', float(na.data['开盘价']), float(na.data['最高价']), float(na.data['最低价']), round(float(re.sub(r'[\u4e00-\u9fff]+', '', na.data['碳排放配额总成交额']))/float(re.sub(r'[\u4e00-\u9fff]+', '', na.data['碳排放配额总成交量'])), 2), float(na.data['收盘价']), '', float(na.data['收盘价较前一日上涨']), float(na.data['碳排放配额总成交量']), float(na.data['碳排放配额总成交额']), float(na.data['挂牌协议交易成交量']), float(na.data['碳排放配额总成交额']), float(na.data['大宗协议交易成交量']), float(na.data['大宗协议交易成交额'])])

hb_date = latest_time['湖北']
compare_date = pd.to_datetime(hb.data['日期'])
if hb_date < compare_date:
    data.append([hb.data['日期'], '湖北', '', hb.data['最高'], hb.data['最低'], round(float(re.sub(r'[\u4e00-\u9fff]+', '', hb.data['成交额']))/float(re.sub(r'[\u4e00-\u9fff]+', '', hb.data['成交量'])), 2), hb.data['最新'], hb.data['昨收盘价'], hb.data['涨跌幅'], hb.data['成交量'], hb.data['成交额'], '', '', '', ''])
    data_insert.append([hb.data['日期'], '湖北', 'HBEA', '', float(hb.data['最高']), float(hb.data['最低']), round(float(re.sub(r'[\u4e00-\u9fff]+', '', hb.data['成交额']))/float(re.sub(r'[\u4e00-\u9fff]+', '', hb.data['成交量'])), 2), float(hb.data['最新']), float(hb.data['昨收盘价']), float(hb.data['涨跌幅']), float(hb.data['成交量']), float(hb.data['成交额']), '', '', '', ''])

tj_date = latest_time['天津']
compare_date = pd.to_datetime(tj.data['日期'])
if tj_date < compare_date:
    data.append([tj.data['日期'], '天津', '', '', '', round((float(tj.data['挂牌均价'])*float(tj.data['挂牌量'])+float(tj.data['大宗均价'])*float(tj.data['大宗量']))/(float(tj.data['挂牌量'])+float(tj.data['大宗量'])), 2), '', '', '', float(tj.data['挂牌量'])+float(tj.data['大宗量']), float(tj.data['挂牌额'])+float(tj.data['大宗额']), tj.data['挂牌量'] if tj.data['挂牌量']!=0 else '', tj.data['挂牌额'] if tj.data['挂牌额']!=0 else '', tj.data['大宗量'] if tj.data['大宗量']!=0 else '', tj.data['大宗额'] if tj.data['大宗额']!=0 else ''])
    data_insert.append([tj.data['日期'], '天津', 'TJEA', '', '', '', round((float(tj.data['挂牌均价'])*float(tj.data['挂牌量'])+float(tj.data['大宗均价'])*float(tj.data['大宗量']))/(float(tj.data['挂牌量'])+float(tj.data['大宗量'])), 2), '', '', '', float(tj.data['挂牌量'])+float(tj.data['大宗量']), float(tj.data['挂牌额'])+float(tj.data['大宗额']), float(tj.data['挂牌量']) if tj.data['挂牌量']!=0 else '', float(tj.data['挂牌额']) if tj.data['挂牌额']!=0 else '', float(tj.data['大宗量']) if tj.data['大宗量']!=0 else '', float(tj.data['大宗额']) if tj.data['大宗额']!=0 else ''])

# 指定列名顺序
columns_show = ['日期', '名称', '开盘', '最高', '最低',
        '均价', '收盘', '前收盘', '涨跌', '总量', '总额',
        '挂牌量', '挂牌额', '大宗量', '大宗额']
columns_print = ['TradingDate', 'CityName', 'TradingType', 'OpenPrice', 'HighPrice', 'LowPrice',
        'AvgPrice', 'ClosePrice', 'PreClosePrice', 'ChangeRatio', 'Volume', 'Amount',
        'ListingVolume', 'ListingAmount', 'BulkVolume', 'BulkAmount']

# 创建DataFrame对象
df = pd.DataFrame(data, columns=columns_show)
df_insert = pd.DataFrame(data_insert, columns=columns_print)
output = tabulate(df[columns_show], headers='keys', tablefmt='fancy_grid', numalign='center', stralign='center',floatfmt=".2f")

if len(data) == 0:
    print("没有需要更新的数据。")
else:
    print('检测到以下%d条数据需要更新:' % len(data))
    print(output)
    print('\n')
    # print(df_insert)
    confirmation = input("确认要在excel中插入以上数据吗?(y/n): ")

    if confirmation.lower() == 'y':
        print("执行操作...")
        # 读取现有的 Excel 文件
        workbook = load_workbook('中国碳交易数据-202307.xlsx')

        # 获取要操作的工作表
        sheet = workbook['sheet1']
        # 将 DataFrame 的数据逐行写入工作表
        for row in dataframe_to_rows(df_insert, index=False, header=False):
            sheet.append(row)

        # 保存修改后的 Excel 文件
        workbook.save('中国碳交易数据-202307.xlsx')
        print("操作完成。")
    elif confirmation.lower() == 'n':
        print("取消操作...")
    else:
        print("无效的输入，请重新运行程序并输入 'y' 或 'n'。")