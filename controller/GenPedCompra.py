from PyQt5 import uic
from controller import MenuPrincipal

class GenPedCompra:
    
    def __init__(self):
        self.newPedCompr = uic.loadUi("view/FRM_GEN_PED_COMPR.ui")
        self.newPedCompr.setWindowTitle("Generar Pedido de Compra")
        
        self.newPedCompr.bt_cancelar_pedcompr.clicked.connect(self.CancelarPedCompr)
        self.newPedCompr.show()
        
    def CancelarPedCompr(self):
        self.newPedCompr.close()
        self.menu = MenuPrincipal.Menu()