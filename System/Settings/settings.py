from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QTabWidget, QPushButton, QLabel, QScrollArea

from Starts.UIstart.windowui import FrameLessWindow


class Settings(FrameLessWindow):
    def __init__(self, parent: QWidget | None = None):
        super(Settings, self).__init__("设置",
                                       100001,
                                       parent=parent,
                                       MinimumSize=QSize(800, 450),
                                       themeBackground=True,
                                       iconyes=False,
                                       )
        self.public_qss()
        self.setWindowTitle("设置")
        self.setGeometry(100, 100, 900, 450)
        self.setMouseTracking(True)
        self.tabWidget_toLeft = 120
        self.initUI()
        self.initLeftList()
        self.initmouseT()
        self.__System()

    def resizeEvent(self, event):
        self.tabWidget.setGeometry(self.tabWidget_toLeft, 0,
                                   self.size().width() - self.tabWidget_toLeft,
                                   self.size().height())
        self.buttonl1.setGeometry(0, self.size().height() - self.bh, self.bw, self.bh)
        super().resizeEvent(event)

    def public_qss(self):
        self.pqss_title = ("QLabel {"
                           'font: normal bold 25px "微软雅黑";'
                           "background-color:rgba(200,200,200,0);"
                           "}")
        self.pqss_2title = ("QLabel {"
                            'font: normal bold 23px "微软雅黑";'
                            "background-color:rgba(200,200,200,0);"
                            "}")

    def initUI(self):
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(self.tabWidget_toLeft, 0,
                                   self.size().width() - self.tabWidget_toLeft,
                                   self.size().height())
        self.tabWidget.setStyleSheet("""
QTabWidget
{
    background-color:rgba(200,200,200,0);
}
QTabWidget:pane
{
    background-color: rgba(200,200,200,0);
    border:none;
 
}
QTabBar:tab
{
     font: 15pt "Chinese fine black";
     background-color: rgba(200,200,200,0);
     color: rgba(200,200,200,0);
     min-width: 60px;
     min-height: 30px;
     padding: 2px;
}
QTabBar:tab:selected
{
    background-color: rgba(200,200,200,0);
}""")

    def __System(self):
        self.system_S = QScrollArea()
        self.system = QWidget(self.system_S)
        self.system_T = QLabel(" 系统", self.system)
        self.system_T.setStyleSheet(self.pqss_title)
        self.system_T.move(self.edge, self.edge)
        self.system_T.resize(1000,30)
        self.tabWidget.addTab(self.system_S, "系统")

    def initLeftList(self):
        self.bw = self.tabWidget_toLeft
        self.bh = 40
        self.th = self.title_height
        self.bs = ("QPushButton {"
                   'font: normal normal 15px "微软雅黑";'
                   "background-color:rgba(200,200,200,0);"
                   "}"
                   "QPushButton:hover {"
                   'font: normal normal 16px "微软雅黑";'
                   "background-color:rgba(200,200,200,0.5);"
                   "}"
                   "QPushButton:pressed {"
                   'font: normal normal 17px "微软雅黑";'
                   "background-color:rgba(180,180,180,0.7);"
                   "}"
                   )
        self.__bs = ("QPushButton {"
                     "background-color:rgba(200,200,200,0);"
                     "}"
                     "QPushButton:hover {"
                     "background-color:rgba(200,200,200,0);"
                     "}"
                     "QPushButton:pressed {"
                     "background-color:rgba(180,180,180,0);"
                     "}"
                     )
        self.button0 = QPushButton("系统", self)
        self.button0.setGeometry(0, self.th, self.bw, self.bh)
        self.button0.setStyleSheet(self.bs)
        self.button1 = QPushButton("设备", self)
        self.button1.setGeometry(0, self.th + self.bh, self.bw, self.bh)
        self.button1.setStyleSheet(self.bs)
        self.button2 = QPushButton("账户", self)
        self.button2.setGeometry(0, self.th + self.bh * 2, self.bw, self.bh)
        self.button2.setStyleSheet(self.bs)
        self.button3 = QPushButton("应用", self)
        self.button3.setGeometry(0, self.th + self.bh * 3, self.bw, self.bh)
        self.button3.setStyleSheet(self.bs)
        self.button4 = QPushButton("隐私", self)
        self.button4.setGeometry(0, self.th + self.bh * 4, self.bw, self.bh)
        self.button4.setStyleSheet(self.bs)
        self.button5 = QPushButton("个性化", self)
        self.button5.setGeometry(0, self.th + self.bh * 5, self.bw, self.bh)
        self.button5.setStyleSheet(self.bs)
        self.button6 = QPushButton("搜索", self)
        self.button6.setGeometry(0, self.th + self.bh * 6, self.bw, self.bh)
        self.button6.setStyleSheet(self.bs)
        self.button7 = QPushButton("时间和语言", self)
        self.button7.setGeometry(0, self.th + self.bh * 7, self.bw, self.bh)
        self.button7.setStyleSheet(self.bs)
        self.button8 = QPushButton("更新和安全", self)
        self.button8.setGeometry(0, self.th + self.bh * 8, self.bw, self.bh)
        self.button8.setStyleSheet(self.bs)
        self.button9 = QPushButton(self)
        self.button9.setGeometry(0, self.button8.pos().y() + self.button8.size().height(), self.bw, 1080)
        self.button9.setStyleSheet(self.__bs)
        self.buttonl1 = QPushButton("关于设置", self)
        self.buttonl1.setGeometry(0, self.size().height() - self.bh, self.bw, self.bh)
        self.buttonl1.setStyleSheet(self.bs)
        self.buttonl1.raise_()

    def initmouseT(self):
        self.mouseT = QPushButton(self)
        self.mouseT.resize(100, 100)
        self.mouseT.setStyleSheet(
            'background-color: rgba(240,240,240,0.25);border-radius: 50px; border: 0px groove gray;border-style: outset;')
        self.mouseT.lower()

    def mouseMoveEvent(self, arg__1):
        super().mouseMoveEvent(arg__1)
        self.mouseT.lower()
        self.mouseT.move(arg__1.pos().x() - self.mouseT.size().width() // 2,
                         arg__1.pos().y() - self.mouseT.size().height() // 2)
