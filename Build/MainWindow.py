import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets

class mainWindowUI(object):
    def setup(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.buttonTest = QtWidgets.QPushButton()
        self.buttonTest.setText("Convert Flac to Mp3")

        self.buttonTest2 = QtWidgets.QPushButton()
        self.buttonTest2.setText("Select Source File Dir")

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.buttonTest)
        self.mainLayout.addWidget(self.buttonTest2)