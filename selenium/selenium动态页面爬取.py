import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
url='https://spa1.scrape.center/'
browser = webdriver.Chrome()
browser.get(url)
def xtd(browser):
    for j in range(5):
        j+=1
        html = 'https://spa1.scrape.center/detail/{}'.format(j)  #循环每个电影标签页
        browser.get(html)  #获取每个电影标签
        browser.implicitly_wait(10)  # 等待时长最多不超过10秒
        bt = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div/div/div[2]/a/h2').text  # 获取电影名称
        pf = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[3]/p[1]').text  # 获取电影评分
        dz = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[2]').text  # 获取电影地址
        js = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p').text  # 获取电影介绍
        tp = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[1]/a/img').get_attribute('src')  # 通过get_attribute获取img节点中的src
        # print(bt)
        # print(pf)
        # print(dz)
        # print(js)
        # print(tp)
        with open(r'D:\python爬取写入文件\selenium篇\xtd.txt', 'a', encoding='utf-8') as f:
            f.write("{}{}{}{}{}{}{}{}{}".format('\n',bt, '\n', dz, '\n', '评分：'+pf, '\n', js, '\n'))
            print('已经写入的第{}部电影'.format(j))
            urllib.request.urlretrieve(tp, 'D:\python爬取写入文件\selenium篇\{}.jpg'.format(j))
            print('正在下载{}张'.format(j))
            print('------------')
xtd(browser)
