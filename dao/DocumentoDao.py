from util import ConexionBD


class DocumentoBD:
    
    def DataDocumentos(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoDoc FROM documento")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]

    def ObtenerDocumentoID(self, tipoDOC):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaDOC = "SELECT idDocumento FROM documento WHERE TipoDoc = '{}'".format(tipoDOC)
        cursor.execute(ConsultaDOC)
        objDocumentoID = cursor.fetchone()
        objDocumento = objDocumentoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objDocumento