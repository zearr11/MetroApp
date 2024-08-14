from model.HerenciasModel import PersonaCLASS, CargoCLASS, PermisosCLASS
from dao import	TipoDocumentoDao, CargoDao, PermisoDao, NumeroDocumentoDao, ContactoDao, PersonaDao, UsuarioDao


class UsuariosCLASS(PersonaCLASS, CargoCLASS, PermisosCLASS):
    
    def __init__(self, NombUser="", Password="", Nombres="", Apellidos="", Telefono="", Email="", NumeroDoc="", TipoDoc="", TipoCargo="", TipoPermiso=""):
        super().__init__(Nombres, Apellidos, Telefono, Email, NumeroDoc, TipoDoc)
        CargoCLASS.__init__(self, TipoCargo)
        PermisosCLASS.__init__(self, TipoPermiso)
        self.__NombUser = NombUser
        self.__Password = Password
        
    #CAMBIAR DATOS:
    def set_NombUser(self, NombUser):
        self.__NombUser = NombUser
        
    def set_Password(self, Password):
        self.__Password = Password
    
    #OBTENER DATOS    
    def get_NombUser(self):
        return self.__NombUser

    def get_Password(self):
        return self.__Password
    
    
    def Nuevo_Usuario(self):
        Usuario = self.get_NombUser()
        Password = self.get_Password()
        Nombres = self.get_Nombres()
        Apellidos = self.get_Apellidos()
        Tipo_Doc = self.get_TipoDoc()
        Numero_Doc = self.get_NumeroDoc()
        Celular = self.get_Telefono()
        Email = self.get_Email()
        Cargo = self.get_TipoCargo()
        Permiso = self.get_TipoPermiso()
    
        DaoTipoDocumento = TipoDocumentoDao.TipoDocumentoBD()
        DaoCargo = CargoDao.CargoBD()
        DaoPermiso = PermisoDao.PermisoBD()
        DaoNumeroDocumento = NumeroDocumentoDao.NumeroDocumentoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoPersona = PersonaDao.PersonaBD()
        DaoUsuario = UsuarioDao.UsuarioBD()
        
        #Obtencion de ID
        idTipoDocumento = DaoTipoDocumento.ObtenerTipoDocumentoID(Tipo_Doc)
        idCargo = DaoCargo.ObtenerCargoID(Cargo)
        idPermisos = DaoPermiso.ObtenerPermisoID(Permiso)
        
        #Insert en Tabla NumeroDocumento y Obtencion de ID
        DaoNumeroDocumento.InsertTablaNumeroDocumento(Numero_Doc, idTipoDocumento)
        idNumeroDocumento = DaoNumeroDocumento.ObtenerNumeroDocumentoID(Numero_Doc, idTipoDocumento)
                
        #Insert en Tabla Contacto y Obtencion de ID
        DaoContacto.InsertTablaContacto(Celular, Email)
        idContacto = DaoContacto.ObtenerContactoID(Celular, Email)
        
        #Insert en Tabla Persona y Obtencion de ID
        DaoPersona.InsertTablaPersona(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)
        idPersona = DaoPersona.ObtenerPersonaID(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)
        
        #Insert en Tabla Usuario y Finalizacion del Registro
        DaoUsuario.InsertTablaUser(Usuario, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento)
        
        
    def Actualizar_Usuario(self, userNew, paswNew, celNew, emaNew, cargoNew, permisoNew, idU):
        Celular = self.get_Telefono()
        Email = self.get_Email()
        
        DaoCargo = CargoDao.CargoBD()
        DaoPermiso = PermisoDao.PermisoBD()
        DaoContacto = ContactoDao.ContactoBD()
        DaoUsuario = UsuarioDao.UsuarioBD()
        
        #ObtencionID's Principales
        idContacto = DaoContacto.ObtenerContactoID(Celular, Email)
        idCargo = DaoCargo.ObtenerCargoID(cargoNew)
        idPermisos = DaoPermiso.ObtenerPermisoID(permisoNew)
        
        DaoContacto.UpdateContacto(celNew, emaNew, idContacto)
        DaoUsuario.UpdateUsuario(userNew, paswNew, idCargo, idPermisos, idU)
        
        
    