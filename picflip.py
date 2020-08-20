import cv2
import os

path = "G:/test/tiaozhanbeidataset/exam_pic"
files = os.listdir(path)
num = 1275
print("开始处理！")
for i in files:
    picpath = os.path.join(path, i)
    print(picpath)
    img = cv2.imread(picpath)
    out = cv2.flip(img,1)
    cv2.imwrite("G:/test/tiaozhanbeidataset/exam_pic_flip/exam"+ str(num) + '.jpg',out)
    num += 1
print("完成图片翻转处理")