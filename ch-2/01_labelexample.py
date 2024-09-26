from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("python GUI Development")
        self.setWindowIcon(QIcon('./images/python.png'))
        '''
        label = QLabel("", self)
        label.setText('New Text is Here')

        label.move(100, 100)
        label.setFont(QFont("sanserif", 15))
        label.setStyleSheet('color:red')
        '''

        label = QLabel(self)
        pixmap = QPixmap('./images/python_logo.png')
        label.setPixmap(pixmap)



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())