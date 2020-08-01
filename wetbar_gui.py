#!/usr/bin/python3
from PyQt5 import QtWidgets, uic, QtCore
import sys 
import os
from pigbmp183 import bmp183

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('wetbar.ui', self)

        self.bmp = bmp183()

    def measure(self):
        self.bmp.measure_pressure()
        t = 100
        if (self.bmp.ID != 85):
            print("Communication error!")
            print("Measurement may not be reliable. Chip ID is incorrect.")
        else:
            t = bmp.temperature
            
        self.lcdNumber.setValue(bmp.temperature)
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowCloseButtonHint);
    main.showFullScreen();
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main()
