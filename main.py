import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        # self.browser.setUrl(QUrl('http://google.com'))
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction('<-', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(':)', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home = QAction('|^|', self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        github = QAction('</>', self)
        github.triggered.connect(self.github)
        navbar.addAction(github)

        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.connect_url)

        self.browser.urlChanged.connect(self.update_url)

    def connect_url(self):
        url = self.url_bar.text()
        if 'http://' in url or 'https://' in url:
            url = url
        else:
            url = f"https://{url}"
        self.browser.setUrl(QUrl(url))

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def github(self):
        self.browser.setUrl(QUrl("http://github.com"))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Dark Browser")
window = Window()
app.exec_()