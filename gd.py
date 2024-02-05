import requests
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create Chrome WebDriver with configured options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create Chrome WebDriver with configured options
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://ets.cnemission.com/carbon/portalIndex/marketrealtime")
time.sleep(3)

# 使用 WebDriver 获取所有带有 tdleft 类的元素
tdleft_elements = driver.find_elements(By.CLASS_NAME,"tdright")

# 使用 WebDriver 获取所有带有 labfund 类的 label 元素
label_elements = driver.find_elements(By.CLASS_NAME,"labfund")

text = driver.find_element(By.ID,"myDayInfo").text
matches = re.findall(r'\((.*?)\)', text)
# 创建字典来存储数据
data = {}
data['日期'] = matches[0]
# 遍历 tdleft 元素和 label 元素，将它们一一对应存储在字典中
for i in range(len(tdleft_elements)):
    tdleft_text = tdleft_elements[i].text
    label_text = label_elements[i].text
    label_text = re.sub(r'[\u4e00-\u9fff%]+', '', label_text)
    data[tdleft_text] = label_text

# # 打印提取到的数据
# for tdleft_text, label_text in data.items():
#     print(f"{tdleft_text}: {label_text}")

# 关闭浏览器
driver.quit()