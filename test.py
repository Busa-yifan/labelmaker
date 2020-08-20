import cv2
import os
num = 1000
#图片路径
im_dir = 'G:/test/tiaozhanbeidataset/2'
files = os.listdir(im_dir)
#for i in range(1,num):

im_name = os.path.join(im_dir, 'class1050.jpg')
frame = cv2.imread(im_name)
cv2.imshow('asd',frame)
cv2.waitKey(0)
print(im_name)
cv2.destroyAllWindows()