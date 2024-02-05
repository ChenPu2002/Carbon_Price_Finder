import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.hbets.cn/list_30.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
text = response.text
# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(text, 'html.parser')

# 查找所有行（tr）并提取数据
data = {}
rows = soup.find_all('tr')
name = rows[0].find_all('th')
value = rows[1].find_all('td')
for i in range(len(name)):
    va = re.sub(r'[\u4e00-\u9fff%,]+', '', str(value[i].text.strip()))
    data[name[i].text] = va

# print(data)