from PySide6.QtWidgets import QWidget

from Starts.UIstart.windowui import FrameLessWindow


class Settings(FrameLessWindow):
    def __init__(self, parent: QWidget):
        super(Settings, self).__init__("设置", 100001, parent)
        self.setWindowTitle("设置")
        self.setGeometry(100,100,900,450)
