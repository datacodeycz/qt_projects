from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

# 状态栏窗口
window = QMainWindow()

# 在窗口的左下角添加文本信息
window.statusBar().showMessage("welcome to PyQt")

# 在左上方（默认）添加file按钮
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())