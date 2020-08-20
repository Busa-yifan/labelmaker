#xml测试
import xml.etree.ElementTree as ET
import cv2

tree = ET.parse('G:/test/tiaozhanbeidataset/exam_xml/exam1000.xml')
root = tree.getroot()
print(root.text)
xmin=[]
ymin=[]
xmax=[]
ymax=[]
for elem in root.iter('xmin'):
    xmin.append(int(elem.text))
for elem in root.iter('ymin'):
    ymin.append(int(elem.text))
for elem in root.iter('xmax'):
    xmax.append(int(elem.text))
for elem in root.iter('ymax'):
    ymax.append(int(elem.text))


img=cv2.imread('G:/test/tiaozhanbeidataset/exam_2_pic/exam1000.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_AUTOSIZE)
cv2.rectangle(img,(xmin[4],ymin[4]),(xmax[4],ymax[4]),(0,255,0),2)
cv2.imshow('input_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()