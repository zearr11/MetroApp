from model.HerenciasModel import VentaCLASS
from model.ProductoModel import ProductoCLASS


class DetalleVenta(ProductoCLASS, VentaCLASS):
    def __init__(self, Descripcion, Marca, Cantidad, MedidaVenta, Precio, Estado, TipoCategoria):
        super().__init__(Descripcion, Marca, Cantidad, MedidaVenta, Precio, Estado, TipoCategoria)
