from util import ConexionBD


class TipoDocumentoBD:
    
    def DataTipoDocumento(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoDoc FROM tipodocumento")
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def ObtenerTipoDocumentoID(self, TipoDoc):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTipoDocumento = "SELECT idTipoDocumento FROM tipodocumento WHERE TipoDoc = '{}'".format(TipoDoc)
        cursor.execute(ConsultaTipoDocumento)
        objTipoDocumentoID = cursor.fetchone()
        objTipoDocumento = objTipoDocumentoID[0]
        return objTipoDocumento