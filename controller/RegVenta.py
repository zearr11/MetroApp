from PyQt5 import uic
from controller import MenuPrincipal


class RegVentaFRM:
    
    def __init__(self):
        self.newVenta = uic.loadUi("view/FRM_REG_VENTA.ui")
        self.newVenta.setWindowTitle("Gestion de Ventas")
        
        self.newVenta.bt_cancelar_vent.clicked.connect(self.CancelarProduct)
        self.newVenta.show()
        
        
    def CancelarProduct(self):
        self.newVenta.close()
        self.menu = MenuPrincipal.MenuFRM()