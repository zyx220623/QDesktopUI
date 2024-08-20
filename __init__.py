from os import environ
from Starts.UIstart.desktop import Desktop, QApplication
environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"
APPS = QApplication()
DESKTOP = Desktop()
DESKTOP.show()
APPS.exec()