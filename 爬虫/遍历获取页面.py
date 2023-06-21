import requests
from bs4 import BeautifulSoup
import re
n=1
for i in range(10):
    headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}
    url='https://ssr1.scrape.center/detail/{}'.format(n)
    n += 1
    soup=BeautifulSoup(url,'html.parser')
    div=soup.find(attrs={'class':'el-card__body'})

    a=1