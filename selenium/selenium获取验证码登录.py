import time
import re
import tesserocr
from selenium import webdriver
from io import BytesIO
from PIL import Image
from retrying import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import numpy as np
from zh_and_mm import zh,mm



def preprocess(image):
    image = image.convert('L')
    array = np.array(image)
    array = np.array(image)
    array = np.where(array > 50, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    return image


@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    browser.get('http://cas.gxcme.edu.cn/cas/login?service=http://portal.gxcme.edu.cn/sso/home')        #打开网址
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#wx_login_div').click()      #点击切换到账号登录
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,'#username').send_keys(zh)         #输入账号
    browser.find_element(By.CSS_SELECTOR,'#password').send_keys(mm)         #输入密码
    captcha = browser.find_element(By.CSS_SELECTOR,'#captcha_img')          #获取验证码信息
    image = Image.open(BytesIO(captcha.screenshot_as_png))          #打包为png文件
    # image = preprocess(image)
    captcha = tesserocr.image_to_text(image)                #图片转换为文本
    print(captcha)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)               #正则表达式提取
    browser.find_element(By.CSS_SELECTOR,'#captcha').send_keys(captcha)         #输入框输入提取出来的验证码
    browser.find_element(By.CSS_SELECTOR,'#submit_btn').click()       #点击登录
    time.sleep(5)
    a=1
    # try:
    #     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="app"]/div/div[1]/div[1]/div[6]/div/div/span/span[1]')))
    #     time.sleep(10)
    #     browser.close()
    #     return True
    # except TimeoutException:
    #     return False


if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()