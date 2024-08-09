from util import ConexionBD


class PersonaBD:   
    
    def ObtenerPersonaID(self, Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPersona = "SELECT idPersona FROM persona WHERE Nombres = '{}' AND Apellidos = '{}' AND NumeroDocumento = '{}' AND Documento_idDocumento = '{}' AND Contacto_idContacto = '{}'".format(Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto)
        cursor.execute(ConsultaPersona)
        objPersonaID = cursor.fetchone()
        objPersona = objPersonaID[0]
        cursor.close()
        nbd.CloseConexion()
        return objPersona
    
        
    def InsertTablaPersona(self, Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into persona(Nombres, Apellidos, NumeroDocumento, Documento_idDocumento, Contacto_idContacto) values('{}', '{}', '{}', '{}', '{}')".format(Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        