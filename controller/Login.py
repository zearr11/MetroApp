from PyQt5 import uic
from view_img import Recursos
from dao import UsuarioDao
from controller import MenuPrincipal

class Login:
    
    def __init__(self):
        self.log = uic.loadUi("view/FRM_LOGIN.ui")
        self.log.setWindowTitle("Acceso Login")
        self.log.login.clicked.connect(self.acceso_login)
        self.log.show()
        
    def acceso_login(self):
        user = self.log.username.text()
        passw = self.log.password.text()

        if len(user)== 0 or len(passw) == 0:
            self.log.warning.setText("¡Los campos no deben estar vacios!")
                
        else:
            if len(user)> 8 or len(passw)<8:
                self.log.warning.setText("¡Datos inválidos!")
                
            else:
                PruebaLog = UsuarioDao.UsuarioBD()
                if PruebaLog.ConsultaLogin(user, passw) == True:
                    self.log.close()
                    self.InicioMenu = MenuPrincipal.Menu()
                else:
                    self.log.warning.setText("¡Datos inválidos!")