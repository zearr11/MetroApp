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
    
    def ObtenerNumeroDocumentoID2(self, NumeroDoc):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaNumeroDocumento2 = "SELECT idNumeroDocumento FROM numerodocumento WHERE NumeroDoc = '{}'".format(NumeroDoc)
        cursor.execute(ConsultaNumeroDocumento2)
        objNumeroDocumento2ID = cursor.fetchone()
        objNumeroDocumento2 = objNumeroDocumento2ID[0]
        return objNumeroDocumento2
    
    def InsertTablaNumeroDocumento(self, NumeroDoc, idTipoDocumento): 
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into numerodocumento(NumeroDoc, TipoDocumento_idTipoDocumento) values ('{}', '{}')".format(NumeroDoc, idTipoDocumento)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def UpdateNumeroDocumento(self, NumeroDoc, idTipoDocumento, idNumDoc):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE numerodocumento SET NumeroDoc = '{}', TipoDocumento_idTipoDocumento = '{}' where idNumeroDocumento = '{}'".format(NumeroDoc, idTipoDocumento, idNumDoc)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
