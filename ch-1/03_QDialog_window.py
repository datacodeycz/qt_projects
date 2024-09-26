from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv)

# 对话框
window = QDialog()

window.show()

sys.exit(window.exec())
