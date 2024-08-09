from PyQt5 import uic
from controller import MenuPrincipal


class RegProductosFRM:
    
    def __init__(self):
        self.newProduct = uic.loadUi("view/FRM_REG_PROD_NUEVO.ui")
        self.newProduct.setWindowTitle("Gestion de Productos")
        
        self.newProduct.bt_cancelar_prod.clicked.connect(self.CancelarProduct)
        self.newProduct.show()
        
    def CancelarProduct(self):
        self.newProduct.close()
        self.menu = MenuPrincipal.MenuFRM()