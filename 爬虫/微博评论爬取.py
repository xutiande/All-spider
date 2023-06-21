
"""简单微博爬虫，需要自行扫码登录"""
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
opt=webdriver.ChromeOptions()
url='https://weibo.com/'
browser =webdriver.Chrome()
def weibo():
    weibo_html='https://weibo.com/7467277921/LxGmUbo7d#comment'
    browser.get(weibo_html)
    time.sleep(5)
    username=browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[1]/div/a[1]').click()
    time.sleep(20)
    title = browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/main/div/div/div[2]/article/div[2]/div/div[1]/div').text
    txt_comments=set()
    with open('weibo_comments.txt', 'w', encoding='gb18030') as f:
        for speed in range(20):
            browser.execute_script("window.scrollBy(0,{})".format(3*random.randint(50,100)))
            sleep(3*random.random())
            div_comments=browser.find_elements(By.XPATH,"//div[@class='vue-recycle-scroller__item-wrapper']/div")
            dit_list=len(div_comments)
            for txt in range(dit_list):
                comments=browser.find_element(By.XPATH,'//*[@id="scroller"]/div[1]/div[{}]/div/div/div/div[1]/div[2]/div[1]/span'.format(txt+1)) .text
                txt_comments.add(comments)
        print(txt_comments)
        f.write(''.join(txt_comments))
        f.write('\n')


if __name__=="__main__":
    weibo()

