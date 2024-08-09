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
from os import system
from System.Settings.settings import Settings


class Desktop(QMainWindow):
    startmenu_showed: bool
    tasklist: list[str]
    def taskbar_init(self):
        def show_menu(pos):
            menu = QMenu(self)
            action1 = QAction("任务管理器           ", menu)
            action2 = QAction("任务栏设置           ", menu)
            menu.addAction(action1)
            menu.addAction(action2)
            menu.exec(self.taskbar.mapToGlobal(pos))

        self.taskbar = QPushButton(self)
        self.taskbar.resize(1920, 50)
        self.taskbar.raise_()
        self.taskbar.move(0, self.size().height() - self.taskbar.size().height())
        self.taskbar.setStyleSheet(
            "QPushButton {"
            "background-color: rgba(20,20,20,0.9);"
            "}"
            "QPushButton:hover {"
            "background-color: rgba(25,25,25,0.9);"
            "}"
            "QPushButton:pressed {"
            "background-color: rgba(30,30,30,0.9);"
            "}"
        )
        self.taskbar.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.taskbar.customContextMenuRequested.connect(show_menu)
        self.taskbar.clicked.connect(self.backgroundClickedEvent)

    def background_init(self):
        def backgroundRightClickedEvent(pos: QPoint):
            self.background_menu = QMenu(self.background)
            self.see_menu = QMenu("查看", self)
            self.background_menu.addMenu(self.see_menu)
            b02 = self.background_menu.addAction("刷新")
            self.background_menu.exec(self.background.mapToGlobal(pos))

        self.background = QPushButton(QIcon("Starts/UIstart/desktopimage/background.png"), "", self)
        self.background.setIconSize(QSize(1920, 1080))
        self.background.setFixedSize(1920, 1080)
        self.background.clicked.connect(self.backgroundClickedEvent)
        self.background.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.background.customContextMenuRequested.connect(backgroundRightClickedEvent)

    def startButton_init(self):
        def startButtonRightClickedEvent():
            self.startbutton_menu = QMenu(self.startbutton)
            self.a01 = self.startbutton_menu.addAction("显示桌面")
            self.a02 = self.startbutton_menu.addAction("睡眠")
            self.a03 = self.startbutton_menu.addAction("关机")
            self.a04 = self.startbutton_menu.addAction("重新启动")
            self.a01.triggered.connect(self.desktopShowEvent)
            self.a02.triggered.connect(self.showMinimized)
            self.a03.triggered.connect(self.close)
            self.a04.triggered.connect(self.restartEvent)
            self.startbutton_menu.exec(self.startbutton.mapToGlobal(QPoint(2, self.startbutton.pos().y() -
                                                                           self.startbutton_menu.size().height() -
                                                                           1100)))

        self.startbutton = QPushButton(self)
        self.startbutton.resize(50, 50)
        self.startbutton.setIconSize(QSize(30, 30))
        self.startbutton.setStyleSheet(
            "QPushButton {"
            "background-color: rgba(20,20,20,0.1);"
            "icon: url(Starts/UIstart/desktopimage/start0.jpg);"
            "}"
            "QPushButton:hover {"
            "background-color: rgba(25,25,25,0.1);"
            "icon: url(Starts/UIstart/desktopimage/start1.jpg);"
            "}"
            "QPushButton:pressed {"
            "background-color: rgba(25,25,25,0.1);"
            "icon: url(Starts/UIstart/desktopimage/start2.jpg);"
            "}"
        )
        self.startbutton.move(self.taskbar.pos().x(), self.taskbar.pos().y())
        self.startbutton.clicked.connect(self.startButtonClickedEvent)
        self.startbutton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.startbutton.customContextMenuRequested.connect(startButtonRightClickedEvent)

    def startmenu_init(self):
        def ShutDownButtonClickedEvent():
            self.shutdown_menu = QMenu(self.shutdown_button)
            self.s01 = self.shutdown_menu.addAction("睡眠")
            self.s02 = self.shutdown_menu.addAction("关机")
            self.s03 = self.shutdown_menu.addAction("重新启动")
            self.s01.triggered.connect(self.sleepEvent)
            self.s02.triggered.connect(self.close)
            self.s03.triggered.connect(self.restartEvent)
            self.shutdown_menu.exec(self.shutdown_button.mapToGlobal(
                QPoint(self.shutdown_button.pos().x() + self.shutdown_button.size().width(),
                       self.shutdown_button.pos().y() - 670)))

        def settingButtonClickedEvent():
            if "设置" not in self.tasklist:
                self.setting_window = Settings(self)
                self.setting_window.show()
                self.tasklist.append("设置")
            self.backgroundClickedEvent()
            self.taskbar.raise_()
            self.startbutton.raise_()

        self.startmenu_showed = False
        self.startmenu = QPushButton(self)
        self.startmenu.resize(500, 700)
        self.startmenu.move(2, self.size().height())
        self.startmenu.setStyleSheet("QPushButton {"
                                     "background-color: rgba(40,40,40,0.9);"
                                     "border: none;"
                                     "}")

        self.startmenu_button_qss = ("QPushButton {"
                                     "background-color: rgba(40,40,40,0.9);"
                                     'font: normal normal 15px "微软雅黑";'
                                     "color: rgb(255,255,255);"
                                     "border: none;"
                                     "}"
                                     "QPushButton:hover {"
                                     "background-color: rgba(100,100,100,0.9);"
                                     "color: rgb(255,255,255);"
                                     "}")

        self.shutdown_button = QPushButton("电源", self.startmenu)
        self.shutdown_button.resize(80, 30)
        self.shutdown_button.move(0, self.startmenu.size().height() - self.shutdown_button.size().height())
        self.shutdown_button.setStyleSheet(self.startmenu_button_qss)
        self.shutdown_button.clicked.connect(ShutDownButtonClickedEvent)
        self.setting_button = QPushButton("设置", self.startmenu)
        self.setting_button.resize(80, 30)
        self.setting_button.move(0, self.shutdown_button.pos().y() - self.setting_button.size().height())
        self.setting_button.setStyleSheet(self.startmenu_button_qss)
        self.setting_button.clicked.connect(settingButtonClickedEvent)

    def UIinit(self):
        self.background_init()
        self.taskbar_init()
        self.startmenu_init()
        self.startButton_init()

    def __init__(self):
        super(Desktop, self).__init__()
        self.tasklist = []
        self.UIinit()
        self.resize(1600, 900)
        # self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.showFullScreen()
        self.setWindowTitle("QSystem")

    def startButtonClickedEvent(self):
        if not self.startmenu_showed:
            self.startmenu.move(2, self.size().height() - self.startmenu.size().height() - 55)
            self.startmenu.raise_()
            self.startmenu_showed = True
        else:
            self.startmenu.move(2, self.size().height())
            self.startmenu_showed = False

    def backgroundClickedEvent(self):
        if not self.startmenu_showed:
            pass
        else:
            self.startmenu.move(2, self.size().height())
            self.startmenu_showed = False

    def resizeEvent(self, event):
        super(Desktop, self).resizeEvent(event)
        try:
            self.taskbar.move(0, self.size().height() - self.taskbar.size().height())
        except:
            pass
        try:
            self.startbutton.move(self.taskbar.pos().x(), self.taskbar.pos().y())
        except:
            pass
        try:
            self.startmenu.move(2, self.size().height())
        except:
            pass

    def restartEvent(self):
        self.close()
        system("__init__.vbs")

    def desktopShowEvent(self):
        self.backgroundClickedEvent()

    def keyPressEvent(self, event):
        super(Desktop, self).keyPressEvent(event)
        if event.key() == Qt.Key.Key_Alt:
            self.startButtonClickedEvent()

    def closeEvent(self, event):
        super().closeEvent(event)

    def sleepEvent(self):
        self.backgroundClickedEvent()
        self.showMinimized()
