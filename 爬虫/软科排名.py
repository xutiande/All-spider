"""获取所需的使用url地址"""
import csv
import os.path
from time import sleep
import random
import json
import io
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 改变标准输出的默认编码为gb18030
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 配置Chrome浏览器选项
opt = ChromeOptions()
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-web-security')
opt.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')  # 添加请求头

url = 'https://www.shanghairanking.cn/rankings/arwu/2003'  # 网址链接

# 使用Chrome浏览器启动Webdriver，并应用上述设置
browser = webdriver.Chrome(r'D:\Chromedriver\chromedriver_16.exe', options=opt)

# 禁用webdriver检测
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)

url_list = []

# 读取url地址列表
with open('软科排名url地址.csv', 'r', encoding='gb18030') as f:
    url_list.append(f.readlines())

urls = url_list[0][1:]  # 提取URL地址列表的内容，去除第一行标题
every_url_page = []

# 遍历URL地址列表
for i in urls:
    top_list = []
    school_list = []
    country_list = []
    score_list = []

    sleep(random.random())

    url = i.strip()  # 去除URL地址两端的空格
    browser.get(url)  # 打开URL对应的网页

    # 创建文件夹
    folder_path = r'软科排名\{}'.format(browser.current_url[-4:])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 创建文件
    file_path = os.path.join(folder_path, '{}.csv'.format(browser.current_url[-4:]))
    f = open(file_path, 'w', encoding='gb18030', newline='')
    filename = ['排名', '学校', '国家', '评分']
    f_csv = csv.DictWriter(f, fieldnames=filename)
    f_csv.writeheader()

    # 获取页数
    url_page_count = browser.find_element(By.XPATH, '//*[@id="content-box"]/ul/li[8]/a').text

    # 循环翻页
    for pages in range(int(url_page_count) - 1):
        browser.implicitly_wait(random.randint(5, 8))

        # 获取数据行
        div_list = browser.find_elements(By.XPATH, '//*[@id="content-box"]/div[2]/table/tbody/tr')

        # 遍历每一行数据
        for tr in range(1, len(div_list) + 1):
            # 获取排名
            top = browser.find_element(By.XPATH,
                                       f'//*[@id="content-box"]/div[2]/table/tbody/tr[{tr}]/td[1]/div').text
            top_list.append(top)

            try:
                # 获取学校
                school = browser.find_element(By.XPATH,
                                              f'//*[@id="content-box"]/div[2]/table/tbody/tr[{tr}]/td[2]/div/div[2]/div/span').text
                school_list.append(school)
            except Exception as e:
                # 获取学校（备选路径）
                school = browser.find_element(By.XPATH,
                                              f'//*[@id="content-box"]/div[2]/table/tbody/tr[{tr}]/td[2]/div/div[2]/div[1]/div/div/a').text
                school_list.append(school)

            # 获取国家
            country = browser.find_element(By.XPATH,
                                           f'//*[@id="content-box"]/div[2]/table/tbody/tr[{tr}]/td[3]').text
            country_list.append(country)

            # 获取评分
            score = browser.find_element(By.XPATH,
                                         f'//*[@id="content-box"]/div[2]/table/tbody/tr[{tr}]/td[5]').text
            score_list.append(score)

        browser.implicitly_wait(random.randint(5, 15))

        # 点击下一页按钮
        next_page = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class=' ant-pagination-next']")))
        browser.execute_script("arguments[0].click();", next_page)

    # 将数据写入CSV文件
    for info in range(len(top_list)):
        try:
            f_csv.writerow({
                '排名': top_list[info],
                '学校': school_list[info],
                '国家': country_list[info],
                '评分': score_list[info]
            })
        except Exception as e:
            pass

browser.quit()  # 关闭浏览器
f.close()  # 关闭文件
