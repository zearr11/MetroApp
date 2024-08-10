from model.HerenciasModel import ContactoCLASS, CategoriaCLASS
from dao import CategoriaDao, ContactoDao, ProveedorDao


class ProveedorCLASS(ContactoCLASS, CategoriaCLASS):

    def __init__(self, RazonSocial, Numero_RUC, Direccion, Telefono, Email, TipoCategoria):
        super().__init__(Telefono, Email)
        CategoriaCLASS.__init__(self, TipoCategoria)
        self.__RazonSocial = RazonSocial
        self.__Numero_RUC = Numero_RUC
        self.__Direccion = Direccion
    
    #CAMBIAR DATOS
    def set_RazonSocial(self, RazonSocial):
        self.__RazonSocial = RazonSocial
        
    def set_Numero_RUC(self, Numero_RUC):
        self.__Numero_RUC = Numero_RUC
        
    def set_Direccion(self, Direccion):
        self.__Direccion = Direccion
        
    #OBTENER DATOS        
    def get_RazonSocial(self):
        return self.__RazonSocial
    
    def get_Numero_RUC(self):
        return self.__Numero_RUC
    
    def get_Direccion(self):
        return self.__Direccion
    
    def Nuevo_Proveedor(self):
        RazonSocial = self.get_RazonSocial()
        NumeroRUC = self.get_Numero_RUC()
        Direccion = self.get_Direccion()
        Telefono = self.get_Telefono()
        Email = self.get_Email()
        TipoCategoria = self.get_TipoCategoria()
        
        DaoContacto = ContactoDao.ContactoBD()
        DaoCategoria = CategoriaDao.CategoriaBD()
        DaoProveedor = ProveedorDao.ProveedorBD()
        
        #Obtencion de ID Categoria
        idCategoria = DaoCategoria.ObtenerCategoriaID(TipoCategoria)
        
        #Insert en Tabla Contacto y Obtencion de ID
        DaoContacto.InsertTablaContacto(Telefono, Email)
        idContacto = DaoContacto.ObtenerContactoID(Telefono, Email)
        
        #Insert en Tabla Proveedor y Finalizacion del Registro
        DaoProveedor.InsertTablaProveedor(RazonSocial, NumeroRUC, Direccion, idContacto, idCategoria)
        
