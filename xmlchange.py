import os
from xml.etree.ElementTree import ElementTree,Element

rootdir = "G:/test/tiaozhanbeidataset/exam_xml"
outdir = "G:/test/tiaozhanbeidataset/exam_xml"
list = os.listdir(rootdir)
for i in range(0,len(list)):
    path = os.path.join(rootdir, list[i])
    print(path)
    outpath = os.path.join(outdir, list[i])
    tree=ElementTree()
    tree.parse(path)
    root=tree.getroot()

    #element=Element('annotation') #指点里面是属性，结果展示：<train name="wang">
    #创建二级目录

    one=Element('filename')
    one.text=list[i][:-3]+"jpg"#二级目录的值 #结果展示：<id>1</id>
    root.append(one)#将二级目录加到一级目录里
    #root.append(element)

    tree.write(outpath,encoding="utf-8",xml_declaration=True)
