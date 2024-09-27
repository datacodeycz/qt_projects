from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon('./images/python_logo.png'))

        # 添加一个输入框lineEdit
        line_edit = QLineEdit(self)
        # 设置该输入框文字的样式
        line_edit.setFont(QFont('Sanserif', 12))
        # 设置该输入框的默认文字
        # line_edit.setText('Default Text')
        # 设置该输入框的提示文字(占位字符)
        line_edit.setPlaceholderText('Please enter your username')
        # 设置该输入框是否能输入内容，默认是True 可以输入
        # line_edit.setEnabled(False)  # 不可用了
        # 将该输入框格式设置为密码格式（就是看不到输入的内容）
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        

    
app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())

