'''
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
'''
import glob
import os

from h11 import Data

def list_files():
    py_files = glob.glob(os.path.join(os.getcwd(),"**/*.py"),recursive=True)
    return py_files

def notes(content):
    notes_line = 0
    if content == "'''" or content == '"""':
        notes_line += 1
    return notes_line
        

def count_notes(datas):
    dic = {}
    notes_line = 0
    blank_line = 0
    flag = False
    flag1 = False
    for data in datas:
        data = data.strip()
        
        d = data.split()
        if len(d) == 0:
            blank_line += 1
        # 注释行数处理
        if data.startswith('#'):
            notes_line += 1
        if data == "'''":
            if not flag:
                notes_line += 1
            flag = not flag

        if flag:
            notes_line += 1

        if flag1:
            notes_line += 1

        if data == '"""':
            if not flag1:
                notes_line += 1
            flag1 = not flag1
            
    dic['notes_line'] = notes_line
    dic['blank_line'] = blank_line
    dic['code_line'] = len(datas)-notes_line-blank_line
    return dic



def count_lines(p):
    dic = {}
    with open(p,'r',encoding='utf-8') as f:
        datas = f.readlines()
        print(len(datas))
        dic = count_notes(datas)
    name  = os.path.basename(p)
    return {name:dic}

codes = 0
def count_all(dic):
    global codes
    print("codes:",codes)
    print(dic)
    for k,v in dic.items():
        codes += dic[k]['code_line']

file_path = os.path.join(os.getcwd(),"**/*.py")

lst = list(map(count_lines,list_files()))
# c = sum(list(map(count_all,lst)))
# print(c)
list(map(count_all,lst))
print("codes:",codes)



