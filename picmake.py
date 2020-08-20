import cv2

vc = cv2.VideoCapture('G:/test/tiaozhanbeidataset/video/exam_2.mp4')  # 读入视频文件
c = 1
num = 1

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
    print("视频正常打开！")
else:
    rval = False

timeF = 1  # 视频帧计数间隔频率

while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite('G:/test/tiaozhanbeidataset/exam1_test/exam' + str(num) + '.jpg', frame)  # 存储为图像
        num+=1
    c = c + 1
    cv2.waitKey(1)
vc.release()
print("截取完成")
