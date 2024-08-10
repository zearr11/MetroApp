from util import ConexionBD


class ClienteBD:
    
    def InsertTablaCliente(self, Direccion, idPersona, idContac, idNumeroDoc, idTipoDoc):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into cliente(Direccion, Persona_idPersona, Persona_Contacto_idContacto, Persona_NumeroDocumento_idNumeroDocumento, Persona_NumeroDocumento_TipoDocumento_idTipoDocumento) values('{}', '{}', '{}', '{}', '{}')".format(Direccion, idPersona, idContac, idNumeroDoc, idTipoDoc)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()