from model.HerenciasModel import PersonaCLASS
from dao import TipoDocumentoDao, NumeroDocumentoDao, ContactoDao, PersonaDao, ClienteDao


class ClienteCLASS(PersonaCLASS):
    
    def __init__(self, Nombres, Apellidos, Telefono, Email, NumeroDoc, TipoDoc, Direccion):
        super().__init__(Nombres, Apellidos, Telefono, Email, NumeroDoc, TipoDoc)
        self.__Direccion = Direccion
        
    #CAMBIAR DATO DIRECCION
    def set_Direccion(self, Direccion):
        self.__Direccion = Direccion
        
    #OBTENER DATO DIRECCION
    def get_Direccion(self):
        return self.__Direccion

    def Nuevo_Cliente(self):
        Nombres = self.get_Nombres()
        Apellidos = self.get_Apellidos()
        Telefono = self.get_Telefono()
        Email = self.get_Email()
        NumeroDoc = self.get_NumeroDoc()
        TipoDoc = self.get_TipoDoc()
        Direccion = self.get_Direccion()
        
        DaoTipoDocumento = TipoDocumentoDao.TipoDocumentoBD()
        DaoNumeroDocumento = NumeroDocumentoDao.NumeroDocumentoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoPersona = PersonaDao.PersonaBD()
        DaoCliente = ClienteDao.ClienteBD()
        
        #Obtencion de ID Documento
        idTipoDocumento = DaoTipoDocumento.ObtenerTipoDocumentoID(TipoDoc)
        
        #Insert en Tabla NumeroDocumento y Obtencion de ID
        DaoNumeroDocumento.InsertTablaNumeroDocumento(NumeroDoc, idTipoDocumento)
        idNumeroDocumento = DaoNumeroDocumento.ObtenerNumeroDocumentoID(NumeroDoc, idTipoDocumento)
        
        #Insert en Tabla Contacto y Obtencion de ID
        DaoContacto.InsertTablaContacto(Telefono, Email)
        idContacto = DaoContacto.ObtenerContactoID(Telefono, Email)
        
        #Insert en Tabla Persona y Obtencion de ID
        DaoPersona.InsertTablaPersona(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)  
        idPersona = DaoPersona.ObtenerPersonaID(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)
        
        #Insert en Tabla Cliente y Finalizacion del Registro
        DaoCliente.InsertTablaCliente(Direccion, idPersona, idContacto, idNumeroDocumento, idTipoDocumento)
