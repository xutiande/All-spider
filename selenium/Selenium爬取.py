import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup



url=webdriver.Chrome('chromedriver')
url.get('https://image.baidu.com/search/albumsdetail?tn=albumsdetail&word=%E5%9F%8E%E5%B8%82%E5%BB%BA%E7%AD%91%E6%91%84%E5%BD%B1%E4%B8%93%E9%A2%98&fr=searchindex_album%20&album_tab=%E5%BB%BA%E7%AD%91&album_id=7&rn=30')
print(url.title)
for i in range(20):
    ActionChains(url).send_keys(Keys.PAGE_DOWN).perform()  #滚动
time.sleep(5)
html=url.page_source  #获取页面源代码
# print(html)
soup=BeautifulSoup(html)  #解析
# img=soup.find_all(class_='main_img img-hover')
img=soup.find_all(class_='albumsdetail-item-img') #定位全部class_
s=1
# for j in img:
#     a=j['src']
#     print(a)
#     with open('D:\爬虫图片放置文件\%d.jpg' % s ,'wb' )as f:
#         f.write(requests.get(a).content)
#         print('正在下载第%s张图片'% s)
#         s+=1