from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # 
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("python GUI Development")
        self.setWindowIcon(QIcon('./images/python.png'))
        '''
        # 创建标签对象，默认可以给标签对象设置文本信息
        label = QLabel("", self)
        # 给该对象设置文本信息
        label.setText('New Text is Here')

        # 移动标签到指定位置（相对窗口左上角的高宽）
        label.move(100, 100)
        # 设置标签的文本文字格式和大小
        label.setFont(QFont("sanserif", 15))
        # 设置标签的样式
        label.setStyleSheet('color:red')
        '''
        
        
        '''
        label = QLabel(self)
        # 创建一个图片对象
        pixmap = QPixmap('./ch-2/images/python_logo.png')
        # 给标签设置一个图片对象
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        # 创建一个动图对象
        movie = QMovie('./images/1.gif')
        # 设置动图的速度
        movie.setSpeed(500)
        # 给标签设置一个动图
        label.setMovie(movie)
        # 开启动图
        movie.start()
        


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())