from PySide6.QtCore import (Qt,
                            QRect,
                            QSize,
                            QPoint)
from PySide6.QtGui import (QPixmap,
                           QMouseEvent,
                           QCursor,
                           QGuiApplication,
                           QIcon)
from PySide6.QtWidgets import (QPushButton,
                               QWidget,
                               QTabWidget,
                               QLayout,
                               QLabel,
                               QListView,
                               QComboBox,
                               QCheckBox)
from System.Settings.Settings.theme import THEME
from .switchbutton import SwitchButton
class _QComboBox(QComboBox):
    def wheelEvent(self, e):
        pass

class FrameLessWindow(QPushButton):
    edge: int

    def __NoneEvent(self, event: QMouseEvent | None = None):
        pass

    def __theme(self):
        self.theme = THEME
        if self.theme == "dark":
            self.button_hovered_color = [50, 50, 50, 1]
            self.minimum_color = [255, 255, 255, 1]
            self.title_background_color_rgba = [0, 0, 0, 1]
            self.title_text_color_rgba = [255, 255, 255, 1]
            self.__background_color_rgba = [0, 0, 0, 0.86]
        elif self.theme == "light":
            self.button_hovered_color = [230, 230, 230, 1]
            self.minimum_color = [0, 0, 0, 1]
            self.title_background_color_rgba = [255, 255, 255, 0.9]
            self.title_text_color_rgba = [0, 0, 0, 1]
            self.__background_color_rgba = [255, 255, 255, 0.95]

    def __attributeInit(self):
        self.__theme()
        self.movemode = 0
        self.is_mouse_pressed = False
        self.up_resized = False
        self.toDownPress = False
        self.left_resized = False
        self.toRightPress = False
        self.upleft_resized = False
        self.upright_resized = False
        self.downright_resized = False
        self.downleft_resized = False
        self.edge = 5
        self.beginning_pos_right = QCursor().pos()
        self.beginning_pos_up = QCursor().pos()
        self.beginning_pos_down = QCursor().pos()
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.__screen__ = QGuiApplication.primaryScreen().size()

    def __init__(self, appname: str = None, apphandle = None, parent: QWidget = None,
                 background_color_rgba: list[int] | tuple[int] | set[int] = (255, 255, 255, 0.9),
                 iconyes: bool = True,
                 taskbar_height: int = 50,
                 MinimumSize: QSize = QSize(400, 225),
                 ReSize: QSize = QSize(400, 225),
                 Position: QPoint | None = None,
                 title_height: int = 35,
                 themeBackground: bool = False):
        super(FrameLessWindow, self).__init__(parent)
        self.__attributeInit()
        self.__parent__ = parent
        self.setMinimumSize(MinimumSize)
        self.resize(ReSize)
        self.taskbar_height = taskbar_height
        self.appname = appname
        self.iconyes = iconyes
        self.apphandle = apphandle
        self.background_color_rgba = background_color_rgba
        if themeBackground:
            self.background_color_rgba = self.__background_color_rgba
        self.setStyleSheet("QPushButton {"
                           f"background-color:rgba({self.background_color_rgba[0]}, {self.background_color_rgba[1]}, {self.background_color_rgba[2]}, {self.background_color_rgba[3]});"
                           "border: none;"
                           "}")
        self.title_height = title_height
        self.__setMainWidget()
        self.__setThreeButton()
        if Position is not None:
            self.move(Position)
        else:
            self.move((self.__screen__.width() - self.size().width()) // 2,
                      (self.__screen__.height() - self.size().height() - self.taskbar_height) // 2)
        self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        self.main_widget.clicked.connect(self.windowClickedEvent)
        self.raise_()
        self.hide()

    def raise_(self):
        super().raise_()
        self.__parent__.taskbar.raise_()
        self.__parent__.startbutton.raise_()
        self.__parent__.backgroundClickedEvent()
    
    def show(self):
        super().show()
        self.raise_()
        self.__parent__.taskbar.raise_()
        self.__parent__.startbutton.raise_()
        self.__parent__.backgroundClickedEvent()
        self.showNormal()

    def setWindowTitle(self, arg__1):
        self.title = arg__1
        self.__setWindowTitleBar(background_color_rgba=self.title_background_color_rgba,
                                 color_rgba=self.title_text_color_rgba,
                                 title_height=self.title_height)

    def setWindowIcon(self, icon: QIcon | QPixmap):
        if self.iconyes:
            self.__icon__ = icon
            self.icon_image = QPushButton(self)
            self.icon_image.setIcon(icon)
            self.icon_image.setIconSize(QSize(self.title_height - 10, self.title_height - 10))
            self.icon_image.setFixedSize(self.title_height - 10, self.title_height - 10)
            self.icon_image.move(5, 5)
            self.icon_image.setStyleSheet("QPushButton {"
                                          "background-color: rgba(0,0,0,0);"
                                          "border: none;"
                                          "}")

    def resizeEvent(self, event):
        self.beforeResizeEventEvent()
        self.WindowTitleBar.setGeometry(self.edge * 3, 0, self.size().width(), 35)
        self.MoveableArea.setGeometry(0, 0, self.size().width(), self.title_height)
        self.ToUpArea.setGeometry(0, 0, self.size().width(), self.edge)
        self.ToDownArea.setGeometry(0, self.size().height() - self.edge, self.size().width(), self.edge)
        self.ToLeftArea.setGeometry(0, 0, self.edge, self.size().height())
        self.ToRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.size().height())
        self.main_widget.setGeometry(self.edge,
                                     self.title_height,
                                     self.size().width() - 2 * self.edge,
                                     self.size().height() - self.title_height - self.edge)
        self.UpRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.edge)
        self.DownRightArea.setGeometry(self.size().width() - self.edge, self.size().height() - self.edge, self.edge,
                                       self.edge)
        self.DownLeftArea.setGeometry(0, self.size().height() - self.edge, self.edge,
                                      self.edge)
        self.CloseButton.move(self.size().width() - self.CloseButton.size().width(), 0)
        self.MaximumButton.move(self.CloseButton.pos().x() - self.MaximumButton.size().width(), 0)
        self.MinimumButton.move(self.MaximumButton.pos().x() - self.MinimumButton.size().width(), 0)
        self.WindowTitleBackground.raise_()
        self.WindowTitleBar.raise_()
        self.MoveableArea.raise_()
        try:
            self.icon_image.raise_()
        except:
            pass
        self.customTitleResizeEvent()
        self.CloseButton.raise_()
        self.MaximumButton.raise_()
        self.MinimumButton.raise_()
        self.ToUpArea.raise_()
        self.ToRightArea.raise_()
        self.ToDownArea.raise_()
        self.ToLeftArea.raise_()
        self.UpRightArea.raise_()
        self.DownRightArea.raise_()
        self.UpLeftArea.raise_()
        self.DownLeftArea.raise_()

    def customTitleResizeEvent(self):
        pass

    def beforeResizeEventEvent(self):
        pass

    def __setMainWidget(self):
        self.main_widget = QPushButton(self)
        self.main_widget.setStyleSheet("QPushButton {"
                                       "border: none;"
                                       f"background-color: rgba({self.background_color_rgba[0]}, {self.background_color_rgba[1]}, {self.background_color_rgba[2]}, 0);"
                                       "border: none;"
                                       "}")
        self.main_widget.setGeometry(self.edge,
                                     self.title_height,
                                     self.size().width() - 2 * self.edge,
                                     self.size().height() - self.title_height - self.edge)

        self.main_widget.raise_()

    def __setNoneEvent(self):
        self.ToUpArea.mouseMoveEvent = self.__NoneEvent
        self.ToUpArea.mousePressEvent = self.__NoneEvent
        self.ToUpArea.mouseReleaseEvent = self.__NoneEvent
        self.ToDownArea.mouseMoveEvent = self.__NoneEvent
        self.ToDownArea.mousePressEvent = self.__NoneEvent
        self.ToDownArea.mouseReleaseEvent = self.__NoneEvent
        self.ToLeftArea.mouseMoveEvent = self.__NoneEvent
        self.ToLeftArea.mousePressEvent = self.__NoneEvent
        self.ToLeftArea.mouseReleaseEvent = self.__NoneEvent
        self.ToRightArea.mouseMoveEvent = self.__NoneEvent
        self.ToRightArea.mousePressEvent = self.__NoneEvent
        self.ToRightArea.mouseReleaseEvent = self.__NoneEvent
        self.UpLeftArea.mouseMoveEvent = self.__NoneEvent
        self.UpLeftArea.mousePressEvent = self.__NoneEvent
        self.UpLeftArea.mouseReleaseEvent = self.__NoneEvent
        self.UpRightArea.mouseMoveEvent = self.__NoneEvent
        self.UpRightArea.mousePressEvent = self.__NoneEvent
        self.UpRightArea.mouseReleaseEvent = self.__NoneEvent
        self.DownRightArea.mouseMoveEvent = self.__NoneEvent
        self.DownRightArea.mousePressEvent = self.__NoneEvent
        self.DownRightArea.mouseReleaseEvent = self.__NoneEvent
        self.DownLeftArea.mouseMoveEvent = self.__NoneEvent
        self.DownLeftArea.mousePressEvent = self.__NoneEvent
        self.DownLeftArea.mouseReleaseEvent = self.__NoneEvent

    def __isNoneEvent(self):
        result = True
        for i in (self.ToUpArea.mouseMoveEvent == self.__NoneEvent,
                  self.ToUpArea.mousePressEvent == self.__NoneEvent,
                  self.ToUpArea.mouseReleaseEvent == self.__NoneEvent,
                  self.ToDownArea.mouseMoveEvent == self.__NoneEvent,
                  self.ToDownArea.mousePressEvent == self.__NoneEvent,
                  self.ToDownArea.mouseReleaseEvent == self.__NoneEvent,
                  self.ToLeftArea.mouseMoveEvent == self.__NoneEvent,
                  self.ToLeftArea.mousePressEvent == self.__NoneEvent,
                  self.ToLeftArea.mouseReleaseEvent == self.__NoneEvent,
                  self.ToRightArea.mouseMoveEvent == self.__NoneEvent,
                  self.ToRightArea.mousePressEvent == self.__NoneEvent,
                  self.ToRightArea.mouseReleaseEvent == self.__NoneEvent,
                  self.UpLeftArea.mouseMoveEvent == self.__NoneEvent,
                  self.UpLeftArea.mousePressEvent == self.__NoneEvent,
                  self.UpLeftArea.mouseReleaseEvent == self.__NoneEvent,
                  self.UpRightArea.mouseMoveEvent == self.__NoneEvent,
                  self.UpRightArea.mousePressEvent == self.__NoneEvent,
                  self.UpRightArea.mouseReleaseEvent == self.__NoneEvent,
                  self.DownRightArea.mouseMoveEvent == self.__NoneEvent,
                  self.DownRightArea.mousePressEvent == self.__NoneEvent,
                  self.DownRightArea.mouseReleaseEvent == self.__NoneEvent,
                  self.DownLeftArea.mouseMoveEvent == self.__NoneEvent,
                  self.DownLeftArea.mousePressEvent == self.__NoneEvent,
                  self.DownLeftArea.mouseReleaseEvent == self.__NoneEvent):
            if not i:
                result = False
                break
        return result

    def __setNormalEvent(self):
        self.ToUpArea.mouseMoveEvent = self.__toUpMoveEvent
        self.ToUpArea.mousePressEvent = self.__toUpPressEvent
        self.ToUpArea.mouseReleaseEvent = self.__toUpReleaseEvent
        self.ToDownArea.mouseMoveEvent = self.__toDownMoveEvent
        self.ToDownArea.mousePressEvent = self.__toDownPressEvent
        self.ToDownArea.mouseReleaseEvent = self.__toDownReleaseEvent
        self.ToLeftArea.mouseMoveEvent = self.__toLeftMoveEvent
        self.ToLeftArea.mousePressEvent = self.__toLeftPressEvent
        self.ToLeftArea.mouseReleaseEvent = self.__toLeftReleaseEvent
        self.ToRightArea.mouseMoveEvent = self.__toRightMoveEvent
        self.ToRightArea.mousePressEvent = self.__toRightPressEvent
        self.ToRightArea.mouseReleaseEvent = self.__toRightReleaseEvent
        self.MoveableArea.mousePressEvent = self.__movePressEvent
        self.MoveableArea.mouseMoveEvent = self.__moveMoveEvent
        self.MoveableArea.mouseReleaseEvent = self.__moveReleaseEvent
        self.MoveableArea.mouseDoubleClickEvent = self.__titleDoubleClickedEvent
        self.UpLeftArea.mouseMoveEvent = self.__UpLeftMoveEvent
        self.UpLeftArea.mousePressEvent = self.__UpLeftPressEvent
        self.UpLeftArea.mouseReleaseEvent = self.__UpLeftReleaseEvent
        self.UpRightArea.mouseMoveEvent = self.__UpRightMoveEvent
        self.UpRightArea.mousePressEvent = self.__UpRightPressEvent
        self.UpRightArea.mouseReleaseEvent = self.__UpRightReleaseEvent
        self.DownRightArea.mouseMoveEvent = self.__DownRightMoveEvent
        self.DownRightArea.mousePressEvent = self.__DownRightPressEvent
        self.DownRightArea.mouseReleaseEvent = self.__DownRightReleaseEvent
        self.DownLeftArea.mouseMoveEvent = self.__DownLeftMoveEvent
        self.DownLeftArea.mousePressEvent = self.__DownLeftPressEvent
        self.DownLeftArea.mouseReleaseEvent = self.__DownLeftReleaseEvent

    def showMaximized(self):
        """自定义最大化方法"""
        self.MaximumButton.setIcon(QIcon(f"Starts/UIstart/desktopimage/{self.theme}/normal.png"))
        self.setGeometry(0, 0, self.__screen__.width(), self.__screen__.height() - self.taskbar_height)
        self.__setNoneEvent()

    def showMinimized(self):
        pass

    def showLined(self):
        self.setGeometry(self.pos().x(), 0, self.size().width(), self.__screen__.height() - self.taskbar_height)
        self.__setNoneEvent()

    def showNormal(self):
        self.setGeometry(self.normal_geometry.x(), self.normal_geometry.y(), self.normal_geometry.width(),
                         self.normal_geometry.height())
        self.MaximumButton.setIcon(QIcon(f"Starts/UIstart/desktopimage/{self.theme}/max.png"))
        self.__setNormalEvent()
        if self.pos().y() <= 5 and self.__isLined() is not True:
            self.move(self.normal_geometry.x(), 5)

    def showSizeNormal(self):
        self.resize(self.normal_geometry.width(), self.normal_geometry.height())
        self.MaximumButton.setIcon(QIcon(f"Starts/UIstart/desktopimage/{self.theme}/max.png"))
        self.__setNormalEvent()

    def showUpLeft(self):
        self.setGeometry(0, 0, self.__screen__.width() // 2,
                         (self.__screen__.height() - self.taskbar_height) // 2)
        self.__setNoneEvent()

    def showFullLeft(self):
        self.setGeometry(0, 0, self.__screen__.width() // 2,
                         self.__screen__.height() - self.taskbar_height)
        self.__setNoneEvent()

    def showDownLeft(self):
        self.setGeometry(0, (self.__screen__.height() - self.taskbar_height) // 2,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - self.taskbar_height) // 2)
        self.__setNoneEvent()

    def showUpRight(self):
        self.setGeometry(self.__screen__.width() // 2, 0,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - self.taskbar_height) // 2)
        self.__setNoneEvent()

    def showDownRight(self):
        self.setGeometry(self.__screen__.width() // 2,
                         (self.__screen__.height() - self.taskbar_height) // 2,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - self.taskbar_height) // 2)
        self.__setNoneEvent()

    def showFullRight(self):
        self.setGeometry(self.__screen__.width() // 2, 0,
                         self.__screen__.width() // 2,
                         self.__screen__.height() - self.taskbar_height)
        self.__setNoneEvent()

    def isMaximized(self) -> bool:
        """自定义最大化规则"""
        if (self.pos().x() == 0 and
                self.pos().y() == 0 and
                self.size().width() == self.__screen__.width() and
                self.size().height() == self.__screen__.height() - self.taskbar_height):
            return True
        else:
            return False

    def __isLined(self) -> bool:
        if self.size().height() == self.__screen__.height() - self.taskbar_height and self.pos().y() == 0:
            return True
        else:
            return False

    def __isFullSide(self) -> bool:
        if self.size().width() == self.__screen__.width() // 2 and \
                self.size().height() == self.__screen__.height() - self.taskbar_height and \
                self.pos().y() == 0:
            if self.pos().x() == self.__screen__.width() // 2 or \
                    self.pos().x() == 0:
                return True
            else:
                return False
        else:
            return False

    def __isFullCorner(self) -> bool:
        result = True
        if (self.size().width() != self.__screen__.width() // 2 or self.size().height() != (
                self.__screen__.height() - self.taskbar_height) // 2) and \
                (self.pos().x() <= 5 or self.pos().x() != self.__screen__.width() // 2) and \
                (self.pos().y() <= 5 or self.pos().y() != (self.__screen__.height() - self.taskbar_height) // 2):
            result = False
        return result

    def __titleDoubleClickedEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.isMaximized() or self.__isLined() or self.__isFullCorner() or self.__isFullSide():
                self.showNormal()
                self.__parent__.startMenuHideEvent()
            else:
                self.showMaximized()
                self.__parent__.startMenuHideEvent()

    def __setWindowTitleBar(self,
                            background_color_rgba: tuple[int] | list[int] | set[int] = (0, 0, 0, 1),
                            color_rgba: tuple[int] | list[int] | set[int] = (255, 255, 255, 1),
                            title_height: int = 35):
        try:
            self.title
        except:
            self.title = ""
        self.title_height = title_height
        self.WindowTitleBackground = QPushButton(self)
        self.WindowTitleBackground.setStyleSheet("QPushButton {"
                                                 f"background-color: rgba({background_color_rgba[0]}, {background_color_rgba[1]}, {background_color_rgba[2]}, {background_color_rgba[3]});"
                                                 "border: none;"
                                                 "}")
        self.WindowTitleBackground.setGeometry(0, 0, self.__screen__.width(), title_height)
        if self.iconyes:
            self.WindowTitleBar = QPushButton("     " + self.title, self)
        else:
            self.WindowTitleBar = QPushButton(self.title, self)
        self.WindowTitleBar.setGeometry(self.edge, 0, self.size().width(), title_height)
        self.WindowTitleBar.setStyleSheet("QPushButton {"
                                          "text-align: left;"
                                          'font: normal normal 18px "微软雅黑";'
                                          f"background-color: rgba(0,0,0,0);"
                                          f"color: rgba({color_rgba[0]}, {color_rgba[1]}, {color_rgba[2]}, {color_rgba[3]});"
                                          "border: none;"
                                          "}")
        self.__setMoveableArea()

    def __setMinimumButton(self):
        self.MinimumButton = QPushButton("—", self)
        self.MinimumButton.setStyleSheet("QPushButton {"
                                         "background-color: rgba(25, 25, 25, 0);"
                                         f"color: rgba({self.minimum_color[0]}, {self.minimum_color[1]}, {self.minimum_color[2]}, 1);"
                                         "border: none;"
                                         "}"
                                         "QPushButton:hover {"
                                         f"background-color: rgba({self.button_hovered_color[0]},{self.button_hovered_color[1]}, {self.button_hovered_color[2]}, 1);"
                                         f"color: rgba({self.minimum_color[0]}, {self.minimum_color[1]}, {self.minimum_color[2]}, 1);"
                                         "}")
        self.MinimumButton.resize(self.title_height, self.title_height)
        self.MinimumButton.move(self.MaximumButton.pos().x() - self.MinimumButton.size().width(), 0)
        self.MinimumButton.clicked.connect(self.showMinimized)

    def __setMaximumButton(self):
        self.MaximumButton = QPushButton(self)
        self.MaximumButton.setIcon(QIcon(f"Starts/UIstart/desktopimage/{self.theme}/max.png"))
        self.MaximumButton.setIconSize(QSize(self.title_height - 20, self.title_height - 20))
        self.MaximumButton.resize(self.title_height, self.title_height)
        self.MaximumButton.setStyleSheet("QPushButton {"
                                         f"background-color: rgba(0, 0, 0, 0);"
                                         "color: rgba(255,255,255,1);"
                                         "border: none;"
                                         "}"
                                         "QPushButton:hover{"
                                         f"background-color: rgba({self.button_hovered_color[0]},{self.button_hovered_color[1]}, {self.button_hovered_color[2]}, 1);"
                                         "color: rgba(255,255,255,1);"
                                         "}")
        self.MaximumButton.move(self.CloseButton.pos().x() - self.MaximumButton.size().width(), 0)
        self.MaximumButton.clicked.connect(self.MaximumButtonClickedEvent)

    def __setCloseButton(self):
        self.CloseButton = QPushButton(self)
        self.CloseButton.resize(self.title_height, self.title_height)
        self.CloseButton.setIcon(QIcon(f"Starts/UIstart/desktopimage/{self.theme}/close.png"))
        self.CloseButton.setIconSize(QSize(self.title_height - 20, self.title_height - 20))
        self.CloseButton.setStyleSheet("QPushButton {"
                                       "background-color: rgba(25, 25, 25, 0);"
                                       "color: rgba(255,255,255,1);"
                                       "border: none;"
                                       "}"
                                       "QPushButton:hover {"
                                       "background-color: rgba(250, 0, 0, 1);"
                                       f"icon: url('Starts/UIstart/desktopimage/{self.theme}/closeHover.png');"
                                       "color: rgba(255,255,255,1);"
                                       "}")
        self.CloseButton.move(self.size().width() - self.CloseButton.size().width(), 0)
        self.CloseButton.raise_()
        self.CloseButton.clicked.connect(self.close)

    def __setThreeButton(self):
        self.__setCloseButton()
        self.__setMaximumButton()
        self.__setMinimumButton()

    def MaximumButtonClickedEvent(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def __setMoveableArea(self):
        self.MoveableArea = QPushButton(self)
        self.MoveableArea.setStyleSheet("QPushButton {"
                                        "background-color: rgba(255,255,255,0);"
                                        "border: none;"
                                        "}")
        self.MoveableArea.setGeometry(0, 0, self.size().width(), self.title_height)
        self.MoveableArea.mousePressEvent = self.__movePressEvent
        self.MoveableArea.mouseMoveEvent = self.__moveMoveEvent
        self.MoveableArea.mouseReleaseEvent = self.__moveReleaseEvent
        self.MoveableArea.mouseDoubleClickEvent = self.__titleDoubleClickedEvent
        self.__setToUpArea()

    def mousePressEvent(self, e):
        self.beforeMousePressEventEvent()
        self.raise_()
        self.__parent__.taskbar.raise_()
        self.__parent__.startbutton.raise_()
        self.__parent__.backgroundClickedEvent()
        self.afterMousePressEventEvent()

    def beforeMousePressEventEvent(self):
        pass

    def afterMousePressEventEvent(self):
        pass

    def __setToUpArea(self):
        self.ToUpArea = QPushButton(self.MoveableArea)
        self.ToUpArea.setStyleSheet("QPushButton {"
                                    "background-color: rgba(255,255,255,0);"
                                    "border: none;"
                                    "}")
        self.ToUpArea.setGeometry(0, 0, self.size().width(), self.edge)
        self.ToUpArea.setCursor(Qt.CursorShape.SizeVerCursor)
        self.ToUpArea.mouseMoveEvent = self.__toUpMoveEvent
        self.ToUpArea.mousePressEvent = self.__toUpPressEvent
        self.ToUpArea.mouseReleaseEvent = self.__toUpReleaseEvent
        self.__setToDownArea()

    def __setToDownArea(self):
        self.ToDownArea = QPushButton(self)
        self.ToDownArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.ToDownArea.setGeometry(0, self.size().height() - self.edge, self.size().width(), self.edge)
        self.ToDownArea.setCursor(Qt.CursorShape.SizeVerCursor)
        self.ToDownArea.mouseMoveEvent = self.__toDownMoveEvent
        self.ToDownArea.mousePressEvent = self.__toDownPressEvent
        self.ToDownArea.mouseReleaseEvent = self.__toDownReleaseEvent
        self.__setToLeftArea()

    def __setToLeftArea(self):
        self.ToLeftArea = QPushButton(self)
        self.ToLeftArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.ToLeftArea.setGeometry(0, 0, self.edge, self.size().height())
        self.ToLeftArea.setCursor(Qt.CursorShape.SizeHorCursor)
        self.ToLeftArea.mouseMoveEvent = self.__toLeftMoveEvent
        self.ToLeftArea.mousePressEvent = self.__toLeftPressEvent
        self.ToLeftArea.mouseReleaseEvent = self.__toLeftReleaseEvent
        self.__setToRightArea()

    def __setToRightArea(self):
        self.ToRightArea = QPushButton(self)
        self.ToRightArea.setStyleSheet("QPushButton {"
                                       "background-color: rgba(255,255,255,0);"
                                       "border: none;"
                                       "}")
        self.ToRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.size().height())
        self.ToRightArea.setCursor(Qt.CursorShape.SizeHorCursor)
        self.ToRightArea.mouseMoveEvent = self.__toRightMoveEvent
        self.ToRightArea.mousePressEvent = self.__toRightPressEvent
        self.ToRightArea.mouseReleaseEvent = self.__toRightReleaseEvent
        self.__setUpLeftArea()

    def __toRightPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.right_click_position = event.globalPosition().toPoint() - self.pos()
            self.beginning_pos_x = QCursor.pos().x()
            self.toRightPress = True
            self._width_ = self.size().width()
            self.__parent__.startMenuHideEvent()

    def __toRightMoveEvent(self, event: QMouseEvent):
        if self.toRightPress and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_x), self.size().height())
        event.accept()

    def __toRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toRightPress = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __movePressEvent(self, event: QMouseEvent):
        self.raise_()
        self.__parent__.taskbar.raise_()
        self.__parent__.startbutton.raise_()
        self.__parent__.backgroundClickedEvent()
        if event.button() == Qt.MouseButton.LeftButton and \
                event.position().y() <= self.title_height:
            self.is_mouse_pressed = True
            self.mouse_click_position = event.globalPosition().toPoint() - self.pos()
            if self.isMaximized():
                self.movemode = 1
            elif self.__isFullSide():
                self.movemode = 3
            elif self.__isFullCorner():
                self.movemode = 4
            elif self.__isLined():
                self.movemode = 2
            else:
                self.movemode = 0
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __moveMoveEvent(self, event: QMouseEvent):
        if self.is_mouse_pressed:
            if self.movemode == 0:
                self.move(event.globalPosition().toPoint() - self.mouse_click_position)
            elif self.movemode == 3:
                self.showSizeNormal()
                self.move(
                    event.globalPosition().toPoint().x() - self.mouse_click_position.x() * self.normal_geometry.width() // (
                            self.__screen__.width() // 2),
                    (event.globalPosition().toPoint() - self.mouse_click_position).y())
            elif self.movemode == 1:
                self.showSizeNormal()
                self.move(
                    event.globalPosition().toPoint().x() - self.mouse_click_position.x() * self.normal_geometry.width() // QGuiApplication.primaryScreen().geometry().width(),
                    (event.globalPosition().toPoint() - self.mouse_click_position).y())
            elif self.movemode == 4:
                self.showSizeNormal()
                self.move(
                    event.globalPosition().toPoint().x() - self.mouse_click_position.x() * self.normal_geometry.width() // (
                            self.__screen__.width() // 2),
                    (event.globalPosition().toPoint() - self.mouse_click_position).y())
            elif self.movemode == 2:
                self.showSizeNormal()
                self.move(event.globalPosition().toPoint() - self.mouse_click_position)

        event.accept()

    def __moveReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_mouse_pressed = False
            if QCursor.pos().y() <= 0 and self.__screen__.width() - 5 > QCursor.pos().x() > 5:
                self.showMaximized()
            elif QCursor.pos().x() <= 5 and QCursor.pos().y() <= 5:
                self.showUpLeft()
            elif QCursor.pos().x() >= self.__screen__.width() - 5 and QCursor.pos().y() <= 5:
                self.showUpRight()
            elif QCursor.pos().x() <= 5 and QCursor.pos().y() >= self.__screen__.height() - self.taskbar_height:
                self.showDownLeft()
            elif QCursor.pos().y() >= self.__screen__.height() - self.taskbar_height and \
                    QCursor.pos().x() >= self.__screen__.width() - 5:
                self.showDownRight()
            elif QCursor.pos().x() <= 5 <= QCursor.pos().y() <= self.__screen__.height() - 5:
                self.showFullLeft()
            elif QCursor.pos().x() >= self.__screen__.width() - 5 and \
                    self.__screen__.height() - 5 >= QCursor.pos().y() >= 5:
                self.showFullRight()
            elif QCursor.pos().y() >= self.__screen__.height() - self.taskbar_height and 5 <= QCursor.pos().x() <= self.__screen__.width() - 5:
                self.setGeometry(self.normal_geometry.x(), self.normal_geometry.y(), self.normal_geometry.width(),
                                 self.normal_geometry.height())
            elif not (self.isMaximized() or self.__isLined() or self.__isFullSide() or self.__isFullCorner()):
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __toUpPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and \
                event.position().y() <= self.edge:
            self.up_resized = True
            self.up_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos_y = QCursor().pos().y()
            self.justnow_size_list = []
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __toUpMoveEvent(self, event: QMouseEvent):
        if self.up_resized and self.size().height() + self.pos().y() - QCursor.pos().y() >= self.minimumHeight():
            self.resize(self._width_, self._height_ - QCursor.pos().y() + self.beginning_pos_y)
            self.move(self._x_, (event.globalPosition().toPoint() - self.up_click_position).y())
        event.accept()

    def __toUpReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.up_resized = False
            if QCursor.pos().y() <= 0 and QGuiApplication.primaryScreen().geometry().width() - 5 > QCursor.pos().x() > 5:
                self.showLined()
            else:
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __toDownPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.down_click_position = event.globalPosition().toPoint() - self.pos()
            self.beginning_pos_y = QCursor.pos().y()
            self._height_ = self.size().height()
            self.toDownPress = True
        self.__parent__.startMenuHideEvent()

    def __toDownMoveEvent(self, event: QMouseEvent):
        if self.toDownPress and QCursor.pos().y() >= self.minimumHeight() + self.pos().y():
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_y))
        event.accept()

    def __toDownReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toDownPress = False
            if QCursor.pos().y() >= self.__screen__.height() - self.taskbar_height and \
                    5 <= QCursor.pos().x() <= self.__screen__.width() - self.edge:
                self.showLined()
            else:
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __toLeftPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and \
                event.position().x() <= self.edge:
            self.left_resized = True
            self.left_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos_x = QCursor().pos().x()
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __toLeftMoveEvent(self, event: QMouseEvent):
        if self.left_resized and self.pos().x() + self.size().width() - QCursor.pos().x() >= self.minimumWidth():
            self.resize(self._width_ - QCursor.pos().x() + self.beginning_pos_x, self.height())
            self.move((event.globalPosition().toPoint() - self.left_click_position).x(), self._y_)
        event.accept()

    def __toLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.left_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __setUpLeftArea(self):
        self.UpLeftArea = QPushButton(self)
        self.UpLeftArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.UpLeftArea.setGeometry(0, 0, self.edge, self.edge)
        self.UpLeftArea.setCursor(Qt.CursorShape.SizeFDiagCursor)
        self.UpLeftArea.mouseMoveEvent = self.__UpLeftMoveEvent
        self.UpLeftArea.mousePressEvent = self.__UpLeftPressEvent
        self.UpLeftArea.mouseReleaseEvent = self.__UpLeftReleaseEvent
        self.__setUpRightArea()

    def __UpLeftPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upleft_resized = True
            self.upleft_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos = QCursor().pos()
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __UpLeftMoveEvent(self, event: QMouseEvent):
        if self.upleft_resized and \
                self.pos().x() + self.size().width() - QCursor.pos().x() >= self.minimumWidth():
            self.resize(self._width_ - QCursor.pos().x() + self.beginning_pos.x(),
                        self.size().height())
            self.move((event.globalPosition().toPoint() - self.upleft_click_position).x(), self.pos().y())
        if self.upleft_resized and \
                self.pos().y() + self.size().height() - QCursor.pos().y() >= self.minimumHeight():
            self.resize(self.size().width(),
                        self._height_ - QCursor.pos().y() + self.beginning_pos.y())
            self.move(self.pos().x(), (event.globalPosition().toPoint() - self.upleft_click_position).y())
        event.accept()

    def __UpLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upleft_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __setUpRightArea(self):
        self.UpRightArea = QPushButton(self)
        self.UpRightArea.setStyleSheet("QPushButton {"
                                       "background-color: rgba(255,255,255,0);"
                                       "border: none;"
                                       "}")
        self.UpRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.edge)
        self.UpRightArea.setCursor(Qt.CursorShape.SizeBDiagCursor)
        self.UpRightArea.mouseMoveEvent = self.__UpRightMoveEvent
        self.UpRightArea.mousePressEvent = self.__UpRightPressEvent
        self.UpRightArea.mouseReleaseEvent = self.__UpRightReleaseEvent
        self.__setDownRightArea()

    def __UpRightPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upright_resized = True
            self.upleft_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos_right = QCursor().pos()
            self.beginning_pos_up = QCursor().pos()
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __UpRightMoveEvent(self, event: QMouseEvent):
        if self.upright_resized and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_right.x()), self.size().height())
        if self.upright_resized and self.pos().y() + self.size().height() - QCursor.pos().y() >= self.minimumHeight():
            self.resize(self.width(), self._height_ - QCursor.pos().y() + self.beginning_pos_up.y())
            self.move(self._x_, (event.globalPosition().toPoint() - self.upleft_click_position).y())
        event.accept()

    def __UpRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upright_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __setDownRightArea(self):
        self.DownRightArea = QPushButton(self)
        self.DownRightArea.setStyleSheet("QPushButton {"
                                         "background-color: rgba(255,255,255,0);"
                                         "border: none;"
                                         "}")
        self.DownRightArea.setGeometry(self.size().width() - self.edge, self.size().height() - self.edge, self.edge,
                                       self.edge)
        self.DownRightArea.setCursor(Qt.CursorShape.SizeFDiagCursor)
        self.DownRightArea.mouseMoveEvent = self.__DownRightMoveEvent
        self.DownRightArea.mousePressEvent = self.__DownRightPressEvent
        self.DownRightArea.mouseReleaseEvent = self.__DownRightReleaseEvent
        self.__setDownLeftArea()

    def __DownRightPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downright_resized = True
            self.upleft_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos_right = QCursor().pos()
            self.beginning_pos_down = QCursor().pos()
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __DownRightMoveEvent(self, event: QMouseEvent):
        if self.downright_resized and (
                event.globalPosition().toPoint() - self.pos()).y() >= self.minimumHeight() - self.edge:
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_down.y()))
        if self.downright_resized and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_right.x()), self.size().height())
        event.accept()

    def __DownRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downright_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def __setDownLeftArea(self):
        self.DownLeftArea = QPushButton(self)
        self.DownLeftArea.setStyleSheet("QPushButton {"
                                        "background-color: rgba(255,255,255,0);"
                                        "border: none;"
                                        "}")
        self.DownLeftArea.setGeometry(0, self.size().height() - self.edge, self.edge,
                                      self.edge)
        self.DownLeftArea.setCursor(Qt.CursorShape.SizeBDiagCursor)
        self.DownLeftArea.mouseMoveEvent = self.__DownLeftMoveEvent
        self.DownLeftArea.mousePressEvent = self.__DownLeftPressEvent
        self.DownLeftArea.mouseReleaseEvent = self.__DownLeftReleaseEvent

    def __DownLeftPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downleft_resized = True
            self.upleft_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos_left = QCursor().pos()
            self.beginning_pos_down = QCursor().pos()
        event.accept()
        self.__parent__.startMenuHideEvent()

    def __DownLeftMoveEvent(self, event: QMouseEvent):
        if self.downleft_resized and (
                event.globalPosition().toPoint() - self.pos()).y() >= self.minimumHeight() - self.edge:
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_down.y()))
        if self.downleft_resized and self.pos().x() + self.size().width() - QCursor.pos().x() >= self.minimumWidth():
            self.resize(self._width_ - QCursor.pos().x() + self.beginning_pos_left.x(), self.size().height())
            self.move((event.globalPosition().toPoint() - self.upleft_click_position).x(), self._y_)
        event.accept()

    def __DownLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downleft_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def close(self):
        super().close()
        try:
            self.__parent__.tasklist.remove(self.appname)
        except:
            pass

    def windowClickedEvent(self):
        self.raise_()
        self.__parent__.startMenuHideEvent()

    @staticmethod
    def switch_to_tab(tab_widget: QTabWidget, tab_title: str):
        for index in range(tab_widget.count()):
            if tab_widget.tabText(index) == tab_title:
                tab_widget.setCurrentIndex(index)

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
