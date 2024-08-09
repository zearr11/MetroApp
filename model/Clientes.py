from model.Herencias import PersonaCLASS
from dao import DocumentoDao, ContactoDao, PersonaDao, ClienteDao

class ClienteCLASS(PersonaCLASS):
    
    def __init__(self, Nombres, Apellidos, TypeDoc, Num_doc, telefono, email, direccion):
        super().__init__(Nombres, Apellidos, TypeDoc, Num_doc, telefono, email)
        self.__direccion = direccion
        
        
    #CAMBIAR DATO DIRECCION
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
        
    #OBTENER DATO DIRECCION
    def get_direccion(self):
        return self.__direccion
    
    
    #REGISTRO DE NUEVO CLIENTE
    def Nuevo_Ciente(self):        
        Nombres = self.get_nombres()
        Apellidos = self.get_apellidos()
        Tipo_Doc = self.get_tipo_doc()
        Num_Doc = self.get_num_doc()
        Telefono = self.get_telefono()
        Email = self.get_email()
        Direccion = self.get_direccion()
        
        DaoDocumento = DocumentoDao.DocumentoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoPersona = PersonaDao.PersonaBD()
        DaoCliente = ClienteDao.ClienteBD()
        
        #Obtencion de ID Documento
        idDoc = DaoDocumento.ObtenerDocumentoID(Tipo_Doc)
        
        DaoContacto.InsertTablaContacto(Telefono, Email)
        idContacto = DaoContacto.ObtenerContactoID(Telefono, Email)
        
        DaoPersona.InsertTablaPersona(Nombres, Apellidos, Num_Doc, idDoc, idContacto)
        idPersona = DaoPersona.ObtenerPersonaID(Nombres, Apellidos, Num_Doc, idDoc, idContacto)

        DaoCliente.InsertTablaCliente(Direccion, idPersona, idDoc, idContacto)
        