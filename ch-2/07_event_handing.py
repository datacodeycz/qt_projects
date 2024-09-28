from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python GUI event handing")
        self.setWindowIcon(QIcon('./images/python_logo.png'))
    
        # 创建一个按钮
        btn = self.create_button('点击')
        
        # 创建一个标签
        self.label_1 = QLabel("Default Text")
        
        # 使用Hbox进行布局
        hbox = QHBoxLayout()
        hbox.addWidget(btn)
        hbox.addWidget(self.label_1)

        # 将窗口布局设置为hbox
        self.setLayout(hbox)

        # 给这个按钮设置事件触发后，执行的内容
        btn.clicked.connect(self.click_btn)



    def click_btn(self):
        '''事件的触发 响应的结果'''
        self.label_1.setText('Another Text')
        self.label_1.setFont(QFont('Times', 15))
        self.label_1.setStyleSheet('color:red')
        
        

    def create_button(self, str):
        '''用于创建button'''
        btn = QPushButton(str)
        btn.setFont(QFont('黑体', 14, QFont.Weight.ExtraBold))
        return btn




app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())