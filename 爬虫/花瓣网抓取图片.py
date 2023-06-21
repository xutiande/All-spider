import requests
import json
import urllib.request


url=requests.get("https://api.huaban.com/search?q=%E8%BF%9B%E5%87%BB%E7%9A%84%E5%B7%A8%E4%BA%BA&sort=all&per_page=20&page=1&hide_other_count=1") .content.decode('utf-8')

# print(url)
j=json.loads(url)
a=1
l=j['pins']
num=0

for i in l:

    # dict = i['orig_source']
    dict = i['file']['key']
    raw_text = i['raw_text']
    a = 'https://gd-hbimg.huaban.com/' + dict
    print("------------------------------------------------")
    print(a)
    urllib.request.urlretrieve(a, 'C:\Program Files\Python38\img1\%s.jpg' %num)
    num += 1
    print('正在下载\%s张' %num)
