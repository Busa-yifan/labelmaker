from xml.etree.ElementTree import ElementTree, Element
import os
import xml.etree.ElementTree as ET

num = 677
path = "G:/test/tiaozhanbeidataset/xml"
files = os.listdir(path)
for i in files:
    xmlpath = os.path.join(path,i)
    print(xmlpath)
    tree = ET.parse(xmlpath)
    # tree = ET.parse('D:\python\venv1\output.xml')
    root = tree.getroot()
    print(root.text)
    # 遍历文件所有的tag 为目标的值得标签
    i = 0
    for elem in root.iter('name'):
        if(elem.text=='nornal'):
            new_elem = 'normal'
            elem.text = new_elem
    i+=1
    tree.write('G:/test/tiaozhanbeidataset/new_exam_xml/exam'+str(num)+'.xml')
    num+=1
