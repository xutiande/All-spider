import csv
import urllib.request
import requests
from bs4 import BeautifulSoup

title_list = []
score_list = []
time_list = []
introduce_list = []
img_list = []
for i in range(2):
    i += 1
    url = 'https://ssr1.scrape.center/detail/{}'.format(i)  # 循环每个电影标签页
    html = requests.get(url).content.decode('utf-8')  # 将每个标签解析为utf-8
    soup = BeautifulSoup(html)  # 解析网页
    # print(soup)
    title = soup.find(class_='m-b-sm').text  # find寻找class下的全部m-b-sm，并提取文本
    score = soup.find(class_='score m-t-md m-b-n-sm').text  ##find寻找class下的全部score m-t-md m-b-n-sm，并提取文本
    time = soup.find(class_='m-v-sm info').text  ##find寻找class下的全部m-v-sm info，并提取文本
    introduce = soup.find(class_='drama').text  ##find寻找class下的全部drama，并提取文本
    img = soup.find(class_='cover').get('src')  ##find寻找class下的全部cover，用get方法获取cover中的src属性
    title_list.append(title)
    score_list.append(score)
    time_list.append(time)
    introduce_list.append(introduce)
    img_list.append(img)
    print(title.replace('\n', ''))
    print('影片评分' + score.replace('\n', '').replace('    ', ''))
    print(time.replace('\n', ''))
    print(introduce.replace('\n', '').replace('                  ', ''))  # 网址有许多空格，替换成没有
    print(img)

with open('data.csv', 'w', encoding='gb18030', newline="") as f:  # 将每个页面的url地址存储进csv文件中
    filename = ['标题', '评分', '时间', '介绍', '图片链接']  # 表头
    f_csv = csv.DictWriter(f, fieldnames=filename)
    f_csv.writeheader()
    for info in range(0, len(time_list)):
        f_csv.writerow(
            {
                '标题': time_list[info],
                '评分': score_list[info],
                '时间': time_list[info],
                '介绍': introduce_list[info],
                '图片链接': img_list[info],

            }
        )
