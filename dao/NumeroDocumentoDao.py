from util import ConexionBD


class NumeroDocumentoBD:
    
    def ObtenerNumeroDocumentoID(self, NumeroDoc, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaNumeroDocumento = "SELECT idNumeroDocumento FROM numerodocumento WHERE NumeroDoc = '{}' AND TipoDocumento_idTipoDocumento = '{}'".format(NumeroDoc, idTipoDocumento)
        cursor.execute(ConsultaNumeroDocumento)
        objNumeroDocumentoID = cursor.fetchone()
        objNumeroDocumento = objNumeroDocumentoID[0]
        return objNumeroDocumento
    
    def InsertTablaNumeroDocumento(self, NumeroDoc, idTipoDocumento): 
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into numerodocumento(NumeroDoc, TipoDocumento_idTipoDocumento) values ('{}', '{}')".format(NumeroDoc, idTipoDocumento)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
