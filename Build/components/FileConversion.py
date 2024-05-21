import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets



class FileConversionUI(object):
    def setup(self, FileConversion):
        #if not FileConversion.objectName():
        #    FileConversion.setObjectName(u"FiieConversion")

        self.buttonTest = QtWidgets.QPushButton()
        self.buttonTest.setText("Convert to Mp3")

        self.convertTypeDropDown = QtWidgets.QComboBox()
        self.convertTypeDropDown.addItem("mp3")
        self.convertTypeDropDown.addItem("flac")
        self.convertTypeDropDown.addItem("aac")
        self.convertTypeDropDown.addItem("wav")
        self.convertTypeDropDown.addItem("ogg")

        self.buttonTest2 = QtWidgets.QPushButton()
        self.buttonTest2.setText("Select Source File Dir")

        self.buttonTest3 = QtWidgets.QPushButton()
        self.buttonTest3.setText("Select Destination")

        self.labelTest = QtWidgets.QLabel()
        self.labelTest.setText("Source File Path:")

        self.labelTest2 = QtWidgets.QLabel()
        self.labelTest2.setText("Target File Path:")


        self.conversionLayoutContainer = QtWidgets.QWidget()
        self.conversionLayout = QtWidgets.QGridLayout(self.conversionLayoutContainer)
        self.conversionLayout.addWidget(self.buttonTest, 1, 1)
        self.conversionLayout.addWidget(self.buttonTest2, 1, 0)
        self.conversionLayout.addWidget(self.buttonTest3, 1, 2)

        self.conversionLayout.addWidget(self.labelTest, 0, 0)
        self.conversionLayout.addWidget(self.labelTest2, 0, 2)
        self.conversionLayout.addWidget(self.convertTypeDropDown, 2, 1)