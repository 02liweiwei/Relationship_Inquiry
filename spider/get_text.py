import requests
import json
from bs4 import BeautifulSoup

def book_spider(url):
    url = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = page_text.apparent_encoding
    page_text = page_text.text

    soup = BeautifulSoup(page_text, 'lxml')
    aTagList= soup.select('.paiban li > a')

    titleList = [i.text for i in aTagList]
    urlList = [i["href"] for i in aTagList]

    with open('./红楼梦.txt', 'w', encoding='utf-8') as fp:
        fp.write("红楼梦\n")
    for chp in zip(titleList, urlList):
        write_chapter(chp)
    print("已成功下载红楼梦全文！")


def write_chapter(urlList):
    title, url = urlList
    intact_url =  url
    print(intact_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    page_text = requests.get(url=intact_url, headers=headers, timeout=10)
    page_text.encoding = page_text.apparent_encoding
    page_text = page_text.text
    print('文章内容',page_text )
    soup = BeautifulSoup(page_text, 'lxml')
    content = soup.select('.grap')

    txt = ""
    for i in content:
        txt += i.text
    with open('红楼梦.txt', 'a', encoding='utf-8') as fp:
        fp.write(title + '\n')
        fp.write(txt + '\n')
    print("已成功下载内容：{}".format(title))


if __name__ == '__main__':
    url = "https://hongloumeng.5000yan.com/"
    book_spider(url)
