import bs4,requests
from bs4 import BeautifulSoup

url=requests.get('http://www.redbull.com.cn/about/branch').content.decode('utf-8')
x=0
l1 = []
l2 = []
l3 = []
l4 = []
def gethtml(url):
    html=BeautifulSoup(url,'html.parser')
    ul=html.find(attrs={'class':'con'})
    a=ul.find_all('li')
    b=ul.find_all('p')
    # print(a)
    for xx in a:
        biaoti = xx['data-title']
        l1.append(biaoti)
        dizhi = xx['data-describe']
        l2.append(dizhi)
        # youxiang = xx[class="mailIco"']
        # print(youxiang)
    ul1 = html.find(attrs={"class": "con"'mailIco'})
    a1 = ul.find_all('p', ['mailIco'])
    for yx in a1:

        l3.append(yx.text)
    ul2 = html.find(attrs={"class": "con"'telIco'})
    a2 = ul.find_all('p', ['telIco'])
    for dh in a2:
        # print(yx.text)
        l4.append(dh.text)
    for i in range(len(l1)):
        a = l1[i]
        b = l2[i]
        c = l3[i]
        d = l4[i]
        print('--------------------------')
        print(a, b, c,d)

    # for i in a:
    #     dizhi=i['data-title']
    #     weizhi = i['data-describe']
    #     print(dizhi)
    #     print(weizhi)


    # ul1 = html.find(attrs={'class': 'con','class':'mailIco'})
    # print(ul1.text)
    # ul2 = html.find(attrs={'class': 'con', 'class': 'telIco'})
    # print(ul2.text)

    #
    # for n in a:
    #     print(ul2.text)

    # for j in a1:
    #     yx = j['p.maillco']
    #     print(yx)


gethtml(url)