from model.HerenciasModel import CategoriaCLASS, EstadoCLASS, MedidaVentaCLASS


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
    
