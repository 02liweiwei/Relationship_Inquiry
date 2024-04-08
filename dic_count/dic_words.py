# 方法二：分词识别人名
import jieba
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts
import matplotlib.pyplot as plt

# 排除的非人词语
excludes = {"什么","一个","我们","那里","如今","你们","说道","起来",
            "姑娘","这里","出来","他们","众人","奶奶","自己","一面",
            "太太","只见","怎么","两个","没有","不是","不知","这个",
            "知道","听见","这样","进来","告诉","东西","咱们","就是",
            "回来","大家","只是","老爷","只得","丫头","这些","不敢",
            "出去","所以","不过","不好","姐姐","的话","过来","不能","心里","一时","二爷","今日","这么","银子","答应","几个",
            "还有","屋里","只管","二人","一回","说话","那边","如此","外头","打发","自然","这话",
            "那些","小丫头","问道","人家","罢了","看见","今儿","妹妹","不用","媳妇","如何","听说","原来",
            "家里","到底","这会子","一声","一句","别人","进去","不得","还是","老爷"}
name = ['贾宝玉','贾母','林黛玉','薛宝钗','史湘云', '王熙凤', '巧姐', '王夫人',
                  '邢夫人', '薛姨妈', '尤氏', '贾元春', '贾迎春', '贾探春','贾惜春','秦可卿',
                  '尤二姐', '尤三姐', '李纨','妙玉','紫鹃','袭人','晴雯','麝月','茗烟','刑岫烟','平儿',
                 '鸳鸯','玉钏儿','金钏儿','赵姨娘','周瑞家的','林之孝家的','小红','坠儿','芳官','龄官','藕官','翠缕',
                 '夏金桂','宝蟾','香菱','甄士隐','甄宝玉','冷子兴','智能儿','娇杏','贾琏','贾政',
                 '贾雨村','贾珍','薛蟠','薛蟠','薛蝌','贾蓉','贾蔷','贾瑞','贾芸','贾敬','贾赫',
                  '秦钟','蒋玉菡','柳湘莲','焦大','贾环','贾兰','刘姥姥','空空道人','癞头和尚']
txt = open("C:\\Users\\HW\\Desktop\\人物关系系统\\关系系统2.0\\gettext】\\红楼梦.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt) #对文本分词
jieba.add_word('宝二爷')#防止被切开
jieba.add_word('凤辣子')
jieba.add_word('凤哥儿')
jieba.add_word('凤丫头')
jieba.add_word('二太太')
jieba.add_word('林妹妹')
jieba.add_word('林姑娘')
jieba.add_word('琏二爷')
jieba.add_word('宝丫头')
jieba.add_word('宝姑娘')
jieba.add_word('宝姐姐')
jieba.add_word('平姐姐')
jieba.add_word('平姑娘')
jieba.add_word('薛夫人')
jieba.add_word('姨太太')
jieba.add_word('英莲')
#
counts = {}
for word in words:
    if len(word) == 1:#词长度为1.直接下一个词
        continue
    elif word == '宝玉' or word == '宝二爷' or word == '宝兄弟' or word == '怡红公子' or word == '二哥哥' or word == '天魔星':
        rword = '贾宝玉'
    elif word == '凤姐' or word == '凤姐儿' or word == '凤丫头' or word == '凤哥儿' or word == '凤辣子' or word == '熙凤' or word == '琏二奶奶':
        rword = '王熙凤'
    elif word == '老太太' or word == '老祖宗' or word == '史太君' :
        rword = '贾母'
    elif word == '宝钗' or word == '宝姐姐' or word == '宝姑娘' or word== '宝丫头' or word == '蘅芜君':
        rword = '薛宝钗'
    elif word == '贵妃' or word =='元妃' or word =='元春':
        rword = '贾元春'
    elif word == '黛玉' or word == '林妹妹' or word == '林姑娘' or word == '潇湘妃子' or word == '颦儿':
        rword = '林黛玉'
    elif word =='二妹妹'  or word =='迎春':
        rword = '贾迎春'
    elif word == '三妹妹' or word == '探春':
        rword = '贾探春'
    elif word == '四妹妹' or word == '惜春':
        rword = '贾惜春'
    elif word == '秦氏' or word == '可儿' or word == '可卿'  :
        rword = '秦可卿'
    elif word == ' 李宫裁':
        rword = '李纨'
    elif word == '二太太':
        rword = '王夫人'
    elif word == '琏二爷':
        rword = '贾琏'
    elif word == '平姐姐' or word == '平姑娘':
        rword = '平儿'
    elif word == '薛夫人' or word == '姨太太':
        rword = '薛姨妈'
    elif word =='英莲' or word == '香菱':
        rword = '英莲'
    elif word == '道士' or word == '道人':
        rword = '空空道人'
    elif word == '僧道'  or word=='那僧笑':
        rword = '癞头和尚'
    elif word == '湘云':
        rword = '史湘云'
    elif word == '甄士隐':
        rword = '甄士隐'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del (counts[word])  # 删除非人名词的词语

items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
s=set()

for j in name:
        s.add(j)
print(s)

f=open("renwu2.txt","w")#写入文件
relationships={}

for i in range(2000):
    word, count = items[i]
    if word not in s:
        # print(counts[word])
        del(counts[word])
    else:
        print("{0:<10}{1:>5}".format(word,count))
        f.writelines("{0:<10}{1:>5}\n".format(word, count))
        relationships[word] = {}
f.close()



import csv

header = ['id', 'name', 'weight']
data = [['贾宝玉','贾宝玉',3938],
['贾母','贾母',287],['王熙凤','王熙凤',1662],['王夫人','王夫人',988],['林黛玉','林黛玉', 939],
['薛宝钗','薛宝钗',693],['贾琏','贾琏',664],['平儿','平儿',612],['袭人','袭人',583],
['薛姨妈','薛姨妈',556],['贾探春','贾探春',439],['鸳鸯','鸳鸯',426],['史湘云','史湘云',416],
['贾政','贾政',341],['晴雯','晴雯',338],['邢夫人','邢夫人',281],['贾珍','贾珍',278],
['紫鹃','紫鹃',277],['尤氏 ','尤氏 ',223],['薛蟠 ','薛蟠 ',194],
['贾蓉','贾蓉',150],['贾芸','贾芸',147],['贾迎春','贾迎春',145],['赵姨娘','赵姨娘',135],
['芳官 ','芳官 ',95],['尤二姐','尤二姐',91],[' 贾环',' 贾环',87],['秦钟 ','秦钟 ',82],
['妙玉','妙玉',81]
]

with open('name_node.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)

header = ['source', 'target', 'weight']
data = [['甄士隐','贾雨村',242],['贾母','王夫人',108], ['贾母','薛姨妈',102],
        ['贾母','贾政',99], ['王夫人','贾政',97],
        ['王夫人','袭人',95], ['贾政','贾敬',92], ['王夫人','邢夫人',89], ['王夫人','薛姨妈',89],
        ['贾母','袭人',82], ['袭人','晴雯',76], ['贾母','鸳鸯',75], ['袭人','麝月',70],
        ['贾母','邢夫人',69], ['冷子兴','贾政',68], ['王夫人','李纨',67], ['贾母','李纨',66],
        ['贾母','贾琏',65], ['贾珍','贾蓉',64], ['薛姨妈','薛蟠',60],
        ['王夫人','贾琏',60], ['贾琏','贾政',57], ['平儿','贾琏',55],
        ['王夫人','鸳鸯',54], ['晴雯','麝月',53], ['贾母','尤氏',51], ['王夫人','尤氏',50],
        ['袭人','平儿',49],['贾母','贾珍',47],['尤氏','贾珍',45],['王夫人','平儿',43], ['贾琏','贾珍',43],
        ['李纨','平儿',43],
        ['贾政','贾珍',40],
        ['尤氏','贾蓉',37],
        ['贾母','平儿',36],
        ['邢夫人','尤氏',35],
        ['贾琏','贾蓉',35],
        ['贾母','贾蓉',35],
        ]



with open('name_relationship.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)






