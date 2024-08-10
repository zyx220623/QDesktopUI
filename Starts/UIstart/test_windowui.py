import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from windowui import FrameLessWindow
app = QApplication(sys.argv)
window = FrameLessWindow()
window.setWindowTitle("123")
window.setMinimumSize(50,50)
window.resize(100,100)
window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
window.show()
app.exec()