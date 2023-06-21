"""
运行程序需要谷歌浏览器与谷歌驱动，两者的版本也要对应
"""
import csv
import random
from time import sleep

from lxml import etree
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = ChromeOptions()

opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-web-security')
# opt.add_argument("--headless")
opt.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57')  # 添加请求头
url = 'https://kuwo.cn/rankList'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
browser = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)
browsers = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)
browsers.execute_script(script)
browser.get(url)

number_list = []
title_list = []
singer_list = []
album_list = []
duration_list = []
publish_time_list = []
comment_list = []

# 循环翻页
for page in range(11):
    sleep(3 * random.random())

    # 等待下一页按钮可点击
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[4]/i[2]'))
    )

    # 点击下一页按钮
    browser.execute_script("arguments[0].click();", next_button)

    # 等待页面加载完成
    WebDriverWait(browser, 10).until(EC.url_to_be("https://kuwo.cn/rankList"))

    # 判断是否到达最后一页
    current_url = browser.current_url
    if current_url != "https://kuwo.cn/rankList":
        break

    # page_a = browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[4]/i[2]')
    # browser.execute_script("arguments[0].click();", page_a)
    # print(browser.page_source)
    tree = etree.HTML(browser.page_source)  # 解析
    ul_list = tree.xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li')
    for i in range(1, len(ul_list) + 1):

        browser.implicitly_wait(random.randint(2, 5))
        title = \
            tree.xpath(
                f'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li[{i}]/div[2]/a/text()')[
                0]  #
        title_list.append(title)
        singer = tree.xpath(
            f'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li[{i}]/div[3]/span/text()')[
            0]  # 歌手
        singer_list.append(singer)
        try:
            album = tree.xpath(
                f'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li[{i}]/div[4]/span/text()')[
                0]  # 专辑
            album_list.append(album)
        except Exception as e:
            album_list.append('None')
        duration = tree.xpath(
            f'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li[{i}]/div[5]/span/text()')[
            0]  # 时长
        duration_list.append(duration)

        """二级页面信息获取"""
        two_href = \
            tree.xpath(
                f'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/ul/li[{i}]/div[2]/a/@href')[
                0]  # 二级页面地址
        two_url = 'https://kuwo.cn' + two_href

        # print(two_url)
        browsers.get(two_url)
        for scroll in range(random.randint(2, 4)):  # 向下滚动5次
            # 将页面向下滚动100个像素
            browsers.execute_script("window.scrollBy(0, 400);")
            # 等待0.5秒，模拟滚动的时间间隔
            sleep(random.random())
        browser.implicitly_wait(random.randint(1, 5))
        browsers.refresh()

        # 解析二级页面内容
        two_tree = etree.HTML(browsers.page_source)

        try:
            publish_time = two_tree.xpath('//*[@id="__layout"]/div/div[2]/div/div[1]/div[2]/div[1]/p[3]/span[6]/text()')[0]
            publish_time_list.append(publish_time)
            comment = two_tree.xpath('//*[@id="comment_con"]/section[2]/div[1]/span/text()')[0]
            # print(comment)
            comment_list.append(comment)
        except:
            comment_list.append('None')

with open('../练习/music_data.csv', 'w', encoding='gb18030', newline="") as f:
    filename = ['序号', '歌曲名称', '歌手', '专辑', '时长', '发布时间', '评论数']
    f_csv = csv.DictWriter(f, fieldnames=filename)
    f_csv.writeheader()
    for info in range(len(title_list)):
        try:
            f_csv.writerow({
                '序号': info,
                '歌曲名称': title_list[info],
                '歌手': singer_list[info],
                '专辑': album_list[info],
                '时长': duration_list[info],
                '发布时间': publish_time_list[info],
                '评论数': comment_list[info]
            })
        except Exception as e:
            print(e)
# 关闭 WebDriver
browser.quit()
browsers.quit()