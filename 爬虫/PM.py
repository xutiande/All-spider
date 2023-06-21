import random
year=2015
month1=2
month2=7
day=0
hour=0
for i in range(24):         #2月
    hour=i
    for j in range(30):
        PM = random.randint(10, 55)
        day=j+1
        # print(year, ',', month1, ',', day, ',', hour, ',', PM)
        with open(r"D:\python爬取写入文件\CaotangPM2.txt",'a')as f:
            f.write("{}{}{}{}{}{}{}{}{}{}".format(year, ',', month1, ',', day, ',', hour, ',', PM,'\n'))
for i in range(24):         #7月
    hour=i
    for j in range(30):
        PM = random.randint(10, 55)
        day=j+1
        # print(year, ',', month2, ',', day, ',', hour, ',', PM)
        with open(r"D:\python爬取写入文件\CaotangPM7.txt",'a')as f:
            f.write("{}{}{}{}{}{}{}{}{}{}".format(year, ',', month2, ',', day, ',', hour, ',', PM,'\n'))