import json
import requests

url=requests.get('https://api.map.baidu.com/place/v2/search?query=益禾堂&tag=美食&region=西乡塘区&input=json&ak=Kcl9bynY5Icf1yGv6mQPzS7Phhkuw0Pb').content.decode('utf-8')
j=json.loads(url)

for i in j['results']:
    name=i['name']
    add=i['address']
    phone=i['telephone']
    print(name,add,phone)