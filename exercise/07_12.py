'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：
'''
from asyncore import write
import xlwt


def write_to_xls():
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(sheetname='test')
    datas = {
        "1":["张三",150,120,100],
        "2":[u"李四",90,99,95],
        "3":[u"王五",60,66,68]
    }

    for r,k in enumerate(datas.keys()):
        sheet.write(r,0,k)
        for c,v in enumerate(datas[k]):
            print("r:",r,'c:',c+1,'v',v)
            # print("c",c)

            sheet.write(r,c+1,v)
    wb.save('./a.xls')

'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：
'''
import json
def read_data(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        data = f.read()
    data_json = json.loads(data)
    print(data_json)
    print(type(data_json))
    return data_json

def write_json_to_xls(json_data):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet')
    for r,key in enumerate(json_data.keys()):
        sheet.write(r,0,key)
        sheet.write(r,1,json_data[key])
    wb.save('./city.xls')


    
# d = read_data('./pic/city.txt')
# write_json_to_xls(d)

'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中，如下图所示：
'''

import pandas as pa
from xlsxwriter import Workbook

def write_by_pa(datas):
    df = pa.DataFrame.from_dict(datas)
    with pa.ExcelWriter('./pic/numbers.xls',engine='xlsxwriter') as writer:
        df.to_excel(writer)
    

# read_data_to_arr()
d = read_data('./pic/numbers.txt')
write_by_pa(d)
# print(d)