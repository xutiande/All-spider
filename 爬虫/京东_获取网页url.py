# -*- coding: utf-8 -*-
# @Author: XuTianDe
# @Date: 2023-05-07 22:01:49

"""获取所需的使用url地址"""
import csv
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

opt = ChromeOptions()

opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-web-security')
opt.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35')  # 添加请求头
url = 'https://search.jd.com/Search?keyword=Python&wq=Python&pvid=25142fcc7bee448f968bc51ef8cf9944&page=1&s=1&click=0'  # jd网址链接

browser = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)

browser.get(url)
url_list = []
for i in range(1, 19):
    browser.find_element(By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[9]').click()  # 点击每个页面的下一页
    print(browser.current_url)
    sleep(5 * random.random())
    url_list.append(browser.current_url)

with open('data.csv', 'w', encoding='gb18030', newline="") as f:  # 将每个页面的url地址存储进csv文件中
    filename = ['京东每页url地址']  # 表头
    f_csv = csv.DictWriter(f, fieldnames=filename)
    f_csv.writeheader()
    for info in range(0, len(url_list)):
        f_csv.writerow(
            {
                '京东每页url地址': url_list[info]
            }
        )
