
from PySide6.QtCore import Qt, QPoint, QPropertyAnimation
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QWidget


class SwitchButton(QWidget):
    def __init__(self, on: bool = False):
        super().__init__()
        # self.resize(300,80)

        self.isoff = True

        self.offBgBrush = Qt.GlobalColor.gray
        self.onBgBrush = Qt.GlobalColor.blue

        # 定义滑块颜色
        self.offIndicatorBrush = Qt.GlobalColor.black
        self.onIndicatorBrush = Qt.GlobalColor.white

        self.offText = ''
        self.onText = ''

        self.animation = QPropertyAnimation()
        self.animation.setTargetObject(self)
        self.animation.setDuration(300)
        self.currentX = int(self.height() / 2)

        # slots
        self.animation.valueChanged.connect(self.fun)
        if on:
            self.isoff = False
            self.update()

    def fun(self, val):
        self.currentX = str(val)

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self.offBgBrush if self.isoff else self.onBgBrush)
        painter.drawRoundedRect(self.rect(), self.height() / 2, self.height() / 2)

        # 绘制滑块颜色
        painter.setBrush(self.offIndicatorBrush if self.isoff else self.onIndicatorBrush)
        # 定义滑块圆心位置
        if self.isoff:
            center = QPoint(self.height() // 2, self.height() // 2)
        else:
            center = QPoint(self.width() - self.height() // 2, self.height() // 2)
        painter.drawEllipse(center, self.height() / 2 - 10, self.height() / 2 - 10)

        painter.setPen(Qt.GlobalColor.white)
        painter.setFont(QFont("微软雅黑", 10))
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.offText if self.isoff else self.onText)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.isoff = not self.isoff
            self.update()

    def resizeEvent(self, event):
        self.animation.setStartValue(self.height() / 2)
        self.animation.setEndValue(self.width() - self.height() / 2)

    def setoff(self):
        self.isoff = True
        self.update()

    def seton(self):
        self.isoff = False
        self.update()

    def of_on(self):
        return self.isoff
