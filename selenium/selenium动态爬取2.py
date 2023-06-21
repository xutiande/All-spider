import time

from selenium import webdriver
from selenium.webdriver.common.by import By

html = 'https://spa1.scrape.center/'
s=2
num = 0
i = 0
n = 1
def xtd(html):
    global i
    global n
    global num
    global s
    browser = webdriver.Chrome('chromedriver')
    browser.get(html)
    browser.implicitly_wait(10)  # 等待时长最多不超过10秒
    a=1
    for i in range(10):
        i+=1
        buttons = browser.find_elements(By.XPATH, '//*[@id="index"]/div[1]/div/div[{}]/div/div/div[1]/a'.format(i))
        button = buttons[0]
        button.click()
        browser.implicitly_wait(10)
        # browser.switch_to.window(browser.window_handles[-1])  # 与最后访问的页面切换
        bt = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div/div/div[2]/a/h2').text  # 获取电影名称
        pf = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[3]/p[1]').text  # 获取电影评分
        dz = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[2]').text  # 获取电影地址
        js = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p').text  # 获取电影介绍
        tp = browser.find_element(By.XPATH, '//*[@id="detail"]/div[1]/div/div/div[1]/div/div[1]/a/img').get_attribute('src')  # 通过get_attribute获取img节点中的src
        print(bt)
        print(pf)
        print(dz)
        print(js)
        print(tp)
        while i>=10:
            browser.back()
            browser.find_element(By.XPATH,'//*[@id="index"]/div[2]/div/div/div/button[2]').click()
            time.sleep(2)
            for j in range(10):
                try:
                    j += 1
                    buttons1 = browser.find_elements(By.XPATH,'//*[@id="index"]/div[1]/div/div[{}]/div/div/div[{}]/a'.format(j,s))
                    button1 = buttons1[0]
                    button1.click()
                    browser.implicitly_wait(10)
                    bt1 = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div/div/div[2]/a/h2').text  # 获取电影名称
                    pf1 = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[3]/p[1]').text  # 获取电影评分
                    dz1 = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[2]').text  # 获取电影地址
                    js1 = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p').text  # 获取电影介绍
                    tp1 = browser.find_element(By.XPATH,'//*[@id="detail"]/div[1]/div/div/div[1]/div/div[1]/a/img').get_attribute('src')
                    print(bt1)
                    print(pf1)
                    print(dz1)
                    print(js1)
                    print(tp1)
                    browser.back()
                except:
                    print('失败')
        else:
            browser.back()
    browser.close()
xtd(html)
