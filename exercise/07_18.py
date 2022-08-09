'''
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
'''
from math import ceil, floor
import pandas as pd
import math
import re


def count_time(file_path):
    df = pd.read_excel(file_path)
    # print(df)
    # print(df['通话时长'])
    time_lst = df['通话时长'].to_list()
    # transfer_time('2时30分10秒')
    total = 0.0
    for t in time_lst:
        # total += transfer_time(t)
        # r = compile_time(t)
        total += compile_time(t)
        pass

    print(int(total))
    print(round(total))
    print(ceil(total))
    # total=62.66
    # print(floor(total)) 向下取整
    # print(round(total,1)) 四舍五入
    # print(ceil(total)) 向上取整

def compile_time(str_time):
    rsec = re.compile('(\d+)秒')
    rmin = re.compile('(\d+)分')
    print(str_time)
    seci = rsec.findall(str_time)
    mini = rmin.findall(str_time)
    print(mini,seci)
    min = 0
    if(len(mini)==1):
        min = int(mini[0])
    return min+int(seci[0])/60


def transfer_time(str_time):
    hour = 0
    min = 0
    sec = 0
    print("str_time:",str_time)
    if '时' in str_time:
        hour = str_time.split('时')
        hour = hour[0]
    if '分' in str_time:
        # min = str_time.split('分')
        if '时' in str_time:
            hour = str_time.split('时')
            min = hour[0].split('分')[0]
            hour = hour[0]
        else:
            min = str_time.split('分')[0]
    if '秒' in str_time:
        if '时' in str_time:
            hour = str_time.split('时')
            min = hour[1].split('分')
            sec = min[1].split('秒')
            sec = sec[0]
            hour = hour[0]
            min = min[0]
        elif '分' in str_time:
            min = str_time.split('分')
            sec = min[1].split('秒')[0]
            min = min[0]

        else:
            sec = str_time.split('秒')[0]
            print("秒")
    print("hour：",hour)
    print("min:",min)
    print("sec：",sec)
    return float(hour)*60+float(min)+float(sec)/60


    # print(f'时：{1},分：{2},秒：{3}',hour,min,sec)

count_time('./pic/2022年07月语音通信.xls')