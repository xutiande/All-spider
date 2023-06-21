import csv

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
namelist = []
ranklist = []
ratelist = []

url = 'https://www.wanwupai.com/sale/810.html'
r = requests.get(url=url, headers=headers)
data = r.text
f = etree.HTML(data)
div_list = f.xpath("//*[@class='top-box']/div[1]/div")
print(len(div_list))
for i in range(1, len(div_list) + 1):
    print(type(i))
    if i == 9:
        names = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[2]/div[1]/a/text()")[0]
        name='9、'+names
        namelist.append(name)
        rank = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[2]/div[2]/text()")[0]
        ranklist.append(rank)
        rate = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[3]/div[1]/text()")[0]
        ratelist.append(rate)
    else:
        name = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[2]/div[1]/text()")[0]
        namelist.append(name)
        rank = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[2]/div[2]/text()")[0]
        ranklist.append(rank)
        rate = f.xpath(f"//*[@class='top-box']/div[1]/div[{i}]/div[3]/div[1]/text()")[0]
        ratelist.append(rate)
file_path = r'book.csv'
with open(file_path, 'w', encoding='gbk', newline="") as f:
    fieldnames = ['书名', '销量', '价格']
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    for info in range(0, len(namelist)):
        print('正在写入第{}部书'.format(info + 1))
        f_csv.writerow(
            {
                "书名": namelist[info],
                "销量": ranklist[info],
                "价格": ratelist[info],
            }

        )
