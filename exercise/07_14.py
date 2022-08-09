'''
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <cities>
    <!-- 
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </cities>
    </root>
'''
import pandas as pa
from lxml import etree

def read_data(file_path):
    df = pa.read_excel(file_path,header=None)
    print(df)
    return dict(zip(df[0].to_list(),df[1].to_list()))

def write_xml(js):
    root = etree.Element('root')
    citys = etree.SubElement(root,'cities')
    citys.append(etree.Comment('城市信息'))
    citys.text = str(js)

    city_xml = etree.ElementTree(root)
    city_xml.write('./city.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')




js = read_data('./city.xls')
write_xml(js)