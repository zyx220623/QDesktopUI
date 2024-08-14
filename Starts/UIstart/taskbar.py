from PySide6.QtCore import (Qt,
                            QSize, QPoint)
from PySide6.QtGui import (QIcon,
                           QFont,
                           QAction,
                           QPixmap)
from PySide6.QtWidgets import (QMainWindow,
                               QWidget,
                               QDialog,
                               QApplication,
                               QPushButton,
                               QMenu)


class Taskbar(QPushButton):
    tasklist: list[dict[str, list[QPushButton]]]
    toleft: int

    def __init__(self, parent: QWidget = None, background: tuple[int, int, int, int] = (240, 240, 240, 0.5)):
        super().__init__(parent=parent)
        self.setStyleSheet("QPushButton {"
                           f"background-color:rgb{background}"
                           "}")
        self.tasklist = []

    def add_window(self,
                   appname: str,
                   apphundle: str,
                   window: list[QPushButton]):
        self.tasklist.append({"appname": appname,
                              "apphundle": apphundle,
                              "appid": str(len(self.tasklist)),
                              "windowlist": window})
        self.appicon = QPushButton(self)
        self.appicon.resize(self.size().height(), self.size().height())
        self.appicon.move(len(self.tasklist) * self.size().height(), 0)

    def remove_window(self):
        pass

    def thd_window(self):
        pass
