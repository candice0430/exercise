'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

from pickle import FRAME
import random
import string
from db import db_operator


def gen_active_code():
    s = base_str1()
    print(s)

    #激活码6位大小写字母、数字
    arr = []
    for i in range(0,200):
        res = []
        for j in range(0,4):
            res.append(''.join(random.choices(s,k=5)))
            if j != 3:
                res.append('-')
        arr.append(''.join(res))
        
    print(arr)
    return arr
    


def base_str():
    start = 97
    s = ''
    for i in range(start,start+26):
        s += chr(i)
        s += chr(i).upper()
    
    for i in range(0,10):
        s += str(i)
    print(s)
    return s

def base_str1():
    return string.ascii_letters+string.digits


codes = gen_active_code()


for i in range(0,len(codes)):
    pass
    sql = 'insert into active_code(status,code) VALUES (0,"{0}")'.format(codes[i])
    print(sql)
    db_operator.insert(sql)

print(id(db_operator))
print(id(db_operator))
print(id(db_operator))



