from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI HBoxLayout")
        self.setWindowIcon(QIcon('./images/python_logo.png'))

        # 使用Hbox对按钮进行布局 横向布局
        hbox = QHBoxLayout()

        btn1 = QPushButton('click1')
        btn2 = QPushButton('click2')
        btn3 = QPushButton('click3')
        btn4 = QPushButton('click4')

        # 将这四个按钮添加到这个布局中
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        # 添加hbox布局之间的间距
        # hbox.addSpacing(100)  # 离最右边的间距
        hbox.addStretch(5)  # 离最右边的间距 间距像素位参数是上述的100倍

        self.setLayout(hbox)  # 将hbox设置为主要的局部
        

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())

