# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

from dataclasses import replace
import random
import re
import string
from PIL import Image,ImageFont,ImageDraw


def get_chr():
    return random.choice(string.ascii_letters)

def generator_font_color():
    return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))

def generator_bgcolor():
    return (random.randint(64, 355), random.randint(64, 355), random.randint(64, 355))

def imag_produce():
    w = 60*4
    h = 60
    img = Image.new('RGB',(w,h),(255,255,255))      # 生成一张新图片
    font = ImageFont.truetype('./pic/FreeMono.ttf',60)   # 第一个参数为字体文件，第二个参数为字体大小
    draw = ImageDraw.Draw(img)
    for i in range(w):
        for j in range(h):
            draw.point((i,j),fill=generator_bgcolor())
    for i in range(4):
        draw.text((i*60+10,10),get_chr(),font=font,fill=generator_font_color())
    img.save('0010.jpg')
    img.show()

    

# print(get_chr())
# imag_produce()

'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''
def filter_sense(file_path):
    with open(file_path,encoding='utf-8') as f:
        data = f.read()
        words = data.split()
        print(words)
        str = input()
        if str in words:
            print("Freedom")
        else:
            print("Human Rights")

# filter_sense('./pic/sense.txt')

'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

def replace_sense_words(file_path):
    with open(file_path,encoding='utf-8') as f:
        data = f.read()
        words = data.split()
        print(words)
        print("请输入内容：")
        w = input() 
        replace_words = w
        for sense_word in words:
            index = w.find(sense_word)
            if index != -1:
                # print("sense_word:",sense_word)
                # print("w[index:index+len(sense_word)]:",w[index:index+len(sense_word)])
                replace_words = replace_words.replace(w[index:index+len(sense_word)],'*'*len(sense_word))
 
        print(replace_words)

replace_sense_words('./pic/sense.txt')