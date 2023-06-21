import re


src="""

窗外的麻雀在电线杆上多嘴

你说这一句很有夏天的感觉

手中的铅笔在纸上来来回回

我用几行字形容你是我的谁

秋刀鱼的滋味猫跟你都想了解

初恋的香味就这样被我们寻回

那温暖的阳光像刚摘的新鲜草莓

你说你舍不得吃掉这一种感觉

雨下整夜我的爱溢出就像雨水

院子落叶跟我的思念厚厚一叠

几句是非也无法将我的热情冷却

你出现在我诗的每一页

雨下整夜我的爱溢出就像雨水

窗台蝴蝶像诗里纷飞的美丽章节

我接着写把永远爱你写进诗的结尾

你是我唯一想要的了解

那饱满的稻穗幸福了这个季节

而你的脸颊像田里熟透的蕃茄

你突然对我说七里香的名字很美

我此刻却只想亲吻你倔强的嘴

"""
src=re.sub(re.compile("\n+"),"\n",src)
src=src.strip()
# print(src)
with open("xtd.txt", "w", encoding='utf-8') as f:
    f.write(src)
    f.close()
with open("xtd.txt", "r", encoding='utf-8') as f1:
    a=f1.read()
    print(a)