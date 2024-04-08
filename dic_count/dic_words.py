# ���������ִ�ʶ������
import jieba
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts
import matplotlib.pyplot as plt

# �ų��ķ��˴���
excludes = {"ʲô","һ��","����","����","���","����","˵��","����",
            "����","����","����","����","����","����","�Լ�","һ��",
            "̫̫","ֻ��","��ô","����","û��","����","��֪","���",
            "֪��","����","����","����","����","����","����","����",
            "����","���","ֻ��","��ү","ֻ��","Ѿͷ","��Щ","����",
            "��ȥ","����","����","����","���","�Ļ�","����","����","����","һʱ","��ү","����","��ô","����","��Ӧ","����",
            "����","����","ֻ��","����","һ��","˵��","�Ǳ�","���","��ͷ","��","��Ȼ","�⻰",
            "��Щ","СѾͷ","�ʵ�","�˼�","����","����","���","����","����","ϱ��","���","��˵","ԭ��",
            "����","����","�����","һ��","һ��","����","��ȥ","����","����","��ү"}
name = ['�ֱ���','��ĸ','������','Ѧ����','ʷ����', '������', '�ɽ�', '������',
                  '�Ϸ���', 'Ѧ����', '����', '��Ԫ��', '��ӭ��', '��̽��','��ϧ��','�ؿ���',
                  '�ȶ���', '������', '����','����','�Ͼ�','Ϯ��','����','����','����','�����','ƽ��',
                 'ԧ��','���˶�','���˶�','������','����ҵ�','��֮Т�ҵ�','С��','׹��','����','���','ź��','����',
                 '�Ľ��','���','����','��ʿ��','�籦��','������','���ܶ�','����','����','����',
                 '�����','����','Ѧ�','Ѧ�','Ѧ��','����','��Ǿ','����','��ܿ','�־�','�ֺ�',
                  '����','������','������','����','�ֻ�','����','������','�տյ���','�ͷ����']
txt = open("C:\\Users\\HW\\Desktop\\�����ϵϵͳ\\��ϵϵͳ2.0\\gettext��\\��¥��.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt) #���ı��ִ�
jieba.add_word('����ү')#��ֹ���п�
jieba.add_word('������')
jieba.add_word('����')
jieba.add_word('��Ѿͷ')
jieba.add_word('��̫̫')
jieba.add_word('������')
jieba.add_word('�ֹ���')
jieba.add_word('����ү')
jieba.add_word('��Ѿͷ')
jieba.add_word('������')
jieba.add_word('�����')
jieba.add_word('ƽ���')
jieba.add_word('ƽ����')
jieba.add_word('Ѧ����')
jieba.add_word('��̫̫')
jieba.add_word('Ӣ��')
#
counts = {}
for word in words:
    if len(word) == 1:#�ʳ���Ϊ1.ֱ����һ����
        continue
    elif word == '����' or word == '����ү' or word == '���ֵ�' or word == '���칫��' or word == '�����' or word == '��ħ��':
        rword = '�ֱ���'
    elif word == '���' or word == '����' or word == '��Ѿͷ' or word == '����' or word == '������' or word == '����' or word == '��������':
        rword = '������'
    elif word == '��̫̫' or word == '������' or word == 'ʷ̫��' :
        rword = '��ĸ'
    elif word == '����' or word == '�����' or word == '������' or word== '��Ѿͷ' or word == '޿�߾�':
        rword = 'Ѧ����'
    elif word == '����' or word =='Ԫ��' or word =='Ԫ��':
        rword = '��Ԫ��'
    elif word == '����' or word == '������' or word == '�ֹ���' or word == '��������' or word == '��':
        rword = '������'
    elif word =='������'  or word =='ӭ��':
        rword = '��ӭ��'
    elif word == '������' or word == '̽��':
        rword = '��̽��'
    elif word == '������' or word == 'ϧ��':
        rword = '��ϧ��'
    elif word == '����' or word == '�ɶ�' or word == '����'  :
        rword = '�ؿ���'
    elif word == ' ���':
        rword = '����'
    elif word == '��̫̫':
        rword = '������'
    elif word == '����ү':
        rword = '����'
    elif word == 'ƽ���' or word == 'ƽ����':
        rword = 'ƽ��'
    elif word == 'Ѧ����' or word == '��̫̫':
        rword = 'Ѧ����'
    elif word =='Ӣ��' or word == '����':
        rword = 'Ӣ��'
    elif word == '��ʿ' or word == '����':
        rword = '�տյ���'
    elif word == 'ɮ��'  or word=='��ɮЦ':
        rword = '�ͷ����'
    elif word == '����':
        rword = 'ʷ����'
    elif word == '��ʿ��':
        rword = '��ʿ��'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del (counts[word])  # ɾ���������ʵĴ���

items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
s=set()

for j in name:
        s.add(j)
print(s)

f=open("renwu2.txt","w")#д���ļ�
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
data = [['�ֱ���','�ֱ���',3938],
['��ĸ','��ĸ',287],['������','������',1662],['������','������',988],['������','������', 939],
['Ѧ����','Ѧ����',693],['����','����',664],['ƽ��','ƽ��',612],['Ϯ��','Ϯ��',583],
['Ѧ����','Ѧ����',556],['��̽��','��̽��',439],['ԧ��','ԧ��',426],['ʷ����','ʷ����',416],
['����','����',341],['����','����',338],['�Ϸ���','�Ϸ���',281],['����','����',278],
['�Ͼ�','�Ͼ�',277],['���� ','���� ',223],['Ѧ� ','Ѧ� ',194],
['����','����',150],['��ܿ','��ܿ',147],['��ӭ��','��ӭ��',145],['������','������',135],
['���� ','���� ',95],['�ȶ���','�ȶ���',91],[' �ֻ�',' �ֻ�',87],['���� ','���� ',82],
['����','����',81]
]

with open('name_node.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)

header = ['source', 'target', 'weight']
data = [['��ʿ��','�����',242],['��ĸ','������',108], ['��ĸ','Ѧ����',102],
        ['��ĸ','����',99], ['������','����',97],
        ['������','Ϯ��',95], ['����','�־�',92], ['������','�Ϸ���',89], ['������','Ѧ����',89],
        ['��ĸ','Ϯ��',82], ['Ϯ��','����',76], ['��ĸ','ԧ��',75], ['Ϯ��','����',70],
        ['��ĸ','�Ϸ���',69], ['������','����',68], ['������','����',67], ['��ĸ','����',66],
        ['��ĸ','����',65], ['����','����',64], ['Ѧ����','Ѧ�',60],
        ['������','����',60], ['����','����',57], ['ƽ��','����',55],
        ['������','ԧ��',54], ['����','����',53], ['��ĸ','����',51], ['������','����',50],
        ['Ϯ��','ƽ��',49],['��ĸ','����',47],['����','����',45],['������','ƽ��',43], ['����','����',43],
        ['����','ƽ��',43],
        ['����','����',40],
        ['����','����',37],
        ['��ĸ','ƽ��',36],
        ['�Ϸ���','����',35],
        ['����','����',35],
        ['��ĸ','����',35],
        ]



with open('name_relationship.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)





