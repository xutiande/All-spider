import urllib.request
import requests
from lxml import html
from bs4 import BeautifulSoup

url = requests.get('http://gxcme.edu.cn/').content.decode('utf-8')
ht = html.fromstring(url)
a = ht.xpath('//*[@id="tab1"]/li/a')
l1 = []
for i in a:
    href = i.xpath('./@href')[0]
    url2 = requests.get('http://gxcme.edu.cn/' + href).content.decode('utf-8')
    # print(url2)
    soup = BeautifulSoup(url2, "html.parser")
    div = soup.find(class_='v_news_content').text


print(div)



f=open('xtd.txt', 'w', encoding='utf-8')
f.write(div)
f.close()
# f = open('xtd.txt', 'w')
# for j in range(len(div)):
#     f.write(l1[j] + '\n')
# f.close()
