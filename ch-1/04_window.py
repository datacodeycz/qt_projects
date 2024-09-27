from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


# 继承Qwidget类
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口的的位置和大小（位置x， 位置y， 大小x， 大小y）
        self.setGeometry(200, 200, 700, 300)
        # 设置窗口的标题
        self.setWindowTitle("python GUI")
        # 给窗口加上图标
        self.setWindowIcon(QIcon('./resource/images/python_logo.png'))
        
        # 固定窗口的高宽大小
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)
        
        # 设置窗口样式
        self.setStyleSheet('background-color: green')
        # 设置窗口透明度
        self.setWindowOpacity(0.5)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
