from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import concurrent.futures
import threading
import os
from easySpeech import speech
from backend.core import core
from backend.speak import speak


class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    @QtCore.pyqtSlot()
    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                future = executor.submit(speech.speech,"google")
                return_value = future.result()
            except:
                return_value=""
            print(return_value)
            with concurrent.futures.ThreadPoolExecutor() as main:
                try:
                    main_core = main.submit(core,return_value)
                    value = main_core.result()
                    speak(value)
                except:
                    pass


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        # defining shotcuts
        self.shortcut_open = QtWidgets.QShortcut(QtGui.QKeySequence('f5'), self)
        self.shortcut_open.activated.connect(self.download)
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedSize(330, 620)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: black;color:white')
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view .setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.view.load(QtCore.QUrl("https://j-dogcoder.github.io/J.A.R.V.I.S/templates/"))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)
        self.setWindowIcon(QtGui.QIcon(os.path.join('images', 'source.png')))

    def download(self):
        try:
            function=MainThread()
            th = threading.Thread(target=function.run)
            th.daemon = True
            th.start()
        except:
            pass 

#yes you are right i am using download requested to call python function
    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self):
        try:
            function=MainThread()
            th = threading.Thread(target=function.run)
            th.daemon = True
            th.start()
        except:
            pass      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
