import urllib.request

import bs4, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.umei.cc/bizhitupian/diannaobizhi/').content.decode('utf-8')
num = 0


def gethtml(url):
    html = BeautifulSoup(url, 'html.parser')
    ul = html.find(attrs={'class': 'item_list infinite_scroll'})
    a = ul.find_all('img')

    for tupian in a:
        img = tupian['data-original']
        print(img)

        global num
        urllib.request.urlretrieve(img, r'D:\爬虫图片放置文件\%s.jpg' % num)
        num += 1
        print('正在下载%s张' % num)


gethtml(url)
