# 第 0008 题： 一个HTML文件，找出里面的正文。
from bs4 import BeautifulSoup
import requests
import urllib3

r = requests.get('https://www.baidu.com/')
r.encoding = "utf-8"
print(r.text)
bs = BeautifulSoup(r.text,from_encoding='gb18030')
print(bs.title.name)
print(bs.title.string)
# print
# print(bs.prettify())
# print(bs.findall("body"))
# print(bs.text)
# print(content)

for k in bs.find_all("a"):
    print(k['href'])



# 第 0009 题： 一个HTML文件，找出里面的链接。