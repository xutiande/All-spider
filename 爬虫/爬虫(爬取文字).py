import bs4,requests
from bs4 import BeautifulSoup

url=requests.get('http://gxcme.edu.cn/').content.decode('utf-8')
html=BeautifulSoup(url,'html.parser')
ul=html.find(attrs={'class':'news','class':"content-list"})
a=ul.find_all('a')

l1 = []
l2 = []
l3 = []
for yaowen in a:
    # print(yaowen)
    href = yaowen['href']
    title = yaowen['title']
    l1.append(href)
    l2.append(title)
day=html.find(attrs={'class':'news','class':"header-list"})
span=ul.find_all('span')
for day in span:
    l3.append(day.text)
# dic4 = dict(zip(l1, l2,l3))
# print(dic4)
# print(l1)
# print(l2)
# print(l3)

for i in range(len(l1)):
    a = l1[i]
    b = l2[i]
    c = l3[i]
    print(a,b,c)
