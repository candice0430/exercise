'''
第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：
'''
from pprint import PrettyPrinter
import pandas as pd
from lxml import etree
import json

def read_excel(file_path):
    df = pd.read_excel(file_path)
    # :取行
    # df.loc[0] 取第0行；df.loc[3:6]取3-6行
    # :取列
    # df['column1'] 取column1列；df[['column1','column2']] 取column1、column2列
    lst = []
    for row in range(df.shape[0]):
        # lst.append('&#xA')
        lst.append(df.loc[row][[0,1,2]].to_list())

    print(lst)
    return lst

def write_xml(data):
    root = etree.Element('root')
    numbers = etree.SubElement(root,'numbers')
    numbers.append(etree.Comment('数字信息'))
    d = json.dumps(data,indent=-1,separators=(',',']'))
    numbers.text = d

    root_xml = etree.ElementTree(root)
    root_xml.write('./numbers.xml',pretty_print=True, xml_declaration=True, encoding='utf-8')



lst = read_excel('./pic/numbers.xls')
write_xml(lst)