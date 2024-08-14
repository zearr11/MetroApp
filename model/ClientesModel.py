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
        
    def Update_Cliente(self, Newnombres, NewApellidos, NewTelefono, NewEmail, NewNumeroDoc, NewTipoDoc, NewDireccion, idCliente):
        
        NombresA = self.get_Nombres()
        ApellidosA = self.get_Apellidos()
        TelefonoA = self.get_Telefono()
        EmailA = self.get_Email()
        NumeroDocA = self.get_NumeroDoc()
        TipoDocA = self.get_TipoDoc()
        
        DaoTipoDocumento = TipoDocumentoDao.TipoDocumentoBD()
        DaoNumeroDocumento = NumeroDocumentoDao.NumeroDocumentoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoPersona = PersonaDao.PersonaBD()
        DaoCliente = ClienteDao.ClienteBD()
        
        #Obtencion ID Documento
        idTipoDocumentoA = DaoTipoDocumento.ObtenerTipoDocumentoID(TipoDocA)
        idTipoDocumentoN = DaoTipoDocumento.ObtenerTipoDocumentoID(NewTipoDoc)
        
        #Update en Tabla NumeroDocumento
        idNumeroDocumentoA = DaoNumeroDocumento.ObtenerNumeroDocumentoID(NumeroDocA, idTipoDocumentoA)
        DaoNumeroDocumento.UpdateNumeroDocumento(NewNumeroDoc, idTipoDocumentoN, idNumeroDocumentoA)
        
        #Update en Tabla Contacto
        idContactoA = DaoContacto.ObtenerContactoID(TelefonoA, EmailA)
        DaoContacto.UpdateContacto(NewTelefono, NewEmail, idContactoA)
        
        #Update en Tabla Persona
        idPersona = DaoPersona.ObtenerPersonaID(NombresA, ApellidosA, idContactoA, idNumeroDocumentoA, idTipoDocumentoA)
        DaoPersona.UpdatePersona(Newnombres, NewApellidos, idContactoA, idNumeroDocumentoA, idTipoDocumentoN, idPersona)
        
        #Update Cliente
        DaoCliente.UpdateCliente(NewDireccion, idPersona, idContactoA, idNumeroDocumentoA, idTipoDocumentoN, idCliente)
        
        
        
        """
        #Data Antigua
        idTipoDocA = DaoTipoDocumento.ObtenerTipoDocumentoID(TipoDocA)
        idNumeroDocA = DaoNumeroDocumento.ObtenerNumeroDocumentoID(NumeroDocA, idTipoDocA)
        idContactoA = DaoContacto.ObtenerContactoID(TelefonoA, EmailA)
        idPersonaA = DaoPersona.ObtenerPersonaID(NombresA, ApellidosA, idContactoA, idNumeroDocA,idTipoDocA)
        
        #Data Nuevo
        idTipoDocNew = DaoTipoDocumento.ObtenerTipoDocumentoID(NewTipoDoc)

        DaoCliente.UpdateCliente(NewDireccion, idPersonaA, idContactoA, idNumeroDocA, idTipoDocNew, idCliente)
        DaoPersona.UpdatePersona(Newnombres, NewApellidos, idContactoA, idNumeroDocA, idTipoDocNew, idPersonaA)
        DaoContacto.UpdateContacto(NewTelefono, NewEmail, idContactoA)
        DaoNumeroDocumento.UpdateNumeroDocumento(NewNumeroDoc, idTipoDocNew, idNumeroDocA)
        """
        
        