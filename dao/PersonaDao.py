from util import ConexionBD


class PersonaBD:   
    
    def ObtenerPersonaID(self, Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPersona = "SELECT idPersona FROM persona WHERE Nombres = '{}' AND Apellidos = '{}' AND Contacto_idContacto = '{}' AND NumeroDocumento_idNumeroDocumento = '{}' AND NumeroDocumento_TipoDocumento_idTipoDocumento = '{}'".format(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)
        cursor.execute(ConsultaPersona)
        objPersonaID = cursor.fetchone()
        objPersona = objPersonaID[0]
        return objPersona
    
        
    def InsertTablaPersona(self,Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into persona(Nombres, Apellidos, Contacto_idContacto, NumeroDocumento_idNumeroDocumento, NumeroDocumento_TipoDocumento_idTipoDocumento) values('{}', '{}', '{}', '{}', '{}')".format(Nombres, Apellidos, idContacto, idNumeroDocumento, idTipoDocumento)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        