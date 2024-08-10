from util import ConexionBD


class UsuarioBD:
    
    def InsertTablaUser(self, NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into usuario(NombUser, Password, Cargo_idCargo, Permisos_idPermisos, Persona_idPersona, Persona_Contacto_idContacto, Persona_NumeroDocumento_idNumeroDocumento, Persona_NumeroDocumento_TipoDocumento_idTipoDocumento) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()