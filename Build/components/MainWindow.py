import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets

from components import FileConversion

class mainWindowUI(object):
    def setup(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.FileConversion = FileConversion.FileConversionUI()
        self.FileConversion.setup(self)

        #header

        self.headerLayout = QtWidgets.QHBoxLayout()
        self.tabButton1 = QtWidgets.QPushButton("Audio Conversions")
        self.tabButton2 = QtWidgets.QPushButton("Video Conversions")
        self.tabButton3 = QtWidgets.QPushButton("Music Player")

        self.headerLayout.addWidget(self.tabButton1)
        self.headerLayout.addWidget(self.tabButton2)
        self.headerLayout.addWidget(self.tabButton3)


        self.stackedLayouts = QtWidgets.QStackedLayout()
        self.stackedLayouts.addWidget(self.FileConversion.conversionLayoutContainer)

        #default layout

        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.addLayout(self.headerLayout, 0, 0)
        self.mainLayout.addLayout(self.stackedLayouts, 1, 0)

        self.tabButton1.clicked.connect(lambda x: self.switchMainLayout(0))


    @QtCore.Slot() #Tab switching
    def switchMainLayout(self, tabNum):
        print (tabNum) #debug 
        self.stackedLayouts.setCurrentIndex(tabNum)

        """
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

        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.addWidget(self.buttonTest, 1, 1)
        self.mainLayout.addWidget(self.buttonTest2, 1, 0)
        self.mainLayout.addWidget(self.buttonTest3, 1, 2)

        self.mainLayout.addWidget(self.labelTest, 0, 0)
        self.mainLayout.addWidget(self.labelTest2, 0, 2)
        self.mainLayout.addWidget(self.convertTypeDropDown, 2, 1)
        """