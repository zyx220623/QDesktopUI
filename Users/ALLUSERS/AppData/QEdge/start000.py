from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from .BrowserWindow import BrowserWindow
from Starts.UIstart.windowui import FrameLessWindow
from Users.ALLUSERS.AppData.QEdge.BrowserWindow import BrowserTab

class QEdge(FrameLessWindow):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent, appname="QEdge", apphandle=110001, ReSize=QSize(1200,800))
        self.__parent__ = parent
        self.__parent__.backgroundClickedEvent()
        self.__parent__.taskbar.raise_()
        self.__parent__.startbutton.raise_()
        self.body = BrowserWindow(parent=self)
        self.body.setGeometry(0, self.title_height, self.size().width(), self.size().height() - self.title_height)
        self.setWindowTitle("QEdge")
        self.setWindowIcon(QIcon("Users/ALLUSERS/AppData/QEdge/Assets/main.png"))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.body.setGeometry(0, self.title_height, self.size().width(), self.size().height() - self.title_height)

    def closeEvent(self, event):
        super().closeEvent(event)

    def showEvent(self, event):
        super().showEvent(event)
        self.body.tabs.clear()
        self.body.init_tab = BrowserTab(self.body)
        self.body.init_tab.browser.load("http://cn.bing.com/")
        self.body.add_new_tab(self.body.init_tab)
        self.body.show()


