from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

# 顺便复习一下button的方法


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI VBoxLayout")
        self.setWindowIcon(QIcon('./images/python_logo.png'))

        # 创建几个按钮
        btn1 = self.create_button('点击1')
        btn2 = self.create_button('点击2')
        btn3 = self.create_button('点击3')
        btn4 = self.create_button('点击4')
        btn5 = self.create_button('点击5')
        btn6 = self.create_button('点击6')
        btn7 = self.create_button('点击7')
        btn8 = self.create_button('点击8')

        # 使用QVBox对按钮进行布局  纵向布局
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)
        vbox.addWidget(btn6)
        vbox.addWidget(btn7)
        vbox.addWidget(btn8)

        self.setLayout(vbox)
        
        # 添加vbox布局之间的间距
        vbox.addSpacing(100)  # 离最下面的间距
        vbox.addStretch(1)  # 离最下面的间距 间距像素位参数是上述的100倍




    def create_button(self, click):
        btn = QPushButton(click,self)

        btn.setIcon(QIcon('./images/python_logo.png'))
        btn.setIconSize(QSize(36, 36))
        btn.setFont(QFont('黑体', 14, QFont.Weight.ExtraBold))  # 黑体加粗
        return btn

        

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())

