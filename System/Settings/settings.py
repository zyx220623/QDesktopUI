from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QTabWidget, QPushButton, QLabel, QScrollArea, QHBoxLayout, QVBoxLayout, \
    QComboBox, QListView, QLayout, QCheckBox

from Starts.UIstart.windowui import FrameLessWindow, SwitchButton

class _QComboBox(QComboBox):
    def wheelEvent(self, e):
        pass

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
        self.__System()
        self.__computer()

    def __System(self):
        self.wt = QWidget()
        self.wt.setStyleSheet(self.pqss_widget)
        self.sys_topFiller = QWidget()
        # self.sys_topFiller.setMinimumSize(1000, 4500)
        self.systemUI()
        self.system_s = QScrollArea(self)
        self.system_s.setWidget(self.sys_topFiller)
        vbox = QVBoxLayout()
        vbox.addWidget(self.system_s)
        self.wt.setLayout(vbox)
        self.tabWidget.addTab(self.wt, "系统")

    def systemUI(self):
        self.system_l = QVBoxLayout(self.sys_topFiller)
        self.create_title("系统", self.pqss_title,
                          self.sys_topFiller, self.system_l)
        self.create_title("  屏幕", self.pqss_2title, self.sys_topFiller, self.system_l)
        self.create_title("   缩放与布局", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("    更改应用和文本的大小", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     100%（推荐）",
                           "     125%",
                           "     150%",
                           "     175%",
                           "     200%"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("    设置屏幕方向", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     横向",
                           "     纵向",
                           "     横向（翻转）",
                           "     纵向（翻转）"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("\n  通知和操作", self.pqss_2title, self.sys_topFiller, self.system_l)
        self.create_title("   通知", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("    获取来自应用和其他发送者的通知", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     获取所有通知",
                           "     仅获取本地和系统通知",
                           "     屏蔽所有通知"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("    在锁屏页面上显示通知", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     开",
                           "     关"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("    允许通知播放系统提示音", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     开",
                           "     关"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("\n  电源和睡眠", self.pqss_2title, self.sys_topFiller, self.system_l)
        self.create_title("   电源", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("    在接通电源且无任何操作的情况下，电脑经过以下时间后关闭：", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     从不",
                           "     30 分钟",
                           "     1 小时",
                           "     2 小时",
                           "     3 小时",
                           "     4 小时",
                           "     5 小时",
                           "     6 小时"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("   屏幕", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("    在接通电源且无任何操作的情况下，显示器经过以下时间后熄屏：", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     从不",
                           "     2 分钟",
                           "     5 分钟",
                           "     10 分钟",
                           "     20 分钟",
                           "     30 分钟",
                           "     1 小时",
                           "     2 小时",
                           "     3 小时",
                           "     4 小时",
                           "     5 小时"
                           ],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("   睡眠", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("    在接通电源且无任何操作的情况下，电脑经过以下时间后进入睡眠状态：", self.pqss_text, self.sys_topFiller, self.system_l)
        self.create_conmo(["     从不",
                           "     2 分钟",
                           "     5 分钟",
                           "     10 分钟",
                           "     20 分钟",
                           "     30 分钟",
                           "     1 小时",
                           "     2 小时",
                           "     3 小时",
                           "     4 小时",
                           "     5 小时"],
                          self.sys_topFiller,
                          self.system_l,
                          self.pqss_conmo,
                          None, None)
        self.create_title("\n  存储", self.pqss_2title, self.sys_topFiller, self.system_l)
        self.create_title("     虚拟系统不支持存储设置", self.pqss_text,
                          self.sys_topFiller, self.system_l)
        self.create_title("\n  关于", self.pqss_2title, self.sys_topFiller, self.system_l)
        self.create_title("   操作系统信息", self.pqss_3title, self.sys_topFiller, self.system_l)
        self.create_title("     系统名称\t\t\tQUISystem", self.pqss_text,
                          self.sys_topFiller, self.system_l)
        self.create_title("     系统版本号\t\t\t2024.1", self.pqss_text,
                          self.sys_topFiller, self.system_l)
        self.create_title("     操作系统内部版本\t\t241.00001.001", self.pqss_text,
                          self.sys_topFiller, self.system_l)

    def __computer(self):
        self.computerWidget = QWidget()
        self.computerWidget.setStyleSheet(self.pqss_widget)
        self.computer_Filler = QWidget()
        # self.sys_topFiller.setMinimumSize(1000, 4500)
        self.computer_UI()
        self.computer_SA = QScrollArea(self)
        self.computer_SA.setWidget(self.computer_Filler)
        computer_layout = QVBoxLayout()
        computer_layout.addWidget(self.computer_SA)
        self.wt.setLayout(computer_layout)
        self.tabWidget.addTab(self.wt, "设备")

    def computer_UI(self):
        pass

    @staticmethod
    def create_title(text: str,
                     stylesheet: str,
                     parent: QWidget,
                     layout: QLayout):
        title = QLabel()
        title.setText(text)
        title.setStyleSheet(stylesheet)
        layout.addWidget(title)
        parent.setLayout(layout)

    @staticmethod
    def create_conmo(text: list[str],
                     parent: QWidget,
                     layout: QLayout,
                     stylesheet: str = None,
                     event=None, c_text: str | int = None,
                     ):
        catalog = _QComboBox()
        catalog.addItems(text)
        catalog.setView(QListView())
        if c_text is not None:
            if isinstance(c_text, str):
                catalog.setCurrentText(c_text)
            elif isinstance(c_text, int):
                catalog.setCurrentIndex(c_text)
        if stylesheet is not None:
            catalog.setStyleSheet(stylesheet)
        if event is not None:
            catalog.currentIndexChanged.connect(event)
        layout.addWidget(catalog)
        parent.setLayout(layout)

    @staticmethod
    def create_check_box(text: str,
                         stylesheet: str,
                         layout: QLayout,
                         parent: QWidget,
                         event=None):
        checkbox = QCheckBox()
        checkbox.setText(text)
        checkbox.setStyleSheet(stylesheet)
        if event is not None:
            checkbox.stateChanged.connect(event)
        layout.addWidget(checkbox)
        parent.setLayout(layout)

    @staticmethod
    def switch_to_tab(tab_widget: QTabWidget, tab_title: str):
        for index in range(tab_widget.count()):
            if tab_widget.tabText(index) == tab_title:
                tab_widget.setCurrentIndex(index)
                break

    def open_tab_by_text_for_main(self, tab_title: str):
        self.switch_to_tab(self.tabWidget, tab_title)

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
