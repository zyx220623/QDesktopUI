from PySide6.QtCore import (Qt,
                            QRect,
                            QSize)
from PySide6.QtGui import (QPixmap,
                           QMouseEvent,
                           QCursor,
                           QGuiApplication)
from PySide6.QtWidgets import (QPushButton,
                               QWidget,
                               QApplication)


class FrameLessWindow(QPushButton):
    edge: int

    def NoneEvent(self, event: QMouseEvent | None = None):
        pass

    def __init__(self, appname: str = None, apphandle: int = None, parent: QWidget = None,
                 background_color_rgba: list[int] | tuple[int] | set[int] = (25, 25, 25, 0.9)):
        super(FrameLessWindow, self).__init__(parent)
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
        self.is_corner = False
        self.__screen__ = QGuiApplication.primaryScreen().size()
        self.edge = 5
        self.justnow_size = self.size()
        self.beginning_pos_right = QCursor().pos()
        self.beginning_pos_up = QCursor().pos()
        self.beginning_pos_down = QCursor().pos()
        self.setMouseTracking(True)
        self.setMinimumSize(960, 540)
        self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        self.appname = appname
        self.apphandle = apphandle
        self.parent_name = parent
        self.setStyleSheet("QPushButton {"
                           f"background-color: rgba({background_color_rgba[0]},{background_color_rgba[1]},{background_color_rgba[2]},{background_color_rgba[3]});"
                           "border: none;"
                           "}"
                           )
        self.setWindowTitleBar()
        self.setMainWidget()

    def setWindowTitle(self, arg__1):
        self.title = arg__1
        self.setWindowTitleBar()

    def setMainWidget(self):
        self.main_widget = QPushButton(self)
        self.main_widget.setStyleSheet("QPushButton {"
                                       "border: none;"
                                       "background-color: rgba(0, 0, 0, 0);"
                                       "}")
        self.main_widget.setGeometry(self.edge,
                                     self.title_height,
                                     self.size().width() - 2 * self.edge,
                                     self.size().height() - self.title_height - self.edge)

        self.main_widget.raise_()

    def setNoneEvent(self):
        self.ToUpArea.mouseMoveEvent = self.NoneEvent
        self.ToUpArea.mousePressEvent = self.NoneEvent
        self.ToUpArea.mouseReleaseEvent = self.NoneEvent
        self.ToDownArea.mouseMoveEvent = self.NoneEvent
        self.ToDownArea.mousePressEvent = self.NoneEvent
        self.ToDownArea.mouseReleaseEvent = self.NoneEvent
        self.ToLeftArea.mouseMoveEvent = self.NoneEvent
        self.ToLeftArea.mousePressEvent = self.NoneEvent
        self.ToLeftArea.mouseReleaseEvent = self.NoneEvent
        self.ToRightArea.mouseMoveEvent = self.NoneEvent
        self.ToRightArea.mousePressEvent = self.NoneEvent
        self.ToRightArea.mouseReleaseEvent = self.NoneEvent
        self.UpLeftArea.mouseMoveEvent = self.NoneEvent
        self.UpLeftArea.mousePressEvent = self.NoneEvent
        self.UpLeftArea.mouseReleaseEvent = self.NoneEvent
        self.UpRightArea.mouseMoveEvent = self.NoneEvent
        self.UpRightArea.mousePressEvent = self.NoneEvent
        self.UpRightArea.mouseReleaseEvent = self.NoneEvent
        self.DownRightArea.mouseMoveEvent = self.NoneEvent
        self.DownRightArea.mousePressEvent = self.NoneEvent
        self.DownRightArea.mouseReleaseEvent = self.NoneEvent
        self.DownLeftArea.mouseMoveEvent = self.NoneEvent
        self.DownLeftArea.mousePressEvent = self.NoneEvent
        self.DownLeftArea.mouseReleaseEvent = self.NoneEvent

    def isNoneEvent(self):
        result = True
        for i in (self.ToUpArea.mouseMoveEvent == self.NoneEvent,
                  self.ToUpArea.mousePressEvent == self.NoneEvent,
                  self.ToUpArea.mouseReleaseEvent == self.NoneEvent,
                  self.ToDownArea.mouseMoveEvent == self.NoneEvent,
                  self.ToDownArea.mousePressEvent == self.NoneEvent,
                  self.ToDownArea.mouseReleaseEvent == self.NoneEvent,
                  self.ToLeftArea.mouseMoveEvent == self.NoneEvent,
                  self.ToLeftArea.mousePressEvent == self.NoneEvent,
                  self.ToLeftArea.mouseReleaseEvent == self.NoneEvent,
                  self.ToRightArea.mouseMoveEvent == self.NoneEvent,
                  self.ToRightArea.mousePressEvent == self.NoneEvent,
                  self.ToRightArea.mouseReleaseEvent == self.NoneEvent,
                  self.UpLeftArea.mouseMoveEvent == self.NoneEvent,
                  self.UpLeftArea.mousePressEvent == self.NoneEvent,
                  self.UpLeftArea.mouseReleaseEvent == self.NoneEvent,
                  self.UpRightArea.mouseMoveEvent == self.NoneEvent,
                  self.UpRightArea.mousePressEvent == self.NoneEvent,
                  self.UpRightArea.mouseReleaseEvent == self.NoneEvent,
                  self.DownRightArea.mouseMoveEvent == self.NoneEvent,
                  self.DownRightArea.mousePressEvent == self.NoneEvent,
                  self.DownRightArea.mouseReleaseEvent == self.NoneEvent,
                  self.DownLeftArea.mouseMoveEvent == self.NoneEvent,
                  self.DownLeftArea.mousePressEvent == self.NoneEvent,
                  self.DownLeftArea.mouseReleaseEvent == self.NoneEvent):
            if not i:
                result = False
                break
        return result

    def setNormalEvent(self):
        self.ToUpArea.mouseMoveEvent = self.toUpMoveEvent
        self.ToUpArea.mousePressEvent = self.toUpPressEvent
        self.ToUpArea.mouseReleaseEvent = self.toUpReleaseEvent
        self.ToDownArea.mouseMoveEvent = self.toDownMoveEvent
        self.ToDownArea.mousePressEvent = self.toDownPressEvent
        self.ToDownArea.mouseReleaseEvent = self.toDownReleaseEvent
        self.ToLeftArea.mouseMoveEvent = self.toLeftMoveEvent
        self.ToLeftArea.mousePressEvent = self.toLeftPressEvent
        self.ToLeftArea.mouseReleaseEvent = self.toLeftReleaseEvent
        self.ToRightArea.mouseMoveEvent = self.toRightMoveEvent
        self.ToRightArea.mousePressEvent = self.toRightPressEvent
        self.ToRightArea.mouseReleaseEvent = self.toRightReleaseEvent
        self.MoveableArea.mousePressEvent = self.movePressEvent
        self.MoveableArea.mouseMoveEvent = self.moveMoveEvent
        self.MoveableArea.mouseReleaseEvent = self.moveReleaseEvent
        self.MoveableArea.mouseDoubleClickEvent = self.titleDoubleClickedEvent
        self.UpLeftArea.mouseMoveEvent = self.UpLeftMoveEvent
        self.UpLeftArea.mousePressEvent = self.UpLeftPressEvent
        self.UpLeftArea.mouseReleaseEvent = self.UpLeftReleaseEvent
        self.UpRightArea.mouseMoveEvent = self.UpRightMoveEvent
        self.UpRightArea.mousePressEvent = self.UpRightPressEvent
        self.UpRightArea.mouseReleaseEvent = self.UpRightReleaseEvent
        self.DownRightArea.mouseMoveEvent = self.DownRightMoveEvent
        self.DownRightArea.mousePressEvent = self.DownRightPressEvent
        self.DownRightArea.mouseReleaseEvent = self.DownRightReleaseEvent
        self.DownLeftArea.mouseMoveEvent = self.DownLeftMoveEvent
        self.DownLeftArea.mousePressEvent = self.DownLeftPressEvent
        self.DownLeftArea.mouseReleaseEvent = self.DownLeftReleaseEvent
        self.is_corner = False

    def setWindowTitleBar(self,
                          background_color_rgba: tuple[int] | list[int] | set[int] = (25, 25, 25, 0.5),
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
        self.WindowTitleBackground.setGeometry(0, 0, QGuiApplication.primaryScreen().size().width(), title_height)
        self.WindowTitleBar = QPushButton(self.title, self)
        self.WindowTitleBar.setGeometry(0, 0, self.size().width(), title_height)
        self.WindowTitleBar.setStyleSheet("QPushButton {"
                                          'font: normal normal 15px "微软雅黑";'
                                          f"background-color: rgba(0,0,0,0);"
                                          f"color: rgba({color_rgba[0]}, {color_rgba[1]}, {color_rgba[2]}, {color_rgba[3]});"
                                          "border: none;"
                                          "}")
        self.setMoveableArea()

    def showMaximized(self):
        self.setGeometry(0, 0, QGuiApplication.primaryScreen().size().width(),
                         QGuiApplication.primaryScreen().size().height() - 50)
        self.setNoneEvent()

    def showLined(self):
        self.setGeometry(self.pos().x(), 0, self.size().width(), QGuiApplication.primaryScreen().size().height() - 50)
        self.setNoneEvent()

    def showNormal(self):
        self.setGeometry(self.normal_geometry.x(), self.normal_geometry.y(), self.normal_geometry.width(),
                         self.normal_geometry.height())
        self.setNormalEvent()
        if self.pos().y() <= 5 and self.isLined() is not True:
            self.move(self.normal_geometry.x(), 5)

    def showSizeNormal(self):
        self.resize(self.normal_geometry.width(), self.normal_geometry.height())
        self.setNormalEvent()

    def showUpLeft(self):
        self.setGeometry(0, 0, self.__screen__.width() // 2,
                         (self.__screen__.height() - 50) // 2)
        self.setNoneEvent()
        self.is_corner = True

    def showFullLeft(self):
        self.setGeometry(0, 0, self.__screen__.width() // 2,
                         self.__screen__.height() - 50)
        self.setNoneEvent()

    def showDownLeft(self):
        self.setGeometry(0, (self.__screen__.height() - 50) // 2,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - 50) // 2)
        self.setNoneEvent()
        self.is_corner = True

    def showUpRight(self):
        self.setGeometry(self.__screen__.width() // 2, 0,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - 50) // 2)
        self.setNoneEvent()
        self.is_corner = True

    def showDownRight(self):
        self.setGeometry(self.__screen__.width() // 2,
                         (self.__screen__.height() - 50) // 2,
                         self.__screen__.width() // 2,
                         (self.__screen__.height() - 50) // 2)
        self.setNoneEvent()
        self.is_corner = True

    def showFullRight(self):
        self.setGeometry(self.__screen__.width() // 2, 0,
                         self.__screen__.width() // 2,
                         self.__screen__.height() - 50)
        self.setNoneEvent()

    def isMaximized(self) -> bool:
        if [self.size().width(), self.size().height()] == [self.__screen__.width(),
                                                           self.__screen__.height() - 50]:
            return True
        else:
            return False

    def isLined(self) -> bool:
        if self.size().height() == self.__screen__.height() - 50 and self.pos().y() == 0:
            return True
        else:
            return False

    def isFullSide(self) -> bool:
        if self.size().width() == self.__screen__.width() // 2 and \
                self.size().height() == self.__screen__.height() - 50 and \
                self.pos().y() == 0:
            if self.pos().x() == self.__screen__.width() // 2 or \
                    self.pos().x() == 0:
                return True
            else:
                return False
        else:
            return False

    def isFullCorner(self) -> bool:
        result = False
        if self.is_corner == True:
            if self.isNoneEvent():
                result = True
        return result

    def resizeEvent(self, event):
        self.WindowTitleBar.setGeometry(0, 0, self.size().width(), 35)
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

    def titleDoubleClickedEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.isMaximized() or self.isLined() or self.isFullCorner() or self.isFullSide():
                self.showNormal()
            else:
                self.showMaximized()

    def setMoveableArea(self):
        self.MoveableArea = QPushButton(self)
        self.MoveableArea.setStyleSheet("QPushButton {"
                                        "background-color: rgba(255,255,255,0);"
                                        "border: none;"
                                        "}")
        self.MoveableArea.setGeometry(0, 0, self.size().width(), self.title_height)
        self.MoveableArea.mousePressEvent = self.movePressEvent
        self.MoveableArea.mouseMoveEvent = self.moveMoveEvent
        self.MoveableArea.mouseReleaseEvent = self.moveReleaseEvent
        self.MoveableArea.mouseDoubleClickEvent = self.titleDoubleClickedEvent
        self.setToUpArea()

    def setToUpArea(self):
        self.ToUpArea = QPushButton(self.MoveableArea)
        self.ToUpArea.setStyleSheet("QPushButton {"
                                    "background-color: rgba(255,255,255,0);"
                                    "border: none;"
                                    "}")
        self.ToUpArea.setGeometry(0, 0, self.size().width(), self.edge)
        self.ToUpArea.setCursor(Qt.CursorShape.SizeVerCursor)
        self.ToUpArea.mouseMoveEvent = self.toUpMoveEvent
        self.ToUpArea.mousePressEvent = self.toUpPressEvent
        self.ToUpArea.mouseReleaseEvent = self.toUpReleaseEvent
        self.setToDownArea()

    def setToDownArea(self):
        self.ToDownArea = QPushButton(self)
        self.ToDownArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.ToDownArea.setGeometry(0, self.size().height() - self.edge, self.size().width(), self.edge)
        self.ToDownArea.setCursor(Qt.CursorShape.SizeVerCursor)
        self.ToDownArea.mouseMoveEvent = self.toDownMoveEvent
        self.ToDownArea.mousePressEvent = self.toDownPressEvent
        self.ToDownArea.mouseReleaseEvent = self.toDownReleaseEvent
        self.setToLeftArea()

    def setToLeftArea(self):
        self.ToLeftArea = QPushButton(self)
        self.ToLeftArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.ToLeftArea.setGeometry(0, 0, self.edge, self.size().height())
        self.ToLeftArea.setCursor(Qt.CursorShape.SizeHorCursor)
        self.ToLeftArea.mouseMoveEvent = self.toLeftMoveEvent
        self.ToLeftArea.mousePressEvent = self.toLeftPressEvent
        self.ToLeftArea.mouseReleaseEvent = self.toLeftReleaseEvent
        self.setToRightArea()

    def setToRightArea(self):
        self.ToRightArea = QPushButton(self)
        self.ToRightArea.setStyleSheet("QPushButton {"
                                       "background-color: rgba(255,255,255,0);"
                                       "border: none;"
                                       "}")
        self.ToRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.size().height())
        self.ToRightArea.setCursor(Qt.CursorShape.SizeHorCursor)
        self.ToRightArea.mouseMoveEvent = self.toRightMoveEvent
        self.ToRightArea.mousePressEvent = self.toRightPressEvent
        self.ToRightArea.mouseReleaseEvent = self.toRightReleaseEvent
        self.setUpLeftArea()

    def toRightPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.right_click_position = event.globalPosition().toPoint() - self.pos()
            self.beginning_pos_x = QCursor.pos().x()
            self.toRightPress = True
            self._width_ = self.size().width()

    def toRightMoveEvent(self, event: QMouseEvent):
        if self.toRightPress and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_x), self.size().height())
        event.accept()

    def toRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toRightPress = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def movePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and \
                event.position().y() <= self.title_height:
            self.is_mouse_pressed = True
            self.mouse_click_position = event.globalPosition().toPoint() - self.pos()
            if self.isMaximized():
                self.movemode = 1
            elif self.isFullSide():
                self.movemode = 3
            elif self.isFullCorner():
                self.movemode = 4
            elif self.isLined():
                self.movemode = 2
            else:
                self.movemode = 0
        event.accept()

    def moveMoveEvent(self, event: QMouseEvent):
        if self.is_mouse_pressed:
            if self.movemode == 0:
                self.move(event.globalPosition().toPoint() - self.mouse_click_position)
            elif self.movemode == 3:
                self.showSizeNormal()
                self.move(
                    event.globalPosition().toPoint().x() - self.mouse_click_position.x() * self.normal_geometry.width() // (
                            QGuiApplication.primaryScreen().size().width() // 2),
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
                            QGuiApplication.primaryScreen().size().width() // 2),
                    (event.globalPosition().toPoint() - self.mouse_click_position).y())
            elif self.movemode == 2:
                self.showSizeNormal()
                self.move(event.globalPosition().toPoint() - self.mouse_click_position)
        event.accept()

    def moveReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_mouse_pressed = False
            if QCursor.pos().y() <= 0 and self.__screen__.width() - 5 > QCursor.pos().x() > 5:
                self.showMaximized()
            elif QCursor.pos().x() <= 5 and QCursor.pos().y() <= 5:
                self.showUpLeft()
            elif QCursor.pos().x() >= self.__screen__.width() - 5 and QCursor.pos().y() <= 5:
                self.showUpRight()
            elif QCursor.pos().x() <= 5 and QCursor.pos().y() >= self.__screen__.height() - 50:
                self.showDownLeft()
            elif QCursor.pos().y() >= self.__screen__.height() - 50 and \
                    QCursor.pos().x() >= self.__screen__.width() - 5:
                self.showDownRight()
            elif QCursor.pos().x() <= 5 <= QCursor.pos().y() <= self.__screen__.height() - 5:
                self.showFullLeft()
            elif QCursor.pos().x() >= self.__screen__.width() - 5 and \
                    self.__screen__.height() - 5 >= QCursor.pos().y() >= 5:
                self.showFullRight()
            elif not (self.isMaximized() or self.isLined() or self.isFullSide() or self.isFullCorner()):
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def toUpPressEvent(self, event: QMouseEvent):
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

    def toUpMoveEvent(self, event: QMouseEvent):
        if self.up_resized and self.size().height() + self.pos().y() - QCursor.pos().y() >= self.minimumHeight():
            self.resize(self._width_, self._height_ - QCursor.pos().y() + self.beginning_pos_y)
            self.move(self._x_, (event.globalPosition().toPoint() - self.up_click_position).y())
        event.accept()

    def toUpReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.up_resized = False
            if QCursor.pos().y() <= 0 and QGuiApplication.primaryScreen().geometry().width() - 5 > QCursor.pos().x() > 5:
                self.showLined()
            else:
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def toDownPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.down_click_position = event.globalPosition().toPoint() - self.pos()
            self.beginning_pos_y = QCursor.pos().y()
            self._height_ = self.size().height()
            self.toDownPress = True

    def toDownMoveEvent(self, event: QMouseEvent):
        if self.toDownPress and QCursor.pos().y() >= self.minimumHeight() + self.pos().y():
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_y))
        event.accept()

    def toDownReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toDownPress = False
            if QCursor.pos().y() >= self.__screen__.height() - 50 and \
                    5 <= QCursor.pos().x() <= self.__screen__.width() - self.edge:
                self.showLined()
            else:
                self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def toLeftPressEvent(self, event: QMouseEvent):
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

    def toLeftMoveEvent(self, event: QMouseEvent):
        if self.left_resized and self.pos().x() + self.size().width() - QCursor.pos().x() >= self.minimumWidth():
            self.resize(self._width_ - QCursor.pos().x() + self.beginning_pos_x, self.height())
            self.move((event.globalPosition().toPoint() - self.left_click_position).x(), self._y_)
        event.accept()

    def toLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.left_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def setUpLeftArea(self):
        self.UpLeftArea = QPushButton(self)
        self.UpLeftArea.setStyleSheet("QPushButton {"
                                      "background-color: rgba(255,255,255,0);"
                                      "border: none;"
                                      "}")
        self.UpLeftArea.setGeometry(0, 0, self.edge, self.edge)
        self.UpLeftArea.setCursor(Qt.CursorShape.SizeFDiagCursor)
        self.UpLeftArea.mouseMoveEvent = self.UpLeftMoveEvent
        self.UpLeftArea.mousePressEvent = self.UpLeftPressEvent
        self.UpLeftArea.mouseReleaseEvent = self.UpLeftReleaseEvent
        self.setUpRightArea()

    def UpLeftPressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upleft_resized = True
            self.upleft_click_position = event.globalPosition().toPoint() - self.pos()
            self._x_ = self.pos().x()
            self._y_ = self.pos().y()
            self._width_ = self.size().width()
            self._height_ = self.size().height()
            self.beginning_pos = QCursor().pos()
        event.accept()

    def UpLeftMoveEvent(self, event: QMouseEvent):
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

    def UpLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upleft_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def setUpRightArea(self):
        self.UpRightArea = QPushButton(self)
        self.UpRightArea.setStyleSheet("QPushButton {"
                                       "background-color: rgba(255,255,255,0);"
                                       "border: none;"
                                       "}")
        self.UpRightArea.setGeometry(self.size().width() - self.edge, 0, self.edge, self.edge)
        self.UpRightArea.setCursor(Qt.CursorShape.SizeBDiagCursor)
        self.UpRightArea.mouseMoveEvent = self.UpRightMoveEvent
        self.UpRightArea.mousePressEvent = self.UpRightPressEvent
        self.UpRightArea.mouseReleaseEvent = self.UpRightReleaseEvent
        self.setDownRightArea()

    def UpRightPressEvent(self, event: QMouseEvent):
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

    def UpRightMoveEvent(self, event: QMouseEvent):
        if self.upright_resized and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_right.x()), self.size().height())
        if self.upright_resized and self.pos().y() + self.size().height() - QCursor.pos().y() >= self.minimumHeight():
            self.resize(self.width(), self._height_ - QCursor.pos().y() + self.beginning_pos_up.y())
            self.move(self._x_, (event.globalPosition().toPoint() - self.upleft_click_position).y())
        event.accept()

    def UpRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.upright_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def setDownRightArea(self):
        self.DownRightArea = QPushButton(self)
        self.DownRightArea.setStyleSheet("QPushButton {"
                                         "background-color: rgba(255,255,255,0);"
                                         "border: none;"
                                         "}")
        self.DownRightArea.setGeometry(self.size().width() - self.edge, self.size().height() - self.edge, self.edge,
                                       self.edge)
        self.DownRightArea.setCursor(Qt.CursorShape.SizeFDiagCursor)
        self.DownRightArea.mouseMoveEvent = self.DownRightMoveEvent
        self.DownRightArea.mousePressEvent = self.DownRightPressEvent
        self.DownRightArea.mouseReleaseEvent = self.DownRightReleaseEvent
        self.setDownLeftArea()

    def DownRightPressEvent(self, event: QMouseEvent):
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

    def DownRightMoveEvent(self, event: QMouseEvent):
        if self.downright_resized and (
                event.globalPosition().toPoint() - self.pos()).y() >= self.minimumHeight() - self.edge:
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_down.y()))
        if self.downright_resized and QCursor.pos().x() >= self.pos().x() + self.minimumWidth() - self.edge:
            self.resize(self._width_ + (QCursor.pos().x() - self.beginning_pos_right.x()), self.size().height())
        event.accept()

    def DownRightReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downright_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()

    def setDownLeftArea(self):
        self.DownLeftArea = QPushButton(self)
        self.DownLeftArea.setStyleSheet("QPushButton {"
                                        "background-color: rgba(255,255,255,0);"
                                        "border: none;"
                                        "}")
        self.DownLeftArea.setGeometry(0, self.size().height() - self.edge, self.edge,
                                      self.edge)
        self.DownLeftArea.setCursor(Qt.CursorShape.SizeBDiagCursor)
        self.DownLeftArea.mouseMoveEvent = self.DownLeftMoveEvent
        self.DownLeftArea.mousePressEvent = self.DownLeftPressEvent
        self.DownLeftArea.mouseReleaseEvent = self.DownLeftReleaseEvent

    def DownLeftPressEvent(self, event: QMouseEvent):
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

    def DownLeftMoveEvent(self, event: QMouseEvent):
        if self.downleft_resized and (
                event.globalPosition().toPoint() - self.pos()).y() >= self.minimumHeight() - self.edge:
            self.resize(self.size().width(), self._height_ + (QCursor.pos().y() - self.beginning_pos_down.y()))
        if self.downleft_resized and self.pos().x() + self.size().width() - QCursor.pos().x() >= self.minimumWidth():
            self.resize(self._width_ - QCursor.pos().x() + self.beginning_pos_left.x(), self.size().height())
            self.move((event.globalPosition().toPoint() - self.upleft_click_position).x(), self._y_)
        event.accept()

    def DownLeftReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.downleft_resized = False
            self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        event.accept()
