import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets

import tkinter
from tkinter import filedialog


import os 
import subprocess
import pathlib
from pathlib import Path

import ffmpeg #TO DO, PORT FFMPEG LIBRARY INSTEAD OF DIRECTLY RUNNING FFmpeg.exe as a CLI Tool

import time

import HelperClass
from components import MainWindow

#constants - windows
HOMEDIR = os.path.dirname(os.path.realpath(__file__)) #gets the actual path (including python script name), then gets the directory, then appends the ffmpeg location
FFMPEGDIR = os.path.dirname(os.path.realpath(__file__)) + r'\ffmpeg'

class MainWidget(QtWidgets.QMainWindow): #Main Class
    def __init__(self):
        super(MainWidget, self).__init__()
        self.threadpool = QtCore.QThreadPool()

        self.internalData =  HelperClass.internalData()

        self.sourceFileDirectory = ""
        self.targetFileDirectory = HOMEDIR + r"\ConvertedFiles" #default should be here
        self.targetFileFormat = '.mp3'

        self.mainWindowUI = MainWindow.mainWindowUI()
        self.mainWindowUI.setup(self)

        #intial GUI setup
        self.mainWindowUI.FileConversion.labelTest2.setText('Target File Path: \n' + self.targetFileDirectory)

        self.setWindowTitle("Minimal FFmpeg GUI")
        
        widget = QtWidgets.QWidget(self)
        widget.setLayout(self.mainWindowUI.mainLayout)
        self.setCentralWidget(widget)

        #signal - interactions
        self.mainWindowUI.FileConversion.buttonTest.clicked.connect(lambda x: self.convertFile())
        self.mainWindowUI.FileConversion.buttonTest2.clicked.connect(lambda x: self.selectSourceFilePath())
        self.mainWindowUI.FileConversion.buttonTest3.clicked.connect(lambda x: self.selectDestinationPath())

        self.mainWindowUI.FileConversion.convertTypeDropDown.currentIndexChanged.connect(lambda x: self.setTargetFileFormat())

        

    @QtCore.Slot()    
    def convertFile(self):

        sourceFileName = os.path.basename(self.sourceFileDirectory)
        targetFileName = Path(sourceFileName).stem + self.targetFileFormat

        #try: #if Source Directory is valid
        if (os.path.exists(self.sourceFileDirectory) == True): 
            #\" for path name exceptions (Ex. spaces), \\ to allow for appending file path name
            string = f'ffmpeg.exe -i ' + "\"" +  self.sourceFileDirectory + "\"" + f' -ab 320k -map_metadata 0 -id3v2_version 3 ' +  "\"" + self.targetFileDirectory + f'\\' + targetFileName + "\"" 
            print (string)

            process = subprocess.Popen(string, cwd=FFMPEGDIR, shell = True) # shell = true, security issue?

        
        def execute(process): #coroutine
            while (True):
                
                if (process.poll() is None):
                    print ("Conversion Finished") #NON FUNCTIONAL
                    break

                time.sleep(1)
        

        thread = WorkerThread(execute, process)
        self.threadpool.start(thread)
        

        #except:
        #    print ("ERROR, unknown error")     
    
    @QtCore.Slot()   
    def selectSourceFilePath(self):
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        self.sourceFileDirectory = filedialog.askopenfilename()

        self.mainWindowUI.FileConversion.labelTest.setText("Source File Path: \n" + self.sourceFileDirectory)

    @QtCore.Slot()   
    def selectDestinationPath(self):
        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        self.targetFileDirectory = filedialog.askdirectory()
        
        self.mainWindowUI.FileConversion.labelTest2.setText("Target File Path: \n" + self.targetFileDirectory)

    @QtCore.Slot()
    def setTargetFileFormat(self):
        self.targetFileFormat = "." + self.mainWindowUI.FileConversion.convertTypeDropDown.currentText()


#Multithreading
class WorkerThread(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(WorkerThread, self).__init__()
        
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
    
    @QtCore.Slot()  
    def run(self):
        self.fn(*self.args, **self.kwargs)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    MainWindow = MainWidget()

    MainWindow.show()

    sys.exit(app.exec())
