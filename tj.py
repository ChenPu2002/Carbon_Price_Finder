import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.chinatcx.com.cn/list/13.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
text = response.text
# print(text)
# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(text, 'html.parser')

data = {}
rows = soup.find_all('tr')
name = ['日期','品种','挂牌量','大宗量','挂牌额','大宗额','挂牌均价','大宗均价']
value = rows[2].find_all('td')
for i in range(len(name)):
    if value[i].text.strip() == '-':
        da = 0
    else:
        da = re.sub(r'[,]+', '',value[i].text.strip())
    data[name[i]] = da
