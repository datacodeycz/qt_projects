from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

# 状态栏窗口
window = QMainWindow()
window.statusBar().showMessage("welcome to PyQt")

window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())