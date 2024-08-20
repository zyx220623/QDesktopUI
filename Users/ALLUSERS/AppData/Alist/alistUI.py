from os import system, devnull

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QWidget, QTabWidget, QScrollArea, QLayout, QListView, QLabel, QComboBox, QVBoxLayout, \
    QLineEdit, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView
from Starts.UIstart.windowui import FrameLessWindow
from subprocess import Popen, PIPE, DEVNULL


class _QComboBox(QComboBox):
    def wheelEvent(self, e):
        pass


class AlistApps(FrameLessWindow):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent, appname="Alist", apphandle=110002, ReSize=QSize(1200, 700))
        self.WindowTitleUI()
        self.STOP = Popen("taskkill /f /im alist.exe", stdout=DEVNULL, stderr=DEVNULL, shell=True)
        self.public_qss()
        self.font = QFont()
        self.font.setPointSize(15)
        self.setWindowTitle("Alist")
        self.setWindowIcon(QIcon("Users/ALLUSERS/AppData/Alist/icon.png"))
        self.setTabWidget()

    def setTabWidget(self):
        self.main_tab_widget = QTabWidget(self)
        self.main_tab_widget.setGeometry(0, self.title_height,
                                         self.size().width(),
                                         self.size().height() - self.title_height)
        self.body = QWebEngineView()
        self.body.load("http://127.0.0.1:5244")
        self.main_tab_widget.addTab(self.body, "Alist 主页")
        self.docs = QWebEngineView()
        self.docs.load("https://alist.nn.ci/zh/")
        self.main_tab_widget.addTab(self.docs, "Alist 文档")
        self.github = QWebEngineView()
        self.github.load("https://github.com/alist-org/alist")
        self.main_tab_widget.addTab(self.github, "GitHub 仓库")

    def WindowTitleUI(self):
        def mainWidgetButtonClickedEvent():
            self.switch_to_tab(self.main_tab_widget, "Alist 主页")
            self.main_widget_button.setStyleSheet(self.button_clicked_qss)
            self.doc_button.setStyleSheet(self.button_qss)
            self.github_button.setStyleSheet(self.button_qss)

        def mainWidgetButtonDoubleClickedEvent(event):
            self.body.load("http://127.0.0.1:5244")

        def docButtonDoubleClickedEvent(event):
            self.docs.load("https://alist.nn.ci/zh/")

        def docButtonClickedEvent():
            self.switch_to_tab(self.main_tab_widget, "Alist 文档")
            self.doc_button.setStyleSheet(self.button_clicked_qss)
            self.main_widget_button.setStyleSheet(self.button_qss)
            self.github_button.setStyleSheet(self.button_qss)

        def githubButtonClickedEvent():
            self.switch_to_tab(self.main_tab_widget, "GitHub 仓库")
            self.doc_button.setStyleSheet(self.button_qss)
            self.main_widget_button.setStyleSheet(self.button_qss)
            self.github_button.setStyleSheet(self.button_clicked_qss)

        def githubButtonDoubleClickedEvent(event):
            self.github.load("https://github.com/alist-org/alist")

        self.button_qss = ("QPushButton {"
                           'font: normal normal 17px "微软雅黑";'
                           "border: none;"
                           "background-color:rgb(255,255,255);"
                           "color:rgb(100,100,100);"
                           "}"
                           "QPushButton:hover {"
                           'font: normal bold 17px "微软雅黑";'
                           "}"
                           "QPushButton:pressed {"
                           'font: normal bold 18px "微软雅黑";'
                           "color:rgb(0,0,0);"
                           "}"
                           )
        self.button_clicked_qss = ("QPushButton {"
                                   'font: normal bold 18px "微软雅黑";'
                                   "border: none;"
                                   "background-color:rgb(255,255,255);"
                                   "color:rgb(0,0,0);"
                                   "}")
        self.main_widget_button = QPushButton("  Alist 主页", self)
        self.main_widget_button.setStyleSheet(self.button_clicked_qss)
        self.main_widget_button.setGeometry(self.title_height, 0, self.main_widget_button.size().width(),
                                            self.title_height - 2)
        self.main_widget_button.clicked.connect(mainWidgetButtonClickedEvent)
        self.main_widget_button.mouseDoubleClickEvent = mainWidgetButtonDoubleClickedEvent

        self.doc_button = QPushButton("  Alist 文档", self)
        self.doc_button.setStyleSheet(self.button_qss)
        self.doc_button.setGeometry(self.main_widget_button.pos().x() + self.main_widget_button.size().width(),
                                    0,
                                    self.doc_button.size().width(),
                                    self.title_height - 2)
        self.doc_button.clicked.connect(docButtonClickedEvent)
        self.doc_button.mouseDoubleClickEvent = docButtonDoubleClickedEvent

        self.github_button = QPushButton("  GitHub 仓库", self)
        self.github_button.setStyleSheet(self.button_qss)
        self.github_button.setGeometry(self.doc_button.pos().x() + self.doc_button.size().width(),
                                       0,
                                       self.github_button.size().width() + 15,
                                       self.title_height - 2)
        self.github_button.clicked.connect(githubButtonClickedEvent)
        self.github_button.mouseDoubleClickEvent = githubButtonDoubleClickedEvent

        self.main_widget_button.raise_()
        self.doc_button.raise_()
        self.github_button.raise_()

    def customTitleResizeEvent(self):
        self.main_widget_button.raise_()
        self.doc_button.raise_()
        self.github_button.raise_()

    def beforeResizeEventEvent(self):
        self.main_tab_widget.setGeometry(0, 12,
                                         self.size().width(),
                                         self.size().height() - 12)

    def show(self):
        system("Users\\ALLUSERS\\AppData\\Alist\\start.vbs " + devnull)
        super().show()

    def close(self):
        super().close()
        self.STOP = Popen("taskkill /f /im alist.exe", stdout=DEVNULL, stderr=DEVNULL, shell=True)

    def public_qss(self):
        self.pqss_title = ("QLabel {"
                           'font: normal bold 25px "微软雅黑";'
                           "background-color:rgba(200,200,200,0);"
                           "}")
        self.pqss_2title = ("QLabel {"
                            'font: normal normal 22px "微软雅黑";'
                            "background-color:rgba(200,200,200,0);"
                            "}")
        self.pqss_3title = ("QLabel {"
                            'font: normal normal 17px "微软雅黑";'
                            "background-color:rgba(200,200,200,0);"
                            "}")
        self.pqss_text = ("QLabel {"
                          'font: normal normal 13px "微软雅黑";'
                          "background-color:rgba(200,200,200,0);"
                          "}")
        self.pqss_widget = "background-color:rgba(0,0,0,0);border:rgb(255,255,255);"
        self.pqss_conmo = '''
QComboBox
{
	background-color:rgba(60,60,60,0);
	font: 75 14px "微软雅黑";
    color:rgb(0,0,0);
    border:0px ;
	padding-top: 2px;
	padding-left: 2px;
}
QComboBox:disabled
{
	background-color:rgba(50,50,50,0);
	font: 75 13px "微软雅黑";
    color:rgb(0,0,0);
}
QComboBox:hover
{
	background-color:rgba(45,45,45,0);
	border:1px solid rgba(255,255,255,0) ;
}
QComboBox:on
{
	border-radius:3px;
	background-color:rgba(255,255,255,0);
	font: 75 12px "微软雅黑";
    color:rgb(0,0,0);
    border:1px solid rgba(255,255,255,0) ;
}
QComboBox QAbstractItemView 
{
    outline: 0px solid gray;
    border: 1px solid rgba(200,200,200,0);  
    font: 75 13px "微软雅黑";
    color: rgb(0,0,0);
    background-color: rgba(255,255,255,1);   
    selection-background-color: rgb(240,240,240);   
}
QComboBox QAbstractItemView::item
 { 
	height: 25px;  
 }
QComboBox QAbstractItemView::item:selected 
{
    color: rgb(10,10,10);
	background-color: rgb(200,200,200); 
}
QComboBox::drop-down 
{
	border:none;
}
QComboBox::down-arrow 
{
    right:10px;
    width: 9px;  
    height: 9px;   
}
QComboBox::down-arrow:on
{
    width: 9px;  
    height: 9px;   
}'''
