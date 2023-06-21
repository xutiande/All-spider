"""获取所需的使用url地址"""
import csv
from time import sleep
import random
import json
import io
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
opt = ChromeOptions()

opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-web-security')
# opt.add_argument("--headless")
opt.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')  # 添加请求头

url = 'https://search.dangdang.com/?key=python&act=input&page_index=1'

browser = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)
browser.get(url)
# -----登录
browser.implicitly_wait(5)
browser.find_element(By.XPATH, '//*[@id="nickname"]/a[1]').click()
browser.implicitly_wait(5)
browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/a[3]/img').click()

title_list = []
price_list = []
now_price_list = []
press_list = []
browser.implicitly_wait(random.randint(10, 15))
# 获取信息
for page in range(2):
    div_list = browser.find_elements(By.XPATH, "//*[@class='con shoplist']/div[1]/ul/li")
    for i in range(1, len(div_list) + 1):
        sleep(random.random())
        try:
            title = browser.find_element(By.XPATH, f"//*[@class='con shoplist']/div[1]/ul/li[{i}]/a").get_attribute(
                'title')  # 标题
            title_list.append(title)
            price = browser.find_element(By.XPATH,
                                         f"//*[@class='con shoplist']/div[1]/ul/li[{i}]/p[3]/span[1]").text  # 现价
            price_list.append(price)
            now_price = browser.find_element(By.XPATH,
                                             f"//*[@class='con shoplist']/div[1]/ul/li[{i}]/p[3]/span[2]").text  # 原价
            now_price_list.append(now_price)
            browser.find_element(By.XPATH, f"//*[@class='con shoplist']/div[1]/ul/li[{i}]/a").click()
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])  # 切换到最后一个标签卡
            # sleep(random.randint(2, 5))
            browser.implicitly_wait(random.randint(5, 10))
            try:
                press = browser.find_element(By.XPATH, '//*[@id="product_info"]/div[2]/span[2]/a').text
                press_list.append(press)
            except Exception as e:
                pass
            browser.close()
            windows = browser.window_handles
            browser.switch_to.window(windows[0])  # 切换到最后一个标签卡
        except Exception as e:
            # print(e)
            pass
    browser.implicitly_wait(15)
    browser.find_element(By.XPATH, '//*[@id="12810"]/div[5]/div[2]/div/ul/li[10]/a').click()
    # windows = browser.window_handles
    # browser.switch_to.window(windows[-1])  # 切换到最后一个标签卡

with open('data.csv', 'w', encoding='gb18030', newline='') as f:
    filename = ['标题', '原价', '价格', '出版社']
    write_csv = csv.DictWriter(f, fieldnames=filename)
    write_csv.writeheader()
    for i in range(len(title_list)):
        try:
            write_csv.writerow({
                '标题': title_list[i],
                '原价': now_price_list[i],
                '价格': price_list[i],
                '出版社': press_list[i]

            })
        except Exception as e:
            print('写入为空!')
