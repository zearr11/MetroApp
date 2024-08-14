from model.ProductoModel import ProductoCLASS
from model.VentaModel import VentaCLASS

class DetalleVentaCLASS(ProductoCLASS, VentaCLASS):
    
    def __init__(self, idProducto, idVenta, CantidadProd, TotalProd):
        super().__init__(idProducto)
        VentaCLASS().__init__(self, idVenta)
        self.__CantidadProd = CantidadProd
        self.__TotalProd = TotalProd
        
    def get_CantProd(self):
        return self.__CantidadProd
    
    def get_TotalProd(self):
        return self.__TotalProd