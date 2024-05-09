import sys
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import PySide6.QtWidgets

import tkinter
from tkinter import filedialog

import MainWindow

import os 
import subprocess
import pathlib
from pathlib import Path

import time

import HelperClass

#constants
HOMEDIR = os.path.dirname(os.path.realpath(__file__)) #gets the actual path (including python script name), then gets the directory, then appends the ffmpeg location
FFMPEGDIR = os.path.dirname(os.path.realpath(__file__)) + r'\ffmpeg'

class MainWidget(QtWidgets.QMainWindow): #Main Class
    def __init__(self):
        super(MainWidget, self).__init__()
        self.threadpool = QtCore.QThreadPool()

        self.internalData =  HelperClass.internalData()

        self.sourceFileDirectory = ""
        self.targetFileDirectory = HOMEDIR + r'\ConvertedFiles' #default should be here
        self.targetFileFormat = '.mp3'

        '''
        sourceFileDirectory = ""
        targetFileDirectory = homeDir + r'\ConvertedFiles' #default should be here
        targetFileFormat = '.mp3'
        '''

        self.mainWindowUI = MainWindow.mainWindowUI()
        self.mainWindowUI.setup(self)

        #intial GUI setup
        self.mainWindowUI.labelTest2.setText('Target File Path: \n' + self.targetFileDirectory)

        self.setWindowTitle("Minimal FFmpeg GUI")
        
        widget = QtWidgets.QWidget(self)
        widget.setLayout(self.mainWindowUI.mainLayout)
        self.setCentralWidget(widget)

        #signal - interactions
        self.mainWindowUI.buttonTest.clicked.connect(lambda x: self.convertFile())
        self.mainWindowUI.buttonTest2.clicked.connect(lambda x: self.selectSourceFilePath())
        self.mainWindowUI.buttonTest3.clicked.connect(lambda x: self.selectDestinationPath())

    @QtCore.Slot()    
    def convertFile(self):

        sourceFileName = os.path.basename(self.sourceFileDirectory)
        targetFileName = Path(sourceFileName).stem + self.targetFileFormat

        #try: #if Source Directory is valid
        if (os.path.exists(self.sourceFileDirectory) == True): 
            string = f'ffmpeg.exe -i ' + self.sourceFileDirectory + f' -ab 320k -map_metadata 0 -id3v2_version 3 ' + self.targetFileDirectory + f'\\' + targetFileName

            process = subprocess.Popen(string, cwd=FFMPEGDIR, =,shell = True) # shell = true, security issue?

            #status = process.poll() 

        '''
        def execute(): #coroutine
            while (True):
                status = process.poll() 

                if (status is None):
                    print ("Conversion Finished")
                    break

                time.sleep(1)
        '''

        #thread = WorkerThread(execute)
        #self.threadpool.start(thread)

        #except:
        #    print ("ERROR, unknown error")     
    
    @QtCore.Slot()   
    def selectSourceFilePath(self):

        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        self.sourceFileDirectory = filedialog.askopenfilename()

        self.mainWindowUI.labelTest.setText("Source File Path: \n" + self.sourceFileDirectory)

    @QtCore.Slot()   
    def selectDestinationPath(self):

        tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
        self.targetFileDirectory = filedialog.askdirectory()

        self.mainWindowUI.labelTest2.setText("Target File Path: \n" + self.targetFileDirectory)

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
