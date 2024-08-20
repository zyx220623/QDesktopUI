#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年3月1日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: EmbedWindow
@description: 嵌入外部窗口
"""

import win32con
import win32gui

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, \
    QLabel, QApplication
from Starts.UIstart.windowui import FrameLessWindow


class Window(QWidget):

    def __init__(self, parent: QWidget = None):
        super(Window, self).__init__(parent=parent)
        self.resize(800, 600)
        self.__parent__ = parent

        self.myhwnd = int(self.winId())  # 自己的句柄
        self.btn1 = QPushButton('获取所有可用、可视窗口', self)
        self.btn1.setGeometry(5, 5, 200, 30)
        self.btn1.clicked.connect(self._getWindowList)

        self.btn2 = QPushButton('释放窗口', self)
        self.btn2.setGeometry(5, 50, 200, 30)
        self.btn2.clicked.connect(self.releaseWidget)
        self.windowList = QListWidget(self)
        self.windowList.itemDoubleClicked.connect(self.onItemDoubleClicked)
        self.windowList.setGeometry(0, 90, self.size().width(), 200)

    def releaseWidget(self):
        """释放窗口"""
        self.restore()
        self._getWindowList()

    def closeEvent(self, event):
        """窗口关闭"""
        self.releaseWidget()
        super(Window, self).closeEvent(event)

    def resizeEvent(self, event):
        self.windowList.setGeometry(0, 90, self.size().width(), 200)

    def _getWindowList(self):
        """清空原来的列表"""
        self.windowList.clear()
        win32gui.EnumWindows(self._enumWindows, None)

    def onItemDoubleClicked(self, item):
        def bodyResizeEvent(event):
            pass

        def parentResizeEvent():
            widget_window.setGeometry(winui.edge,
                                      winui.title_height + winui.edge,
                                      winui.size().width() - 2 * winui.edge,
                                      winui.size().height() - winui.title_height - 2 * winui.edge)
        def winUIPressEvent():
            widget_window.raise_()

        """列表双击选择事件"""
        # 先移除掉item
        try:
            self.windowList.takeItem(self.windowList.indexFromItem(item).row())
            hwnd, phwnd, _, _ = item.text().split('|')
        except:
            pass
        try:
            # 开始嵌入
            self.releaseWidget()
            hwnd, phwnd = int(hwnd), int(phwnd)
            # 嵌入之前的属性
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            wrect = win32gui.GetWindowRect(hwnd)[:2] + win32gui.GetClientRect(hwnd)[2:]
            print('save', hwnd, style, exstyle, wrect)
            winui = FrameLessWindow(appname=None, apphandle=None,
                                    parent=self.__parent__.__parent__, iconyes=False)
            winui.setWindowTitle(win32gui.GetWindowText(hwnd))
            widget_window = QWidget.createWindowContainer(QWindow.fromWinId(hwnd), parent=winui,
                                                          flags=Qt.WindowType.FramelessWindowHint)
            widget_window.hwnd = hwnd  # 窗口句柄
            widget_window.phwnd = phwnd  # 父窗口句柄
            widget_window.style = style  # 窗口样式
            widget_window.exstyle = exstyle  # 窗口额外样式
            widget_window.wrect = wrect  # 窗口位置
            try:
                win32gui.SetParent(hwnd, int(winui.winId()))
            except:
                pass
            widget_window.setGeometry(winui.edge,
                                      winui.title_height + winui.edge,
                                      winui.size().width() - 2 * winui.edge,
                                      winui.size().height() - winui.title_height - 2 * winui.edge)
            widget_window.resizeEvent = bodyResizeEvent
            winui.afterMousePressEventEvent = winUIPressEvent
            winui.customTitleResizeEvent = parentResizeEvent
            winui.normal_geometry = QRect(200, 100, 1200, 800)
            winui.show()
        except:
            pass
        try:
            self.windowList.takeItem(self.windowList.indexFromItem(item).row())
        except:
            pass
        self.close()
        self.show()

    def restore(self):
        """归还窗口"""
        self.close()
        self.show()
        pass

    def _enumWindows(self, hwnd, _):
        """遍历回调函数"""
        if hwnd == self.myhwnd:
            return  # 防止自己嵌入自己
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            phwnd = win32gui.GetParent(hwnd)
            title = win32gui.GetWindowText(hwnd)
            name = win32gui.GetClassName(hwnd)
            if ("Windows.UI.Core.CoreWindow" not in name and
                    "Progman" not in name and
                    "ApplicationFrameWindow" not in name and
                    "WorkerW" not in name and
                    "CabinetWClass" not in name and
                    "DummyDWMListenerWindow" not in name and
                    "EdgeUiInputTopWndClass" not in name and
                    "Shell_TrayWnd" not in name and
                    title != self.__parent__.__parent__.windowTitle()):
                self.windowList.addItem(
                    f'{hwnd}|{phwnd}|\t标题：{title}\t|\t类名：{name}')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
