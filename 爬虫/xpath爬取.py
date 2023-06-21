import requests
from lxml import etree
for i in range(10):
    url = "https://ssr1.scrape.center/detail/{}".format(i+1)  #每次循环{}+1
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
    text_page = requests.get(url,headers=headers).text  #获取网页请求
    tree = etree.HTML(text_page) #解析
    div=tree.xpath('//*[@id="detail"]/div[1]/div/div/div[1]')[0]        #确定一个范围
    get_h2=div.xpath('div/div[2]/a/h2/text()')[0]       #提取标题
    get_p=div.xpath('div/div[3]/p[1]/text()')[0]        #提取他的评分
    get_span=div.xpath('div/div[2]/div[2]/span/text()')[0:3]    #提取他的地址与时长
    get_span_str=''.join(get_span)
    get_text=div.xpath('div/div[2]/div[4]/p/text()')[0] #提取影片介绍
    get_img=div.xpath('div/div[1]/a/img/@src')[0]       #提取图片
    f=open(r'D:\wyw.txt','a',encoding='utf-8')  #写入文本
    f.write('\n'+get_h2)
    f.write(get_p+'\n')
    f.write(get_span_str+'\n')
    f.write(get_text.replace('\n','')+'\n')
    f.close()
    jpg=open(r'D:\{}.jpg'.format(i),'wb')  #写入图片
    jpg.write(requests.get(get_img).content)