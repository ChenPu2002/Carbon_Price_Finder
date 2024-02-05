import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
# url = 'https://www.cneeex.com/qgtpfqjy/mrgk/2023n/'
url = 'https://www.cneeex.com/qgtpfqjy/mrgk/2023n/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
text = response.text
def get_first_li_link(text):

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(text, 'html.parser')

    # 查找<div class="list-right">元素
    list_right_div = soup.find('div', class_='list-right')

    # 查找<div class="list-right">下的第一个<li>元素
    first_li = list_right_div.find('li')

    # 提取链接
    link = first_li.find('a')['href']
    
    global title
    title = first_li.find('a').text

    return link
def print_number(text):
    # 提取数字的正则表达式模式
    number_pattern = r'[\d,.]+'

    # 提取价格行情中的数字
    price_open = re.search(r'开盘价({})'.format(number_pattern), text).group(1)
    price_high = re.search(r'最高价({})'.format(number_pattern), text).group(1)
    price_low = re.search(r'最低价({})'.format(number_pattern), text).group(1)
    price_close = re.search(r'收盘价({})'.format(number_pattern), text).group(1)
    price_change = re.search(r'收盘价较前一日上涨([\d.]+)%', text).group(1)

    # 提取交易成交量和成交额中的数字
    volume_agreement = re.search(r'挂牌协议交易成交量({})'.format(number_pattern), text).group(1)
    amount_agreement = re.search(r'成交额({})元'.format(number_pattern), text).group(1)
    volume_bulk = re.search(r'大宗协议交易成交量({})'.format(number_pattern), text).group(1)
    amount_bulk = re.search(r'成交额({})元'.format(number_pattern), text).group(1)

    # 提取碳排放配额总成交量和总成交额中的数字
    volume_quota = re.search(r'碳排放配额总成交量({})'.format(number_pattern), text).group(1)
    amount_quota = re.search(r'总成交额({})元'.format(number_pattern), text).group(1)

    # 打印提取到的数字
    # print("开盘价:", price_open)
    # print("最高价:", price_high)
    # print("最低价:", price_low)
    # print("收盘价:", price_close)
    # print("收盘价较前一日上涨:", price_change, "%")
    # print("挂牌协议交易成交量:", volume_agreement)
    # print("挂牌协议交易成交额:", amount_agreement)
    # print("大宗协议交易成交量:", volume_bulk)
    # print("大宗协议交易成交额:", amount_bulk)
    # print("碳排放配额总成交量:", volume_quota)
    # print("碳排放配额总成交额:", amount_quota)
    global data
    data = {
    "开盘价": price_open,
    "最高价": price_high,
    "最低价": price_low,
    "收盘价": price_close,
    "收盘价较前一日上涨": price_change,
    "挂牌协议交易成交量": volume_agreement,
    "挂牌协议交易成交额": amount_agreement,
    "大宗协议交易成交量": volume_bulk,
    "大宗协议交易成交额": amount_bulk,
    "碳排放配额总成交量": volume_quota,
    "碳排放配额总成交额": amount_quota}

    data = {key: re.sub(r'[\u4e00-\u9fff%,]+', '', str(value)) for key, value in data.items()}


def check_for_updates(text):

    link = 'https://www.cneeex.com/'+get_first_li_link(text)
    response_for_today = requests.get(link, headers=headers)
    response_for_today.encoding = 'utf-8'
    today = response_for_today.text
    print_number(today)

check_for_updates(text)
title = re.sub(r'[\u4e00-\u9fff]+', '', title)
date_obj = datetime.strptime(title, "%Y%m%d")
formatted_date = date_obj.strftime("%Y-%m-%d")
data['日期'] = formatted_date
# print(data)