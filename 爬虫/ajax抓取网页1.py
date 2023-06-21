import requests
import json
import urllib.request

url=requests.get("https://api.bilibili.com/x/web-interface/web/channel/category/channel/list?id=100&offset=0&page_size=100").content.decode("utf-8")

j = json.loads(url)
a= 1
l=j['data']['channels']
num=1
for i in l:
    background=i['background']
    name=i['name']

    print(name)
    print(background)
    # print("---------------------------------------------")
    # b=background.split(".")
    # c=b[-1]
    # with open("xtd.txt","wb") as f:
    #     f.write(requests.get(background).content)
    #     f.close()
