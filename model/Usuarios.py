from model.Herencias import PersonaCLASS
from dao import DocumentoDao, CargoDao, PermisoDao, ContactoDao, PersonaDao, UsuarioDao

class UsuariosCLASS(PersonaCLASS):
    def __init__(self, nomUser, contrasenia, Nombres, Apellidos, TypeDoc, Num_doc, telefono, email, cargoUser, permisoUser):
        super().__init__(Nombres, Apellidos, TypeDoc, Num_doc, telefono, email)
        self.__nomUser = nomUser
        self.__contrasenia = contrasenia
        self.__cargoUser = cargoUser
        self.__permisoUser = permisoUser
        
        
    #CAMBIAR DATOS:
    def set_nomUser(self, nomUser):
        self.__nomUser = nomUser
        
    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
        
    def set_cargoUser(self, cargoUser):
        self.__cargoUser = cargoUser
        
    def set_permisoUser(self, permisoUser):
        self.__permisoUser = permisoUser
        

    #OBTENER DATOS    
    def get_nomUser(self):
        return self.__nomUser

    def get_contrasenia(self):
        return self.__contrasenia
    
    def get_cargoUser(self):
        return self.__cargoUser
        
    def get_permisoUser(self):
        return self.__permisoUser
    
    
    #REGISTRO DE NUEVO USUARIO
    def Nuevo_Usuario(self):
        Usuario = self.get_nomUser()
        Password = self.get_contrasenia()
        Nombres = self.get_nombres()
        Apellidos = self.get_apellidos()
        Tipo_Doc = self.get_tipo_doc()
        Numero_Doc = self.get_num_doc()
        Celular = self.get_telefono()
        Email = self.get_email()
        Cargo = self.get_cargoUser()
        Permiso = self.get_permisoUser()
    
        
        DaoDocumento = DocumentoDao.DocumentoBD()
        DaoCargo = CargoDao.CargoBD()
        DaoPermiso = PermisoDao.PermisoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoPersona = PersonaDao.PersonaBD()
        DaoUsuario = UsuarioDao.UsuarioBD()
        
        #Obtencion de ID
        idDoc = DaoDocumento.ObtenerDocumentoID(Tipo_Doc)
        idCargo = DaoCargo.ObtenerCargoID(Cargo)
        idPermiso = DaoPermiso.ObtenerPermisoID(Permiso)
        
        #Insert en Tabla Contacto y Obtencion de ID
        DaoContacto.InsertTablaContacto(Celular, Email)
        idContacto = DaoContacto.ObtenerContactoID(Celular, Email)
        
        #Insert en Tabla Persona y Obtencion de ID
        DaoPersona.InsertTablaPersona(Nombres, Apellidos, Numero_Doc, idDoc, idContacto)
        idPersona = DaoPersona.ObtenerPersonaID(Nombres, Apellidos, Numero_Doc, idDoc, idContacto)
        
        #Insert en Tabla Usuario y Finalizacion del Registro
        DaoUsuario.InsertTablaUser(Usuario, Password, idPersona, idDoc, idContacto, idCargo, idPermiso)

        