from PyQt5 import QtWidgets, QtGui, QtCore
from controller import Login
import time


class AppInicial:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        ImgPix2 = QtGui.QPixmap("view_img/METROSPLASH.png")
        
        self.splash = QtWidgets.QSplashScreen(ImgPix2, QtCore.Qt.WindowStaysOnTopHint)
        self.splash.setMask(ImgPix2.mask())
        self.splash.show()
        
        for i in range(1, 11):
            time.sleep(0.3)
        
        self.splash.finish(self.splash)
        
        self.log = Login.LoginFRM()
        self.app.exec()
        
