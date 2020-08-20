import cv2
import os

#图片路径
im_dir = 'G:/test/tiaozhanbeidataset/1'
#输出视频路径
video_dir = 'G:/test/tiaozhanbeidataset/make_video/exam_video_2.avi'
#帧率
fps = 30
#图片数
num = 2064
#图片尺寸
img_size = (1280,720)

#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')#opencv2.4
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #opencv3.0
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)


for i in range(1,num):
    im_name = os.path.join(im_dir, 'exam'+str(i)+'.jpg')
    frame = cv2.imread(im_name)
    videoWriter.write(frame)
    print(im_name)

videoWriter.release()
print('finish')
