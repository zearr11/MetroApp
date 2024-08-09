from PyQt5 import uic
from controller import MenuPrincipal

class RegProveedor:
    
    def __init__(self):
        self.newProv = uic.loadUi("view/FRM_REG_PROVE.ui")
        self.newProv.setWindowTitle("Gestion de Proveedores")
        
        self.newProv.bt_cancelar_prov.clicked.connect(self.CancelarProv)
        self.newProv.show()
        
    def CancelarProv(self):
        self.newProv.close()
        self.menu = MenuPrincipal.Menu()