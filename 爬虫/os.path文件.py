import os
import os.path
import re
import requests

d=""
# url=requests.get("http://gxcme.edu.cn/").content.decode('utf-8')
url=r'C:\Program Files\Python38\代码\xtd.txt'
a=os.path.basename(url)
b=os.path.splitext(a)

print(a)
print(b)

# img/news-img/20220713.jpg