from model.HerenciasModel import CategoriaCLASS, EstadoCLASS, MedidaVentaCLASS
from dao import CategoriaDao, MedidaVentaDao, EstadoDao, ProductoDao


class ProductoCLASS(CategoriaCLASS, EstadoCLASS, MedidaVentaCLASS):
    
    def __init__(self, Descripcion, Marca, Cantidad, MedidaVenta, Precio, Estado, TipoCategoria):
        super().__init__(TipoCategoria)
        EstadoCLASS.__init__(self, Estado)
        MedidaVentaCLASS.__init__(self, MedidaVenta)
        self.__Descripcion = Descripcion
        self.__Marca = Marca
        self.__Cantidad = Cantidad
        self.__Precio = Precio
    
    #CAMBIAR DATOS:
    def set_Descripcion(self, Descripcion):
        self.__Descripcion = Descripcion
        
    def set_Marca(self, Marca):
        self.__Marca = Marca
        
    def set_Cantidad(self, Cantidad):
        self.__Cantidad = Cantidad
        
    def set_Precio(self, Precio):
        self.__Precio = Precio
        
    #OBTENER DATOS:
    def get_Descripcion(self):
        return self.__Descripcion
    
    def get_Marca(self):
        return self.__Marca
    
    def get_Cantidad(self):
        return self.__Cantidad
    
    def get_Precio(self):
        return self.__Precio
    
    def Nuevo_Producto(self):
        Descripcion = self.get_Descripcion()
        Marca = self.get_Marca()
        Cantidad = self.get_Cantidad()
        MedidaVenta = self.get_MedidaVenta()
        Precio = self.get_Precio()
        Estado = self.get_Estado()
        TipoCategoria = self.get_TipoCategoria()
        
        objCategoria = CategoriaDao.CategoriaBD()
        objMedida = MedidaVentaDao.MedidaVentaBD()
        objEstado = EstadoDao.EstadoBD()
        objProducto = ProductoDao.ProductoBD()
        
        #ObtenerID de Categoria
        idCat = objCategoria.ObtenerCategoriaID(TipoCategoria)
        
        #ObtenerID de Medida de Venta
        idMedVent = objMedida.ObtenerMedidaVentaID(MedidaVenta)
        
        #ObtenerID de Estado
        idEstd = objEstado.ObtenerEstadoID(Estado)
        
        #Insert de Nuevo Producto en Tabla Producto
        objProducto.InsertTablaProducto(Descripcion, Marca, Cantidad, Precio, idMedVent, idEstd, idCat)
        

