#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import glob
from PIL import Image
import os

def resize_img(s):
    file_paths = glob.glob("./snapshots/*.jpg")
    print(file_paths)
    for p in file_paths:
        name = os.path.basename(p)
        img = Image.open(p)
        print(img.format,img.size)
        img.thumbnail(s)
        img.save('./pic/'+name)
        print(img.format,img.size)

resize_img((640,1136))
        


# resize_img()


# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# ing或-ed,-d,-t,-en或-n结尾的英语动词性形容词
def count_words():
    diary_files = glob.glob('./diary/*.txt')
    important_words = []
    for p in diary_files:
        with open(p,'r',encoding='utf-8') as f :
            data = f.readlines()
            dic = {}
            for d in data:
                words = d.split()
                for w in words:
                    if not (w.endswith('ing') and w.endswith("ed") and w.endswith("d") and w.endswith("en") and w.endswith("t")):
                        if w not in dic:
                            dic[w] = 1
                        else:
                            dic[w] += 1
            arr = sorted(dic.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
            # print(arr)
            # print(dic)
            print(arr[0])
            print(type(arr[0]))
            important_words.append(arr[0][0])
    print(important_words)

# count_words()

import re
from collections import Counter

def wc(file_name):
    print("comein====")
    exclud_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this','s', 'is', 'are', 'a', 'with', 'as', 'an']  
    words = []
    with open(file_name,'r',encoding="utf-8") as f:
        for data in f:
            d = re.sub("\"|,>|\.","",data.lower())   
            words.extend(d.split())
    
    ws = Counter(words)
    for w in exclud_words:
        ws[w] = 0
    # print("ws:",ws)
    return ws.most_common(3)

def list_files():
    txts = glob.glob("./study/exercise/diary/*.txt")
    return txts

# print(wc())
# most_common()
# map(wc,list_files())
# print(list(map(wc,list_files())))
    