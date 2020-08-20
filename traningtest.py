# 内置 python 时间模块，这里准备用来计算每一帧视频的耗费
import time
# 用来调用摄像头与图形相关的函数功能
import cv2
import numpy as np
# 整个神经网络建构于此模块中，用以导出最终计算结果
from darkflow.net.build import TFNet


# 设定神经网络的参数，在 model 要使用什么模型，load 要加载什么权重文件
# threshold 影响神经网络判断是非的阈值，太高的话什么都辨识不出来，太低的话看到什么都觉得是标签的一种
# gpu 开启与否，数字决定开启的程度，1 表示全开，如果要留 gpu 在训练的时候预留做其他功能，可以调成 0.?
condition = {
    'model': 'cfg/yolo-voc-5c.cfg',
    'load': 1125,
    'threshold': 0.05,
    'gpu': 1
}

# 把上面设定好的 condition 放入 darkflow 模块里面
net = TFNet(condition)
# 设定标记框框的颜色种类，给几组颜色不重要，希望就是能比预测出来的标签数据多
# 这样后面 zip 起来的结果才不会有些检测到的标签没有颜色可以显示
colors = [tuple(255 * np.random.rand(3)) for i in range(10)]


img=cv2.imread('G:/test/tiaozhanbeidataset/class_pic_all/class5.jpg')
results = net.return_predict(img)
        # 把结果和 colors 结合在一起，谁比较多的部分就会因为 zip 砍掉不要了，所以 colors 要够多才行
for color, result in zip(colors, results):
    LABEL = result['label']
    CONF = result['confidence']
    TLC = (result['topleft']['x'], result['topleft']['y'])
    BRC = (result['bottomright']['x'], result['bottomright']['y'])
    note = '{}: {:.0f}%'.format(LABEL, CONF * 100)

    # 在画面上放上矩形方框与文字标注名称和可能性
    if(CONF>0.15):
        print(CONF)
        img = cv2.rectangle(img, TLC, BRC, color, 5)
        img = cv2.putText(img, note, TLC, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    # 打印每次 camera 得到画面，并加以预测得出结果，然后画上框框和文字信息的图像内容，命名为 'personal tags'
cv2.imshow('personal tags', img)
         # 在 python 中计算每一次所需时间，并打印出来参考
cv2.waitKey(0)
cv2.destroyAllWindows()
