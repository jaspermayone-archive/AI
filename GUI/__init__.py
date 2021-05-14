import sys
from time import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import pyttsx3

class jarvis(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("J.A.R.V.I.S")
        # self.setGeometry(100,100,800,600)
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        GUI_HTML = """
        <head>
        </head>
        <body style="background-color:black;">
        <br>
        <center>
        <img src = "https://cdn.dribbble.com/users/1373613/screenshots/6200333/__1.gif" width=700px>
        <center>
        </body>
        """

        pyttsx3.speak("How Can I help You Sir")

        self.JarvisGUI = QWebEngineView()
        self.JarvisGUI.setHtml(GUI_HTML)
        self.setCentralWidget(self.JarvisGUI)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = jarvis()
    sys.exit(app.exec_())

