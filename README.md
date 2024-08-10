# DesktopUI自述文件
### 这是一个基于 Pyside6 的开源虚拟用户操作界面，此项目的最后更新日期为：2024年8月9日
### —————————————————————————————————————————
### 更新公告：
#### 2024年8月9日，增加基于 QPushbutton 的虚拟窗口及定义了最大化，双击标题栏，向下还原事件。

``` python
    # 最大化事件
    def showMaximized(self):
        self.setGeometry(0, 0, self.parent_name.size().width(), self.parent_name.size().height() - 50)
        self.setNoneEvent()

    # 双击标题栏事件
    def titleDoubleClickedEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.isMaximized() or self.isLined():
                self.showNormal()
            else:
                self.showMaximized()
    def setMoveableArea(self):
        --snip--
        self.MoveableArea.mouseDoubleClickEvent = self.titleDoubleClickedEvent
        --snip--

```

* 向下还原事件的定义方法为：在窗口（ Normal 状态 ）移动或改变大小后获取窗口位置大小信息并更新窗口的 `normal_geometry`属性，在还原事件发生时将调用此属性。
``` python
    # 定义 normal_geometry 属性
    def __init__(self, appname: str = None, apphandle: int = None, parent: QWidget = None,
                 background_color_rgba: list[int] | tuple[int] | set[int] = (25, 25, 25, 0.9)):
        super(FrameLessWindow, self).__init__(parent)
        --snip--
        self.normal_geometry = QRect(self.pos().x(), self.pos().y(), self.size().width(), self.size().height())
        --snip--
    
    # 调用属性
    def showNormal(self):
        self.setGeometry(self.normal_geometry.x(), self.normal_geometry.y(), self.normal_geometry.width(),
                         self.normal_geometry.height())
```

#### 可实现的功能：
* 创建虚拟窗口
* 创建开始菜单和任务栏
* 实现基本电源操作
