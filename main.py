import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


app = QApplication(sys.argv)
QApplication.setApplicationName("Dark Browser")
window = Window()
app.exec_()