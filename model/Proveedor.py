from model.Herencias import DatosCLASS, Rubro_CLASS
from dao import ContactoDao, RubroDao, ProveedorDao


class ProveedorCLASS(DatosCLASS, Rubro_CLASS):

    def __init__(self, razon_social, TipoRubro, ruc, direccion, telefono, email):
        super().__init__(telefono, email)
        Rubro_CLASS.__init__(self, TipoRubro)        
        self.__razon_social = razon_social
        self.__RUC = ruc
        self.__direccion = direccion
        
    
    #CAMBIAR DATOS
    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social
        
    def set_RUC(self, ruc):
        self.__RUC = ruc
        
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
        
    #OBTENER DATOS        
    def get_razon_social(self):
        return self.__razon_social
    
    def get_RUC(self):
        return self.__RUC
    
    def get_direccion(self):
        return self.__direccion
    
    
    #REGISTRO DE NUEVO PROVEEDOR
    def Nuevo_Proveedor(self):

        Razon_Social = self.get_razon_social()
        Numero_RUC = self.get_RUC()
        Direccion = self.get_direccion()
        Telefono = self.get_telefono()
        Email = self.get_email()
        Tipo_Rubro =  self.get_TipoRubro()
        
        
        DaoContacto = ContactoDao.ContactoBD()
        DaoRubro = RubroDao.RubroBD()
        DaoProveedor = ProveedorDao.ProveedorBD()
        
        #Obtencion de ID Rubro
        idRubro = DaoRubro.ObtenerRubroID(Tipo_Rubro)
        
        #Insert en Tabla Contacto y Obtencion de ID
        DaoContacto.InsertTablaContacto(Telefono, Email)
        idContacto = DaoContacto.ObtenerContactoID(Telefono, Email)
        
        #Insert en Tabla Proveedor y Finalizacion del Registro
        DaoProveedor.InsertTablaProveedor(Razon_Social, Numero_RUC, Direccion, idContacto, idRubro)
