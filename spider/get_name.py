# 根据分词排名前50人物获取人物名字
import codecs
def get_character():
    f = codecs.open('C:\\Users\\HW\\Desktop\\人物关系系统\\关系系统2.0\\counts\\renwu2.txt','r','gbk')
    data = []
    for line in f.readlines():
        array = line.strip("\n").split(" ")
        arr = [array[0]]
        data.extend(arr)
    return data
character_arr = get_character()
print(character_arr)


