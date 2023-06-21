# -*- codeing = utf-8 -*-

import re  # 正则表达式，获取网页数据
import urllib.error  # 制定URL获取网页数据
import urllib.request

import xlwt  # 进行excel操作
from bs4 import BeautifulSoup  # 网页解析，获取数据


def main():
    baseurl = "https://movie.douban.com/top250?start="  # 爬取网页
    datalist = getData(baseurl)
    savepath = r"D:\python爬取写入文件\douban.xls"
    saveData(datalist, savepath)
    download(datalist)


findLink = re.compile(r'<a href="(.*?)">')  # 影片详情链接规则
findImgSrc = re.compile(r'<img.*?src="(.*?)"', re.S)  # 查找电影海报链接 re.S让换行符再字符中
findName = re.compile(r'<span class="title">(.*)</span>')  # 查找电影名字
findRating = re.compile(r'<span class="rating_num".*?>(.*)</span>')  # 影片评分
findPeopleNumber = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
findInfo = re.compile(r'<span class="inq">(.*)</span>')  # 找到概况
findBD = re.compile(r'<p class="">(.*?)</p>', re.S)  # 找到导演主演


# 爬取网页
def getData(baseurl):
    datalist = []
    # 解析数据
    for i in range(0, 10):  # 直接爬取10页数据
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        k = 1
        print('正在爬取{}页：'.format(i) + url)
        for item in soup.find_all('div', class_="item"):
            # print(item)
            data = []  # 保存一部电影的信息
            item = str(item)
            Link = re.findall(findLink, item)[0]  # 影片详情链接
            data.append(Link)
            Img = re.findall(findImgSrc, item)[0]  # 影片的图片链接
            data.append(Img)
            Names = re.findall(findName, item)  # 影片片名
            if (len(Names) == 2):
                cName = Names[0]  # 添加中文名
                data.append(cName)
                oName = Names[1].replace("\\", "")  # 去掉无关的符号
                oName = re.sub('/', "", oName)  # 去掉/
                data.append(oName)  # 添加外国名
            else:
                data.append(Names[0])
                data.append(' ')  # 留空

            Rating = re.findall(findRating, item)[0]  # 影片评分
            data.append(Rating)
            PeopleNumber = re.findall(findPeopleNumber, item)[0]  # 影片评价人数
            data.append(PeopleNumber)
            Info = re.findall(findInfo, item)  # 影片详细信息
            if len(Info) != 0:
                Info = Info[0].replace("。", "")
                data.append(Info)
            else:
                data.append(" ")

            BD = re.findall(findBD, item)[0]  # 找到主演信息
            BD = re.sub('<br(\s+)?/>(\s+)?', "", BD)  # 去掉br
            BD = re.sub('/', "", BD)  # 去掉/
            BD = re.sub('/n', "", BD)  # 去掉/n
            BD = re.sub(' ', "", BD)  # 去掉/
            data.append(BD)
            datalist.append(data)
            k += 1
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
    # 用户代理
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(datalist, savapath):
    print("爬取中······")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情连接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d部电影：" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savapath)


def download(datalist):  # 下载图片
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
    i = 1
    for data in datalist:
        save_path = 'D:\python爬取写入文件\%s.jpg' % (data[2])
        request = urllib.request.Request(data[1], headers=head)
        f = urllib.request.urlopen(request)
        with open(save_path, "wb") as code:
            code.write(f.read())
        print("开始下载第%d图片：" % i)
        i += 1


if __name__ == '__main__':
    main()
