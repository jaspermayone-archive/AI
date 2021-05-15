from PyQt5 import QtWidgets,QtGui,QtCore
import os
import sys

class GUI(QtWidgets.QMainWindow): 

    def __init__(self):
        super(GUI, self).__init__()
        self.setFixedSize(205, 205)
        self.setWindowTitle("JARVIS")
        self.setWindowIcon(QtGui.QIcon(os.path.join('images', 'logo.png')))
        self.setStyleSheet("background : white;text-align: center;")


        self.nav = QtWidgets.QToolBar("Navigation")
        self.nav.setOrientation(QtCore.Qt.Vertical)
        self.nav.setIconSize(QtCore.QSize(200, 200))
        self.nav.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.nav.setMovable(False)
        self.addToolBar(self.nav)

        self.mic = QtWidgets.QAction(QtGui.QIcon(os.path.join('images', 'mic.jpg')), "Add new tab", self)

        self.nav.addAction(self.mic)
        
        self.nav.setStyleSheet("""
                                QToolBar {
                                    background-color: #ffffff; 
                                    color:#000000;
                                }
                                QToolBar QToolButton {
                                    background-color: #ffffff;
                                    border-radius: 200px;
                                }
                                
                                """)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("JARVIS")
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
