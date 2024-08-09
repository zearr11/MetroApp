from util import ConexionBD


class UsuarioBD:
    
    def InsertTablaUser(self, NameUser, Contrasenia, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into usuario(NombUser, Password, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(NameUser, Contrasenia, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()