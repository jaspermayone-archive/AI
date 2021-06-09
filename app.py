from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import concurrent.futures
import threading
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
                main_core = main.submit(core,return_value)
                value = main_core.result()
                speak(value)


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedSize(330, 620)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: black;color:white')
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view .setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)
        url = "file:///templates/index.html"
        self.view.load(QtCore.QUrl(url))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)
#yes you are right i am using download requested to call python function
    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self):
        function=MainThread()
        th = threading.Thread(target=function.run)
        th.daemon = True
        th.start()
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())