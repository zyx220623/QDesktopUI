from PySide6.QtWidgets import QWidget

from .EmbedWindow import Window
from Starts.UIstart.windowui import FrameLessWindow


class Win32ApiApps(FrameLessWindow):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent, appname="Windows 窗口嵌入工具", apphandle=120001, iconyes=False)
        self.__parent__ = parent
        self.setWindowTitle("Windows 窗口嵌入工具")
        self.body = Window(self)
        self.body.setGeometry(0,
                              self.title_height,
                              self.size().width(),
                              self.size().height() - self.title_height)
        self.body.show()

    def customTitleResizeEvent(self):
        self.body.setGeometry(0,
                              self.title_height,
                              self.size().width(),
                              self.size().height() - self.title_height)

