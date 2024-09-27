from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        # 不需要将.ui文件转换成.py再运行，可以通过loadUi直接运行
        uic.loadUi('./windowUI.ui', self)


app = QApplication(sys.argv)

window = UI()

window.show()

sys.exit(app.exec())