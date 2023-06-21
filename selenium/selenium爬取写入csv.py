import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
position_list=[]
title_list=[]
name_list=[]
year_list=[]
url=webdriver.Chrome()
for i in range(10):
    url.get('https://www.maoyan.com/board?timeStamp=1672042464447&channelId=40011&index=10&signKey=e076b5025661aa44d9b8ce57441dd37e&sVersion=1&webdriver=false')  #循环页面
    url.implicitly_wait(10)
    html=url.page_source  #获取页面源代码
    get_position=url.find_element(By.XPATH,'//*[@id="app"]/div/div/div/dl/dd[{}]/i'.format(i+1)) .text
    get_title=url.find_element(By.XPATH,'//*[@id="app"]/div/div/div/dl/dd[{}]/div/div/div[1]/p[1]/a'.format(i+1)).text  #提取名字
    get_name =url.find_element(By.XPATH,'//*[@id="app"]/div/div/div/dl/dd[{}]/div/div/div[1]/p[2]'.format(i+1)).text    #提取演员
    get_year = url.find_element(By.XPATH,'//*[@id="app"]/div/div/div/dl/dd[{}]/div/div/div[1]/p[3]'.format(i+1)).text #提取上映时间
    position_list.append(get_position)
    title_list.append(get_title)
    name_list.append(get_name)
    year_list.append(get_year)
    print(get_position)
    print(get_title)
a=1
#
file_path = r'D:\爬虫图片放置文件\maoyan.csv'
with open(file_path, 'a', encoding='gbk', newline="") as f:
    fieldnames = ['position','title', 'name', 'year']
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    for info in range(0, len(position_list)):
        print('正在写入第{}部书'.format(info + 1))
        f_csv.writerow(
            {
                'position':position_list[info],
                "title": title_list[info],
                "name": name_list[info],
                "year": year_list[info],
            }

        )
