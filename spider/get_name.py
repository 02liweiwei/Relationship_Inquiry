# ���ݷִ�����ǰ50�����ȡ��������
import codecs
def get_character():
    f = codecs.open('C:\\Users\\HW\\Desktop\\�����ϵϵͳ\\��ϵϵͳ2.0\\counts\\renwu2.txt','r','gbk')
    data = []
    for line in f.readlines():
        array = line.strip("\n").split(" ")
        arr = [array[0]]
        data.extend(arr)
    return data
character_arr = get_character()
print(character_arr)


