
# coding:utf-8

from urllib import request
from urllib.parse import quote, urljoin
import string
import time
import json
from bs4 import BeautifulSoup
import codecs
from get_name import get_character
import os

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import urlretrieve


if not os.path.exists("C:\\Users\\HW\\Desktop\\人物关系系统\\关系系统2.0\\data\\spider\\image"):
	os.mkdir("C:\\Users\\HW\\Desktop\\人物关系系统\\关系系统2.0\\data\\spider\\image")


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

def get_json(character_arr , save_dir):
	data = {}
	for i in set(character_arr):
		print(i)

		url = r'https://baike.baidu.com/item/' + i
		url = quote(url, safe=string.printable)
		print('url是这个',url)

		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		response = requests.get(url)
		response.raise_for_status()

		soup = BeautifulSoup(response.text, 'html.parser')

		image_links = soup.find_all(class_='picture_QeCgL')
		print(image_links)

		for img in image_links:
			img_url = img.get('src')

			if not img_url.startswith(('http://', 'https://')):
				img_url = urljoin(url, img_url)
			img_name=str(i) + '.jpg'

			urlretrieve(img_url, img_name)

			print(f"Downloaded: {img_name}")
		res_key = soup.find_all(class_="basicInfoItem_FWi9e itemValue_BJjng")
		res_val = soup.find_all(class_="basicInfo_RO2Oh J-basic-info")
		key = [ik.get_text().strip().replace("\n", "、") for ik in res_key]
		value = [iv.get_text().strip().replace("\n", "、") for iv in res_val]
		item = dict(zip(key, value))
		data[str(i)] = item

	if not os.path.exists("../json"):
		os.mkdir("../json")
	f = codecs.open('../json/data.json', 'w', 'utf-8')
	f.write(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
	character_arr = get_character()
	save_dir = "C:\\Users\\HW\\Desktop\\人物关系系统\\关系系统2.0\\data\\spider\\image"  # 图片保存的目录
	get_json(character_arr , save_dir)



