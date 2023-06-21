import csv

import requests
from lxml import etree

# 存放数据的列表
namelist = []
pointlist = []
peoplelist = []
wherelist = []
ilist = []
for i in range(0, 10):
    ilist.append(i)
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)  # 250条数据的url地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}  # 请求头
    r = requests.get(url=url, headers=headers)  # 发送请求
    data = r.text  # 获取响应数据
    f = etree.HTML(data)  # 解析
    movie_list = f.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for j in range(1, len(movie_list) + 1):
        try:
            name = f.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[1]/a/span[1]/text()')[0]  # 电影名字
            point = f.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/div/span[2]/text()')[0]  # 评分
            people = f.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/div/span[4]/text()')[0]  # 评价
            where = f.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/p[2]/span/text()')[0]  # 评语
            wherelist.append(where)
            print(name)
            print(point)
            print(people)
            print(where)
        except Exception as e:  # 错误则执行
            wherelist.append('None')
        namelist.append(name)
        pointlist.append(point)
        peoplelist.append(people)

with open('douban.csv', 'w', encoding='gbk', newline="") as f:
    fieldnames = ['电影名字', '评分', '评价', '评语']  # 表头
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()  # 插入表头
    for info in range(0, len(namelist)):
        try:
            f_csv.writerow(
                {
                    "电影名字": namelist[info],  # 插入数据
                    "评分": pointlist[info],
                    "评价": peoplelist[info],
                    "评语": wherelist[info]
                }
            )
        except Exception as e:
            print('列表为空')
