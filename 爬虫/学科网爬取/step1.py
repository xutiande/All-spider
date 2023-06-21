import json
import re
import requests
from lxml import etree
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

opt = webdriver.ChromeOptions()
# opt.add_argument("--disable-blink-features")
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"')

browser = webdriver.Chrome(r'D:\Chromedriver\Chromedriver.exe', chrome_options=opt)
cookie = {
    'Cookie': 'uuid_tt_dd=10_30288206980-1676118544588-804369; UserName=y662225dd; UserInfo=4f0bf672bd2a440baff8fa22065a6b6e; UserToken=4f0bf672bd2a440baff8fa22065a6b6e; UserNick=y662225dd; AU=8A7; UN=y662225dd; BT=1676206654004; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"islogin":{"value":"1","scope":1},"isonline":{"value":"1","scope":1},"isvip":{"value":"0","scope":1},"uid_":{"value":"y662225dd","scope":1}}; __bid_n=18648fe68b4278e24d4207; __gads=ID=37fc3a1d96919139-22fea122bbd90043:T=1676261878:RT=1676261878:S=ALNI_MbF9Sb2bCmjzoFpUVlFv2DuWm9D2g; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30288206980-1676118544588-804369!5744*1*y662225dd; FPTOKEN=1+Jn1/iiCz7a+tAQ3fPCjHQrHJXgeVKzSwsmQg+m6nVPh8sDcJhDLR/xehYAR2LgEUvYj1TCiv47rjeN2oJitqovjMgab7vyENyHPk0YjDG22zF2TlSR78thx24gn6cWibFtcr2iun3d7vQ9Jh9L6RXDgO9w19I/V00noIa2HSMpj4zILT7tMZsoCnWZGtXZsnLIgO4G69zVyZEitNo7tRiRg8G6fh+ci/jGPE9zU2IRl854B/E6oPIOmOLrpoFzYzg2IgMB+Ucz7yvtrjj+k/jPnTary1b3ja2KtvAvNcyrQsdD4IkmV1aAQ5g7Y6nKrHsiGdEuJuI8ZY1q/AWkVlLNFvjkMZfl/zhoFmUYRckIjiI+Yw3XbdsCHvN8AXfOTFppRFVUXpX1O95Hne5dvw==|+oY0CeJnrvWSiWYtzbbsdr9hvDIyVDgkNjf2zVG2X48=|10|4ebd61b45a10c014c8541e9d44c37caa; __gpi=UID=00000bc0c01f9adc:T=1676261878:RT=1680055420:S=ALNI_MZgmFoWzSQNdRO-kQcpnoHucEGmmg; c_adb=1; c_dl_prid=-; c_dl_rid=1680436067468_195585; c_dl_fref=https://blog.csdn.net/qq_46534950/article/details/107234428; c_dl_fpage=/download/qq_67180497/84298830; c_dl_um=-; ssxmod_itna=Yq+xuDyD07ujDXDniGeG=DCYGCWgQtG8KnIQjDBwie4iNDnD8x7YDvGmpRWGKWKYSq+W4rcgyfN3F=iRGWHmY3PuzqGDB3DEx06KF04YYkDt4DTD34DYDixib1xi5GRD0KDFF5XUZ9Dm4GWFqGfDDoDY86RDitD4qDBGOdDKqGgFq267mt3puDeoGGcD0tdxBdrtahcGeaaaiNexanDTEQDzqHDtutS9Ld3x0PyBMUDZr+WC4+LRD4ftGGimGxEGB+dBGwtm4pbKYeqBYmzfBlIxDfv894xD; ssxmod_itna2=Yq+xuDyD07ujDXDniGeG=DCYGCWgQtG8KnIQD8qpiS4GXFPGaQmimOs5mrBmP1=TRt4343dwYCDxn+emyQl+gPpQopr9p6U7IiKTiBRBb3BxNuYrexHe0=LAdpA2Z3LhBYCp1iF4M24=eZ4xZZeGUQ0Qd+uz=3YKUpIwU1xCaIpbbfmxa/Iz5ZF+wfP5UhqtKAY=aSgpoUorM1ENb/mvoSOCSYTAzRnAx49APSkpu0nj5gp116TCenenBC80o5gz3vpTktadGp2Rt6T7Sh4DwOeDLxG73YD=; firstDie=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1681896150,1681978394,1682045497,1682083528; dc_session_id=10_1682129120948.729130; c_first_ref=www.bing.com; c_first_page=https://blog.csdn.net/fei347795790/article/details/120143334; c_dsid=11_1682129121375.412411; c_segment=1; dc_sid=4955b8c1465031a7fc1144dbc20f335b; c_pref=https://www.bing.com/; c_ref=https://blog.csdn.net/fei347795790/article/details/120143334; log_Id_click=640; c_page_id=default; log_Id_pv=1108; dc_tos=rthv7l; log_Id_view=4764'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}


url = 'https://search.zxxk.com'
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

browser.get(url)
browser.find_element(By.XPATH,'//*[@id="un-login"]/a[1]').click()
sleep(20)
with open('cookie.json', 'w', encoding='UTF-8')as f:
    json.dump(browser.get_cookies(),f)
#
# a_urls = f'https://search.zxxk.com/books/p-channel10-type901-g1/?free=1&kw=科学'  # 每个年级对于每个页数
# get_div_a = requests.get(a_urls, headers=header,cookies=cookie).content.decode('utf-8')
# tree = etree.HTML(get_div_a)
# div_a = tree.xpath('//*[@class="list-cont"]/div')
# for info_a in range(1, len(div_a) + 1):
#     a = tree.xpath(f'//*[@class="list-cont"]/div[{info_a}]/div[1]/a/@href')[0]
#     browser.get(a)
#
#
#     browser.find_element(By.XPATH, '//*[@id="btnSoftDownload"]/div').click()
#     sleep(random.randint(1,5)*random.random())
#     try:
#         browser.find_element(By.XPATH, '/html/body/div[10]/div[2]/div[3]/div[2]/a').click()
#     except Exception as e:
#         print('程序错误,没有该节点：',e)
#     sleep(random.randint(1,5)*random.random())
browser.quit()
