from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import time

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedSize(330, 620)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
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
        print(time.time())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())