import json
import random
import re
from io import BytesIO
from time import sleep

import requests
from lxml import etree
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from svglib.svglib import svg2rlg

opt = webdriver.ChromeOptions()
# opt.add_argument("--disable-blink-features")
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"')

browser = webdriver.Chrome(r'D:\Chromedriver\Chromedriver.exe', chrome_options=opt)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

url = 'https://search.zxxk.com'

browser.get(url)

sleep(3)
with open('cookie.json', 'r') as f:
    cookies = json.load(f)

for cookie in cookies:
    browser.add_cookie(cookie)
browser.refresh()  # 刷新网页
sleep(2)


def main():
    for grade in range(1, 4):
        # 获取每个年级页面的页数
        page_url = f'https://search.zxxk.com/books/p-channel10-type901-g{grade}/index-1.html'
        get_page = requests.get(page_url, headers=header).content.decode('utf-8')
        tree = etree.HTML(get_page)
        # 拿到每个年级的页数
        pages = tree.xpath('/html/body/div[2]/div[3]/div/div[4]/span[1]/text()')
        pages = ''.join(pages)
        # 正则表达式匹配数字
        get_num = re.findall(r'\d+', pages)[0]
        for page in range(1, int(get_num) + 1):  # 遍历页数，例如：第一页
            # 每个年级对于每个页数
            a_urls = f'https://search.zxxk.com/books/p-channel10-type901-g3/index-{page}.html'
            print('页数为:', page)
            # print('现在爬取的网页是:',a_urls)
            get_div_a = requests.get(a_urls, headers=header).content.decode('utf-8')
            trees = etree.HTML(get_div_a)
            div_list = trees.xpath('//*[@class="list-cont"]/div')  # 页面中类名list-cont下的每个div
            for info_a in range(1, len(div_list) + 1):
                a = trees.xpath(f'//*[@class="list-cont"]/div[{info_a}]/div[1]/a/@href')[0]  # 拿到每个div中的a标签

                sleep(2* random.random())
                title = trees.xpath(f'//*[@class="list-cont"]/div[{info_a}]/div[2]/div[2]/div[1]/a/@title')[
                    0]  # 获取a标签内的标题

                print(title)
                # print(browser.get_cookies())            #获取网页cookie信息
                # browser.add_cookie(cookie_dict)
                browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
                })
                browser.get(a)

                try:
                    img = browser.find_element(By.XPATH,
                                               '//*[@class="multiple-date-preview-file"]/div[1]/img').get_attribute(
                        'data-original')  # 获取svg图片的路径
                    response = requests.get(img)  # 获取图片的链接
                    try:
                        with open(f'svg\\{title}.svg', 'wb') as f:
                            f.write(response.content)
                        fonts = [('SimSun', 'SimSun.ttf'), ('DengXian', 'DengXian.ttf'), ('SimHei', 'SimHei.ttf'),
                                 ('Wingdings', 'Wingdings.ttf'), ('Wingdings 2', 'Wingdings2.ttf')]

                        for font in fonts:
                            try:
                                pdfmetrics.registerFont(TTFont(font[0], font[1]))
                                break
                            except Exception as e:
                                print('字体处出现异常:', e)
                                continue
                        drawing = svg2rlg(f'svg\\{title}.svg')

                        pdf_buffer = BytesIO()
                        renderPDF.drawToFile(drawing, pdf_buffer)

                        with open(f'pdf\\{title}.pdf', 'wb') as f:
                            f.write(pdf_buffer.getvalue())

                        # try:
                        #
                        #     print(img)
                        # except Exception as e:
                        #     print('程序错误,没有该节点：', e)
                        # save_image_to_pdf('1.jpg', 'output.pdf')

                    except Exception as e:
                        print('写入svg文件报错：', e)
                except Exception as e:
                    print('元素节点找不到:', e)


if __name__ == '__main__':
    main()
    browser.quit()
    a = 1
