# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
from urllib import request
from urllib.parse import quote, urljoin
from get_character_array import get_character
import string
import os


def get_urls(character_arr):
    urls=[]
    for i in set(character_arr):
        # print(i)
        url = r'https://baike.baidu.com/item/' + i
        url = quote(url, safe=string.printable)
        urls.append(url)
    # return urls
    # print('输出：',urls)

    # 遍历URL数组
    result_data = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            res_key = soup.find_all(class_="basicInfoItem_FWi9e itemValue_BJjng")
            res_val = soup.find_all(class_="basicInfo_RO2Oh J-basic-info")
            key = [ik.get_text(strip=True).replace("\n", "、") for ik in res_key]
            value = [iv.get_text(strip=True).replace("\n", "、") for iv in res_val]
            item = dict(zip(key, value))
            data = {'key': item}  # 可以根据需要调整字典结构
            result_data.append(data)
        else:
            print('失败')
    print(result_data)
    with open('json/data.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, ensure_ascii=False, indent=4)
    print("JSON文件已写入。")
if __name__ == "__main__":
    character_arr = get_character()
    urls = get_urls(character_arr)


