'''
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''
import pandas as pd
from lxml import etree
# from xlrd import xlr

# df = pd.DataFrame.from_dict()
df = pd.read_excel('./a.xls',engine='xlrd',header=None)
# print(df)
# print(df.loc[[0]])
lst = df.loc[0].to_list()
print(lst)

# print(df.shape[0])
dic = {}
for i in range(df.shape[0]):
    tmp = df.loc[i].to_list()
    print(type(tmp))
    key = tmp[0]
    data = tmp[1:]
    dic[key] = data
# print(lst)
# js = df.to_json()
# print(js)

# df.index()

# pd.DataFrame.to_xml('./a.xls')

def save_to_xml(js):
    root = etree.Element('root')
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]"""))
    students.text = str(js)

    student_xml = etree.ElementTree(root)
    student_xml.write('./students.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

save_to_xml(dic)
