import time

import pymysql
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By

class Spider_database:
    def __init__(self):
        '''
        创建数据库
        '''
        self.mydb =  pymysql.connect(host='127.0.0.1', user='root', password='123456', db='jd', charset='utf8')
        self.mycursor = self.mydb.cursor()  # 游标
        self.mycursor.execute("CREATE DATABASE if not exists test")  # 创建名为test的数据库
        '''
        创建表
        '''
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='jd', charset='utf8')
        self.cursor = self.db.cursor()
        # 如果存在table2表，则删除
        self.cursor.execute("DROP TABLE IF EXISTS table2")
        # 创建table2表
        crea_table = ''' 
        create table table2( 
            book varchar(150),
            jiage varchar(150),
            xiangxi varchar(150),
            title varchar(150),
            img varchar(150))'''
        try:
            # 执行SQL语句
            self.cursor.execute(crea_table)
            print("创建数据表成功")
        except Exception as e:
            print("创建数据表失败：case%s" % e)
        finally:
            self.cursor.close() # 关闭游标连接
            self.db.close()# 关闭数据库连接
    def get_html(self,url):
        for i in range(10):
            db1 = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='jd', charset='utf8')     #mysql用户名密码
            cursor1 = db1.cursor()
            get_jiage = url.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[{}]/div/div[2]/strong/i'.format(i+1)).text  # 提取价格
            get_jieshao = url.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/a/em'.format(i+1)).text  # 提取商品介绍
            get_title = url.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[{}]/div/div[5]/span/a'.format(i+1)).text  # 提取店铺
            get_img = url.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[{}]/div/div[1]/a/img'.format(i+1)).get_attribute('src')  # 提取图片
            with open(r'D:\爬虫图片放置文件\{}.txt'.format(get_name),'a',encoding='utf-8')as f:     #写入文件夹以搜索条件命名
                f.write('{}{}{}{}{}{}{}{}'.format(get_jiage,'\n',get_jieshao,'\n',get_title,'\n','图片地址：',get_img))
            insert1 = "insert into table2(book,jiage,xiangxi,title,img)\
                VALUES('%s','%s','%s', '%s','%s')" % (get_name,get_jiage, get_jieshao, get_title, get_img)  #数据插入到mysql的table2表中
            try:
                # 执行sql语句
                cursor1.execute(insert1)
                # 执行sql语句
                db1.commit()
            except:
                # 发生错误时回滚
                db1.rollback()

            # 关闭游标和数据库
            cursor1.close()
            db1.close()
if __name__ == '__main__':
    s = Spider_database()
    n=input('请输入搜索次数：')
    url = webdriver.Chrome()
    while n != '10':
        get_name = input('请输入你想搜索的内容:')       #例如python
        url.get('https://search.jd.com/Search?keyword='+ urllib.parse.quote(get_name))  #搜索条件
        time.sleep(30)
        s.get_html(url)




