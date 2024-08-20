from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QIcon, QPixmap, QAction, QFont
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QToolBar, QLineEdit, QProgressBar, QLabel, QMainWindow, QTabWidget, QStatusBar, QWidget, \
    QPushButton


class BrowserEngineView(QWebEngineView):
    tabs = []

    def __init__(self, Main, parent=None):
        super(BrowserEngineView, self).__init__(parent)
        self.mainWindow = Main

    def createWindow(self, QWebEnginePage_WebWindowType):
        webview = BrowserEngineView(self.mainWindow)
        tab = BrowserTab(self.mainWindow)
        tab.browser = webview
        tab.setCentralWidget(tab.browser)
        self.tabs.append(tab)
        self.mainWindow.add_new_tab(tab)
        return webview


class BrowserTab(QMainWindow):
    def __init__(self, Main, parent=None):
        super(BrowserTab, self).__init__(parent)
        self.mainWindow = Main
        self.browser = BrowserEngineView(self.mainWindow)
        self.browser.load(QUrl(""))
        self.setCentralWidget(self.browser)
        self.navigation_bar = QToolBar('Navigation')
        self.navigation_bar.setIconSize(QSize(32, 32))
        self.navigation_bar.setMovable(False)
        self.addToolBar(self.navigation_bar)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.back_button = QAction('后退', self)
        self.next_button = QAction('前进', self)
        self.stop_button = QAction('停止', self)
        self.refresh_button = QAction('刷新', self)
        self.home_button = QAction('主页', self)
        self.enter_button = QAction('转到', self)
        self.add_button = QAction('新建标签页', self)
        self.ssl_label1 = QLabel(self)
        self.ssl_label2 = QLabel(self)
        self.url_text_bar = QLineEdit(self)
        self.url_text_bar.setMinimumWidth(300)
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(120)
        self.set_button = QAction('设置', self)
        self.navigation_bar.addAction(self.back_button)
        self.navigation_bar.addAction(self.next_button)
        self.navigation_bar.addAction(self.stop_button)
        self.navigation_bar.addAction(self.refresh_button)
        self.navigation_bar.addAction(self.home_button)
        self.navigation_bar.addAction(self.add_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addWidget(self.ssl_label1)
        self.navigation_bar.addWidget(self.ssl_label2)
        self.navigation_bar.addWidget(self.url_text_bar)
        self.navigation_bar.addAction(self.enter_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addWidget(self.progress_bar)
        self.navigation_bar.addAction(self.set_button)
        self.status_label = QLabel()
        self.status_label.setText(" 基于 PySide 6 以及 QWebEngineView 的网页浏览器 - " + self.mainWindow.version)
        self.status_bar.addWidget(self.status_label)

    def navigate_to_url(self):
        s = QUrl(self.url_text_bar.text())
        if s.scheme() == '':
            s.setScheme('http')
        self.browser.load(s)

    def navigate_to_home(self):
        s = QUrl("http://cn.bing.com/")
        self.browser.load(s)

    def renew_urlbar(self, s):
        prec = s.scheme()
        if prec == 'http':
            self.ssl_label2.setText(" 不安全 ")
            self.ssl_label2.setStyleSheet("color:red;")
        elif prec == 'https':
            self.ssl_label2.setText(" 安全 ")
            self.ssl_label2.setStyleSheet("color:green;")
        self.url_text_bar.setText(s.toString())
        self.url_text_bar.setCursorPosition(0)

    def renew_progress_bar(self, p):
        self.progress_bar.setValue(p)


class BrowserWindow(QPushButton):
    name = "QEdge"
    version = "1.0 Beta 1"
    date = "2024.08.16"

    def __init__(self, parent: QWidget = None):
        super().__init__(parent=parent)
        self.setWindowTitle(self.name + " " + self.version)
        self.setWindowIcon(QIcon('Assets/main.png'))
        self.resize(1200, 900)
        self.__parent__ = parent
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setGeometry(0, 0, self.size().width(), self.size().height())
        self.tabs.setTabShape(QTabWidget.TabShape(0))
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        # self.tabs.currentChanged.connect(lambda i: self.setWindowTitle(self.tabs.tabText(i) + " - " + self.name))
        self.init_tab = BrowserTab(self)
        self.init_tab.browser.load(QUrl("http://cn.bing.com/"))
        self.add_new_tab(self.init_tab)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.tabs.setGeometry(0,0,self.size().width(), self.size().height())

    def add_blank_tab(self):
        blank_tab = BrowserTab(self)
        blank_tab.browser.load("http://cn.bing.com/")
        self.add_new_tab(blank_tab)

    def add_new_tab(self, tab):
        i = self.tabs.addTab(tab, "")
        self.tabs.setCurrentIndex(i)
        tab.back_button.triggered.connect(tab.browser.back)
        tab.next_button.triggered.connect(tab.browser.forward)
        tab.stop_button.triggered.connect(tab.browser.stop)
        tab.refresh_button.triggered.connect(tab.browser.reload)
        tab.home_button.triggered.connect(tab.navigate_to_home)
        tab.enter_button.triggered.connect(tab.navigate_to_url)
        tab.add_button.triggered.connect(self.add_blank_tab)
        tab.url_text_bar.returnPressed.connect(tab.navigate_to_url)
        tab.browser.urlChanged.connect(tab.renew_urlbar)
        tab.browser.loadProgress.connect(tab.renew_progress_bar)
        tab.browser.titleChanged.connect(lambda title: (self.tabs.setTabText(i, title),
                                                        self.tabs.setTabToolTip(i, title)))
        tab.browser.iconChanged.connect(lambda icon: self.tabs.setTabIcon(i, icon))

    def close_current_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)
        else:
            self.close()
            self.__parent__.close()

