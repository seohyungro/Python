from PyQt5.QtWidgets import *
import sys , pickle
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'

from PyQt5 import uic, QtCore, QtGui

class UI(QMainWindow):
    def __init(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        self.show()

        self.Browse = self.findChild(QPushButton, "Browse")
        self.column_list = self.findChild(QListWidget, "column_list")

        self.Browse.clicked.connect(self.getCSV)

    def getCSV(self):
        QFileDialog.getOpenFileName(self, "Open File", )
        #self.column_list.clear()
        #self.column_list.addItems["브라우저", "브라우승", "브라질"]

if __name__ == '__main__': # if __name__ == 사용하면 이 제일 먼저 실행됨
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()
