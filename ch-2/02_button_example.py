from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon('./images/python_logo.png'))
        self.create_button()

    def create_button(self):
        # 创建一个按钮对象
        btn = QPushButton("Click", self)
        
        # 设置该按钮对象的位置和大小，位置是针对于窗口左上角
        btn.setGeometry(100, 100, 150, 150)
        # 设置该按钮对象显示的文字样式
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        
        # 设置该按钮对象显示的图标
        btn.setIcon(QIcon('./images/python_logo.png'))

        # 设置图标显示大小
        btn.setIconSize(QSize(36, 36))

        # 给该按钮对象设置菜单栏  QMenu()
        # 创建一个菜单栏对象
        menu = QMenu()
        # 设置该菜单栏对象中文字的样式
        menu.setFont(QFont("times", 14, QFont.Weight.ExtraBold))
        # 设置该菜单栏对象的样式
        menu.setStyleSheet('background-color: green')
        # 增加菜单栏的内容
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Paste')
        # 将该菜单栏对象设置到按钮中
        btn.setMenu(menu)



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())

