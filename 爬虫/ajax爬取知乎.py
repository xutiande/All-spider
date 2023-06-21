from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
base_url='https://www.zhihu.com/api/v4/news_specials/list?'
headers={
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/special/all',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'X-Requested-With':'fetch'
    }

#获取网页的响应并返回json格式的数据
def get_offset(offset):
    params={
        'limit':'10',
        'offset':offset
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):
    if json:
        items=json.get('data')
        for item in items:
            zhihu={}
            zhihu['banner']=item.get('banner')
            zhihu['id']=item.get('id')
            zhihu['updated']=item.get('updated')
            zhihu['title']=pq(item.get('title')).text()
            yield zhihu
            a=1
if __name__=='__main__':
    for offset in range(1,10):
        json=get_offset(offset)
        results=parse_page(json)
        for result in results:
            print(result)
            with open(r'D:\python爬取写入文件\zhihu.txt','a')as f:
                f.write(str(result))
                f.write('\n')