import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets

import tkinter
from tkinter import filedialog

import MainWindow

import os 
import subprocess

homeDir = os.path.dirname(os.path.realpath(__file__)) + r'\ffmpeg' #gets the actual path (including python script name), then gets the directory, then appends the ffmpeg location
sourceFileDir = ""
targetFileDir = homeDir + r'\ConvertedFiles' #default should be here

class MainWidget(QtWidgets.QMainWindow): #Main Class
    def __init__(self):

        super(MainWidget, self).__init__()

        self.mainWindowUI = MainWindow.mainWindowUI()
        self.mainWindowUI.setup(self)

        self.resize(1800,800)
        self.setWindowTitle("Minimal FFmpeg GUI")
        
        widget = QtWidgets.QWidget(self)
        widget.setLayout(self.mainWindowUI.mainLayout)
        self.setCentralWidget(widget)

        self.mainWindowUI.buttonTest.clicked.connect(lambda x: self.convertFile(r'D:\Programming\FFmpeg-GUI\Build\ffmpeg\329.flac', r'D:\Programming\FFmpeg-GUI\Build\ffmpeg\329.mp3'))
        self.mainWindowUI.buttonTest2.clicked.connect(lambda x: self.selectSourceFile())

    @QtCore.Slot()    
    def convertFile(self, sourceFileDirectory, targetFileDirectory):
        os.chdir(homeDir)
        string = r'ffmpeg.exe -i ' + sourceFileDirectory + r' -ab 320k -map_metadata 0 -id3v2_version 3 ' + targetFileDirectory
        process = subprocess.Popen(string, cwd=homeDir)
        status = process.poll()

        if (status is None):
            print ("Conversion Finished")
    
    @QtCore.Slot()   
    def selectSourceFile(self):

        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        sourceFileDir = filedialog.askdirectory()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    MainWindow = MainWidget()

    MainWindow.show()

    sys.exit(app.exec())
