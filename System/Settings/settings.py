from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget

from Starts.UIstart.windowui import FrameLessWindow


class Settings(FrameLessWindow):
    def __init__(self, parent: QWidget | None = None):
        super(Settings, self).__init__("设置", 100001, parent=parent, MinimumSize=QSize(800, 450), themeBackground=True)
        self.setWindowTitle("设置")
        self.setGeometry(100,100,900,450)
