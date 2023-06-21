import requests
from bs4 import BeautifulSoup
import re
url='https://www.shicimingju.com/book/sanguoyanyi.html'
n=0
num=0
list = {}
def getshici(url):
    global n
    global num

    headers={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}
    url1=requests.get(url,headers=headers)
    soup=BeautifulSoup(url1.text.encode(url1.encoding),'lxml')
    div=soup.find('div',attrs= {'class':'book-mulu'})
    div1=div.find_all('a')
     # print(div2)

    for i in div1:
        a=i['href']
        a1='https://www.shicimingju.com/'+a
        name=div.select('li')[n].text+'\n'
        n += 1
        shici=name+a1
        headers1={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.178.400 QQBrowser/11.2.5170.400'}
        url2=requests.get(a1,headers=headers1)

        soup1 = BeautifulSoup(url2.text.encode(url2.encoding), 'lxml')
        text=soup1.find('div',attrs={'class':'chapter_content'})
        # zhengze=re.compile(r'(.*)')
        # zhengze1=re.findall(zhengze,text)
        #
        text1=str(text.text)
        text2 = text1.replace(' ','').replace('\t','').strip('\n')
        t=name+text2+'\n'
        b=1
        #
        # with open('xtd2.txt','a',encoding='utf-8')as f:
        #     f.write(t)
        #     num += 1
        #     print('三国演义小说已写入{}篇'.format(num))
        #     print('--------------------------------------------------')
        #     f.close()
getshici(url)
