from util import ConexionBD


class ClienteBD:
    
    def InsertTablaCliente(self, Direccion, idPersona, idDoc, idContac):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into cliente(Direccion, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto) values('{}', '{}', '{}', '{}')".format(Direccion, idPersona, idDoc, idContac)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()