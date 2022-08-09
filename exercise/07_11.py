'''
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
'''
from cmath import pi
from pyparsing import srange
import requests
from bs4 import BeautifulSoup
import re
import time
import os

def scrap_img():
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    # url = 'https://tieba.baidu.com/p/2555125530'
    url = 'https://www.huiyi8.com/tupian/tag-%E7%8C%AB%E5%92%AA/1.html'
    r = requests.get(url,headers=headers)

    r.encoding = "utf-8"
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')

  
    items = soup.find_all('img')
    print("items:",items)
    folder_path = './photo/'
    if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
        os.makedirs(folder_path)  # 创建文件夹
    
    for index,item in enumerate(items):
        if item:		
            pic_src = item.get('src')
            if pic_src.startswith('http'):
                # pic_src = "http:"+pic_src
                html = requests.get(pic_src)   # get函数获取图片链接地址，requests发送访问请求
                print("scr:",pic_src)
                img_name = folder_path + str(index + 1) +'.png'
                with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
                    file.write(html.content)
                    file.flush()
                file.close()  # 关闭文件
                # print('第%d张图片下载完成' %(index+1))
                time.sleep(1)  # 自定义延时

# scrap_img()



def get_img(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    img_itmes = soup.find_all('img')

    src_dir = './photos/'
    if not os.path.exists(src_dir):
        print("comein")
        os.makedirs(src_dir)
    for index,img_item in enumerate(img_itmes):

        src = img_item.get('src')
        if src.startswith("http"):
            img_data = requests.get(src)

            img_name = src_dir + str(index + 1) +'.png'
            with open(img_name,'wb') as f:
                f.write(img_data.content)
                f.flush()

get_img('https://www.huiyi8.com/tupian/tag-%E7%8C%AB%E5%92%AA/1.html')
            


