import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import math
import os
import nxml, styleSheet


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.FRAME_WIDTH = 1280
        self.FRAME_HEIGHT = 720
        self.resize(self.FRAME_WIDTH, self.FRAME_HEIGHT)
        self.setWindowTitle('LabelImage')
        self.IMAGE_FORMAT = ['jpg', 'jpeg', 'png']

        self.IMAGE_PATH = None

        self.SAVE_PATH = None

        self.pos1 = [0, 0]
        self.pos2 = [0, 0]

        self.stylesheet_btn_add = styleSheet.stylesheet_btn_add
        self.stylesheet_btn_prev = styleSheet.stylesheet_btn_prev
        self.stylesheet_btn_next = styleSheet.stylesheet_btn_next
        self.stylesheet_btn_save = styleSheet.stylesheet_btn_save
        self.stylesheet_btn_clear = styleSheet.stylesheet_btn_clear

        self.IMAGE_list = os.listdir(self.IMAGE_PATH)
        self.imageFilter()
        self.IMAGE_index = 0

        self.initUI()


    def initUI(self):
        self.left_area_width = 180

        self.left_area = QVBoxLayout()
        self.left_area.setGeometry(QtCore.QRect(0, 0, self.left_area_width, self.FRAME_HEIGHT))

        # 按钮
        self.btn_preview = QPushButton(self)
        self.btn_preview.setText('上一张')
        self.btn_preview.clicked.connect(lambda: self.switch_image('prev'))
        self.btn_preview.setMinimumWidth(280)
        self.btn_preview.setMinimumHeight(40)
        self.btn_preview.setStyleSheet(self.stylesheet_btn_prev)
        self.btn_preview.setEnabled(False)

        self.btn_next = QPushButton(self)
        self.btn_next.setText('下一张')
        self.btn_next.clicked.connect(lambda: self.switch_image('next'))
        self.btn_next.setMinimumWidth(280)
        self.btn_next.setMinimumHeight(40)
        self.btn_next.setStyleSheet(self.stylesheet_btn_next)
        self.btn_next.setEnabled(False)

        self.btn_save = QPushButton(self)
        self.btn_save.setText('保存')
        self.btn_save.clicked.connect(lambda: self.switch_image('save'))
        self.btn_save.setMinimumWidth(280)
        self.btn_save.setMinimumHeight(40)
        self.btn_save.setStyleSheet(self.stylesheet_btn_save)
        self.btn_save.setEnabled(False)

        self.btn_clear = QPushButton(self)
        self.btn_clear.setText('清除')
        self.btn_clear.clicked.connect(lambda: self.switch_image('clear'))
        self.btn_clear.setMinimumWidth(280)
        self.btn_clear.setMinimumHeight(40)
        self.btn_clear.setStyleSheet(self.stylesheet_btn_clear)
        self.btn_clear.setEnabled(False)

        # 路径输入框
        self.path_input_layout = QVBoxLayout()
        self.file_path_line = QHBoxLayout()
        self.save_path_line = QHBoxLayout()

        self.path_input_btn = QPushButton('确认')
        self.path_input_btn.clicked.connect(self.getPath)

        self.line1_label = QLabel(self)
        self.line1_label.setText('文件路径：')
        self.line1_edit = QLineEdit(self)

        self.line2_label = QLabel(self)
        self.line2_label.setText('保存路径：')
        self.line2_edit = QLineEdit(self)

        self.file_path_line.addWidget(self.line1_label)
        self.file_path_line.addWidget(self.line1_edit)

        self.save_path_line.addWidget(self.line2_label)
        self.save_path_line.addWidget(self.line2_edit)

        self.path_input_layout.addLayout(self.file_path_line)
        self.path_input_layout.addLayout(self.save_path_line)
        self.path_input_layout.addWidget(self.path_input_btn)

        # 显示类别的滚动列表
        self.text = QLabel(self)
        self.text.setText('类别列表(右击修改、删除)')
        self.text.setFont(QFont("Courier", 10, QFont.Bold))

        self.label_list = myQList(self)
        self.label_list.setMinimumHeight(300)
        self.label_list.doubleClicked.connect(self.edit_label)

        self.btn_add_label = QPushButton(self)
        self.btn_add_label.setText('添加')
        self.btn_add_label.clicked.connect(self.add_label)
        self.btn_add_label.setStyleSheet(self.stylesheet_btn_add)
        self.btn_add_label.setMinimumHeight(30)

        self.picture_frame = myQLabel(self, self.FRAME_WIDTH, self.FRAME_HEIGHT, self.label_list)
        self.setMinimumHeight(680)

        self.left_area.addLayout(self.path_input_layout)
        self.left_area.addStretch(3)
        self.left_area.addWidget(self.text)
        self.left_area.addWidget(self.label_list)
        self.left_area.addWidget(self.btn_add_label)
        self.left_area.addStretch(3)
        self.left_area.addWidget(self.btn_preview)
        self.left_area.addStretch(1)
        self.left_area.addWidget(self.btn_next)
        self.left_area.addStretch(1)
        self.left_area.addWidget(self.btn_save)
        self.left_area.addStretch(1)
        self.left_area.addWidget(self.btn_clear)
        self.left_area.addStretch(1)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.left_area)
        self.mainLayout.addWidget(self.picture_frame)
        self.mainLayout.addStretch(1)

        self.setLayout(self.mainLayout)

    def getPath(self):
        if self.line1_edit.text() != '' and self.line2_edit.text() != '':
            self.IMAGE_PATH = self.line1_edit.text()
            self.SAVE_PATH = self.line2_edit.text()
            try:
                self.IMAGE_list = os.listdir(self.IMAGE_PATH)
                self.imageFilter()
                self.IMAGE_index = 0
                self.switch_image('prev')
                self.btn_preview.setEnabled(True)
                self.btn_next.setEnabled(True)
                self.btn_save.setEnabled(True)
                self.btn_clear.setEnabled(True)
            except:
                self.line1_edit.setText('')
                self.line2_edit.setText('')

    def switch_image(self, flag):
        if flag == 'prev':
            if self.IMAGE_index != 0:
                self.IMAGE_index -= 1
        elif flag == 'next':
            self.IMAGE_index += 1
        elif flag == 'clear':
            self.picture_frame.pos1, self.picture_frame.pos2 = [0, 0], [0, 0]
            self.picture_frame.pos1_list, self.picture_frame.pos2_list, self.picture_frame.label_list = [], [], []
        elif flag == 'save':
            # 保存label
            nxml.generate(os.path.join(self.SAVE_PATH, self.IMAGE_list[self.IMAGE_index][:-3]+'xml'),
                          self.picture_frame.pos1_list, self.picture_frame.pos2_list, self.picture_frame.label_list,
                          self.ration, [self.IMAGE.width(), self.IMAGE.height(), 3])
            self.IMAGE_index += 1

        if self.IMAGE_index > len(self.IMAGE_list)-1:
            self.IMAGE_index = len(self.IMAGE_list)-1

        self.IMAGE = QPixmap(os.path.join(self.IMAGE_PATH, self.IMAGE_list[self.IMAGE_index]))
        print(self.IMAGE_list[self.IMAGE_index])
        picture_frame_width = self.FRAME_WIDTH / 5 * 4
        picture_frame_height = self.FRAME_HEIGHT
        image_height = self.IMAGE.height()
        image_width = self.IMAGE.width()

        ## 计算水平和垂直方向上的缩放系数，取最大的缩放系数对图片进行缩放
        y_ration = float(image_height / picture_frame_height)
        x_ration = float(image_width / picture_frame_width)
        self.ration = max(x_ration, y_ration)
        self.picture_frame.setGeometry(QtCore.QRect(self.left_area_width, 0, self.left_area_width + picture_frame_width,
                                                    picture_frame_height))
        img = self.IMAGE.scaled(image_width / self.ration, image_height / self.ration)
        # self.picture_frame.setAlignment(Qt.AlignHCenter)
        self.picture_frame.setAlignment(Qt.AlignLeft)
        self.picture_frame.setAlignment(Qt.AlignTop)
        self.picture_frame.setPixmap(img)

        # 重置参数
        self.picture_frame.pos1, self.picture_frame.pos2 = [0, 0], [0, 0]
        self.picture_frame.pos1_list, self.picture_frame.pos2_list, self.picture_frame.label_list = [], [], []
        self.picture_frame.image_width = image_width / self.ration
        self.picture_frame.image_height = image_height / self.ration


    def add_label(self):
        label, res = QInputDialog.getText(self, 'Input', '输入类别：')
        if res:
            self.label_list.addItem(label)

    def edit_label(self):
        label, res = QInputDialog.getText(self, '修改', '请输入修改后的类别：')
        if res:
            self.label_list.item(self.label_list.currentRow()).setText(label)

    def imageFilter(self):
        remove_list = []
        for image_path in self.IMAGE_list:
            legal = False
            for format in self.IMAGE_FORMAT:
                if image_path.endswith(format):
                    legal = True
            if not legal:
                remove_list.append(image_path)
        for item in remove_list:
            self.IMAGE_list.remove(item)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            self.switch_image('save')

class myQList(QListWidget):
    def __init__(self, parent=None):
        super(myQList, self).__init__(parent)

    def contextMenuEvent(self, QContextMenuEvent):
        item = self.itemAt(self.mapFromGlobal(QCursor.pos()))
        if item != None:
            popMenu = QMenu(self)
            mod_act = QAction('修改')
            pop_act = QAction('删除')
            popMenu.addAction(mod_act)
            popMenu.addAction(pop_act)
            mod_act.triggered.connect(lambda: self.mod_clicked(self.currentRow()))
            pop_act.triggered.connect(lambda: self.pop_clicked(self.currentRow()))
            popMenu.exec_(QCursor.pos())

    def mod_clicked(self, row):
        label, res = QInputDialog.getText(self, '修改', '请输入修改后的类别：')
        if res:
            self.item(row).setText(label)

    def pop_clicked(self, row):
        self.takeItem(row)


class myQLabel(QtWidgets.QLabel):
    def __init__(self, parent, image_width, image_height, pre_label_list):
        super(myQLabel, self).__init__(parent)
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.pos1_list = []
        self.pos2_list = []
        self.label_list = []
        self.pre_label_list = pre_label_list
        self.image_width = image_width
        self.image_height = image_height

    def paintEvent(self, QPaintEvent):
        QLabel.paintEvent(self, QPaintEvent)
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(0, 200, 0, 40))
        qp.drawRect(self.pos1[0], self.pos1[1], width, height)
        if len(self.pos1_list) != 0:
            pos_list = zip(self.pos1_list, self.pos2_list, self.label_list)
            for pos1, pos2, label in pos_list:
                w = pos2[0] - pos1[0]
                h = pos2[1] - pos1[1]
                qp.drawRect(pos1[0], pos1[1], w, h)
                qp.setFont(QFont("Courier", 14, QFont.Bold))
                qp.drawText(pos1[0]+5, pos1[1]+16, label)
        qp.end()

    def mousePressEvent(self, QMouseEvent):
        self.pos1 = QMouseEvent.pos().x(), QMouseEvent.pos().y()

    def mouseMoveEvent(self, QMouseEvent):
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()

        # 当鼠标超出图片的边界，让坐标回到边界
        if QMouseEvent.pos().x() > self.image_width:
            x = math.floor(self.image_width)
        if QMouseEvent.pos().x() < 0:
            x = 0
        if QMouseEvent.pos().y() > self.image_height:
            y = self.image_height
        if QMouseEvent.pos().y() < 0:
            y = 0
        self.pos2 = x, y
        self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        # class_name, res = QInputDialog.getText(self, 'Input', '输入类别: ')
        # if res:
        #     self.pos1_list.append(list(self.pos1))
        #     self.pos2_list.append(list(self.pos2))
        #     self.label_list.append(class_name)
        # else:
        #     self.pos1 = [0, 0]
        #     self.pos2 = [0, 0]
        self.dialog = QDialog(self)
        self.dialog.setFont(QFont("Courier", 11))
        self.dialog.setWindowTitle('类别选择')
        self.dialog.resize(250, 150)
        layout = QVBoxLayout()

        # 下拉列表
        combo = QComboBox(self)
        for index in range(self.pre_label_list.count()):
            combo.addItem(self.pre_label_list.item(index).text())
        if self.pre_label_list.count() == 0:
            combo.addItem('无')

        # 提示信息
        text = QLabel(self)
        text.setText('请选择类别：')

        btn_layout = QHBoxLayout()
        # 确认按钮
        btn_ok = QPushButton(self)
        btn_ok.setText('确认')
        btn_ok.resize(50, 50)
        btn_ok.clicked.connect(lambda: self.pick_label(str(combo.currentText())))

        # 取消按钮
        btn_cancel = QPushButton(self)
        btn_cancel.setText('取消')
        btn_cancel.clicked.connect(self.pick_label_cannel)

        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_cancel)

        layout.addWidget(text)
        layout.addStretch(1)
        layout.addWidget(combo)
        layout.addStretch(1)
        layout.addLayout(btn_layout)
        self.dialog.setLayout(layout)
        self.dialog.show()

    def pick_label(self, class_name):
        if self.pre_label_list.count() == 0:
            QMessageBox.warning(self, 'Warning', '类别不能为空', QMessageBox.Ok)
            self.pos1 = [0, 0]
            self.pos2 = [0, 0]
        else:
            self.pos1_list.append(list(self.pos1))
            self.pos2_list.append(list(self.pos2))
            self.label_list.append(class_name)
        self.dialog.close()

    def pick_label_cannel(self):
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.dialog.close()


# class myQDialog(QDialog):
#     def __init__(self, parent=None):
#         super(myQLabel, self).__init__(parent)
#
#     def closeEvent(self, QCloseEvent):
#         super(myQLabel, self).closeEvent(QCloseEvent)
#         self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
