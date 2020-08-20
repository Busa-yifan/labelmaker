from xml.etree.ElementTree import ElementTree, Element
import os
import xml.etree.ElementTree as ET

num = 1275
path = "G:/test/tiaozhanbeidataset/exam_xml"
files = os.listdir(path)
for i in files:
    xmlpath = os.path.join(path,i)
    print(xmlpath)
    tree = ET.parse(xmlpath)
    # tree = ET.parse('D:\python\venv1\output.xml')
    root = tree.getroot()
    print(root.text)
    # 遍历文件所有的tag 为目标的值得标签
    global xmin,xmax
    xmin = []
    xmax = []
    i = 0
    for elem in root.iter('xmin'):
        xmin.append(int(elem.text))
    for elem in root.iter('xmax'):
        xmax.append(int(elem.text))
    for elem in root.iter('xmin'):
        new_elem = (1280 - xmax[i])
        elem.text = str(new_elem)
        i+=1
    i = 0
    for elem in root.iter('xmax'):
        new_elem = (1280 - xmin[i])
        elem.text = str(new_elem)
        i+=1
    tree.write('G:/test/tiaozhanbeidataset/exam_xml/exam'+str(num)+'.xml')
    num+=1
