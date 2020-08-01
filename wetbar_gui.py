#!/usr/bin/python3
from PyQt5 import QtWidgets, uic, QtCore
import sys 
import os
have_bmp183 = False

try:
    from pigbmp183 import bmp183
    have_bmp183 = True
except:
    pass

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('wetbar.ui', self)

        if have_bmp183:
            self.bmp = bmp183()


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.t = 25
        self.lcdNumber.display(self.t)
       

    def update(self):
        self.measure()
        self.lcdNumber.display(self.t)

    def measure(self):
        if have_bmp183:
            self.bmp.measure_pressure()
            if (self.bmp.ID != 85):
                print("Communication error!")
                print("Measurement may not be reliable. Chip ID is incorrect.")
            else:
                self.t = bmp.temperature

        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowCloseButtonHint);
    main.showFullScreen();
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main()
