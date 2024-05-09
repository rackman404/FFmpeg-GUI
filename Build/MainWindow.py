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

        self.buttonTest3 = QtWidgets.QPushButton()
        self.buttonTest3.setText("Select Destination")

        self.labelTest = QtWidgets.QLabel()
        self.labelTest.setText("Source File Path:")

        self.labelTest2 = QtWidgets.QLabel()
        self.labelTest2.setText("Target File Path:")

        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.addWidget(self.buttonTest, 1, 1)
        self.mainLayout.addWidget(self.buttonTest2, 1, 0)
        self.mainLayout.addWidget(self.buttonTest3, 1, 3)

        self.mainLayout.addWidget(self.labelTest, 0, 0)
        self.mainLayout.addWidget(self.labelTest2, 0, 3)