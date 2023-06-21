# -*- coding: utf-8 -*-

import csv
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

# 破解浏览器反爬
opt = ChromeOptions()
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-web-security')
opt.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35')  # 添加请求头
# 获取csv文件中的所有url地址
browser = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)

url_list = []
with open('data.csv', 'r', encoding='gb18030') as f:
    url_list.append(f.readlines())
urls = url_list[0][1:]

title_list = []
price_list = []
appraise_list = []
shop_list = []
title_url_list = []
shop_url_list = []
category_list = []
page = 0

for i in urls:
    page += 1
    url = i.strip()  # jd网址链接
    browser.get(url)
    for scroll in range(30):  # 向下滚动5次
        # 将页面向下滚动100个像素
        browser.execute_script("window.scrollBy(0, 400);")
        # 等待0.5秒，模拟滚动的时间间隔
        sleep(random.random())
    div_list = browser.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')

    for li in range(1, len(div_list) + 1):
        sleep(random.randint(1, 3) * random.random())
        # print('爬取中................')
        try:
            category = '手机'
            category_list.append(category)
            title = browser.find_element(By.XPATH, f'//*[@id="J_goodsList"]/ul/li[{li}]/div/div[4]/a/em').text  # 名称
            # print(title)
            title_list.append(title)  # 追加入列表
            title_url = browser.find_element(By.XPATH,
                                             f'//*[@id="J_goodsList"]/ul/li[{li}]/div/div[4]/a').get_attribute(
                'href')  # 名称地址
            title_url_list.append(title_url)  # 追加入列表
            price = browser.find_element(By.XPATH,
                                         f'//*[@id="J_goodsList"]/ul/li[{li}]/div/div[3]/strong/i').text  # 价格
            # print(price)
            price_list.append(price)  # 追加入列表
            # print(price)
            appraise = browser.find_element(By.XPATH,
                                            f"//*[@class='ml-wrap']/div[2]/ul/li[{li}]/div/div[5]/strong/a").text  # 评价数
            # print(appraise)
            appraise_list.append(appraise)  # 追加入列表
            # print(appraise)
            shop = browser.find_element(By.XPATH,
                                        f"//*[@class='ml-wrap']/div[2]/ul/li[{li}]/div/div[7]/span/a").get_attribute(
                'title')  # 店铺名字
            # print(appraise)
            shop_list.append(shop)  # 追加入列表
            shop_url = browser.find_element(By.XPATH,
                                            f"//*[@class='ml-wrap']/div[2]/ul/li[{li}]/div/div[7]/span/a").get_attribute(
                'href')  # 店铺地址
            shop_url_list.append(shop_url)
            # print(shop)
        except Exception as e:
            # print('找不到节点', e)
            pass
    print(f'第{page}爬取完成！')

with open('jd_data.csv', 'w', encoding='gb18030', newline="") as f:
    filename = ['类目', '商品名称', '商品地址', '商品价格', '商品评价', '店铺名称', '店铺地址']
    f_csv = csv.DictWriter(f, fieldnames=filename)
    f_csv.writeheader()
    for info in range(len(price_list)):  # 根据存入列表的长度进行循环遍历
        try:
            f_csv.writerow(
                {
                    '类目': category_list[info],
                    '商品名称': title_list[info],
                    '商品地址': title_url_list[info],
                    '商品价格': price_list[info],
                    '商品评价': appraise_list[info],
                    '店铺名称': shop_list[info],
                    '店铺地址': shop_url_list[info],
                }
            )
        except:
            print('为空跳过写入')

browser.quit()