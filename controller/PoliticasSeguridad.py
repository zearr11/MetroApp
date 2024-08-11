from PyQt5 import uic
from controller import MenuPrincipal, RegUsuarios


class PoliticasSeguridadFRM:

    def __init__(self):
        self.poli = uic.loadUi("view/FRM_POL_SEC.ui")
        self.poli.setWindowTitle("Politicas de Seguridad")
        
        self.poli.bt_cancelar.clicked.connect(self.CancelarPol)
        self.poli.bt_crearUser.clicked.connect(self.CreacionUser)
        self.poli.bt_editUser.clicked.connect(self.ModificacionUser)
        
        self.poli.show()
    
    def CancelarPol(self):
        self.poli.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def CreacionUser(self):
        self.poli.close()
        self.newUser = RegUsuarios.RegUsuariosFRM(True)
    
    def ModificacionUser(self):
        self.poli.close()
        self.newUser = RegUsuarios.RegUsuariosFRM(False)
        
