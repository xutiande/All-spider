from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
url=webdriver.Chrome()
for i in range(10):
    url.get('https://spa1.scrape.center/detail/{}'.format(i+1))  #循环页面
    url.implicitly_wait(10)
    html=url.page_source  #获取页面源代码
    get_biaot=url.find_element(By.CSS_SELECTOR,'#detail > div:nth-child(1) > div > div > div.el-card__body > div > div.p-h.el-col.el-col-24.el-col-xs-16.el-col-sm-12 > a > h2').text  #提取标题
    get_pingf=url.find_element(By.CSS_SELECTOR,'#detail > div:nth-child(1) > div > div > div.el-card__body > div > div.el-col.el-col-24.el-col-xs-8.el-col-sm-4 > p.score.m-t-md.m-b-n-sm').text  #提取评分
    get_jies =url.find_element(By.CSS_SELECTOR,'#detail > div:nth-child(1) > div > div > div.el-card__body > div > div.p-h.el-col.el-col-24.el-col-xs-16.el-col-sm-12 > div.drama > p').text    #提取影片介绍
    get_diz = url.find_element(By.CSS_SELECTOR,'#detail > div:nth-child(1) > div > div > div.el-card__body > div > div.p-h.el-col.el-col-24.el-col-xs-16.el-col-sm-12 > div:nth-child(3)').text #提取地址
    get_tup = url.find_element(By.CSS_SELECTOR,'#detail > div:nth-child(1) > div > div > div.el-card__body > div > div.el-col.el-col-24.el-col-xs-0.el-col-sm-8 > a > img').get_attribute('src') #提取图片
    # f=open(r'D:\wyw.txt','a',encoding='utf-8')  #写入文本
    # f.write(get_biaot+'\n')
    # f.write(get_pingf+'\n')
    # f.write(get_diz+'\n')
    # f.write(get_jies+'\n')
    # f.close()
    # jpg=open(r'D:\{}.jpg'.format(i),'wb')  #写入图片
    # jpg.write(requests.get(get_tup).content)