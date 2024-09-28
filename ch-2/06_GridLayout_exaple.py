from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI QridLayout")
        self.setWindowIcon(QIcon('./images/python_logo.png'))
        # 对8个按钮使用grid进行布局
        btn1 = self.create_btton('点击1')
        btn2 = self.create_btton('点击2')
        btn3 = self.create_btton('点击3')
        btn4 = self.create_btton('点击4')
        btn5 = self.create_btton('点击5')
        btn6 = self.create_btton('点击6')
        btn7 = self.create_btton('点击7')
        btn8 = self.create_btton('点击8')

        # 创建一个qrid布局
        grid_layout = QGridLayout()
        # 将这八个按钮添加到这个布局中
        grid_layout.addWidget(btn1, 0, 0)
        grid_layout.addWidget(btn2, 0, 1)
        grid_layout.addWidget(btn3, 0, 2)
        grid_layout.addWidget(btn4, 0, 3)
        grid_layout.addWidget(btn5, 1, 0)
        grid_layout.addWidget(btn6, 1, 1)
        grid_layout.addWidget(btn7, 1, 2)
        grid_layout.addWidget(btn8, 1, 3)

        grid_layout.setSpacing(100)  # 设置以中心位置的间距

        self.setLayout(grid_layout)

        
    def create_btton(self, str):
        btn = QPushButton(str, self)
        btn.setFont(QFont('黑体', 12, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('./images/python_logo.png'))
        btn.setIconSize(QSize(36, 36))
        return btn
    


     
app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())

