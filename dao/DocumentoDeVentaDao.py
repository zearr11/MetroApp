from util import ConexionBD

class DocumentodeVentaCLASS:
    
    def InsertTablaDocumentodeVenta(self, SubTotal, IGV, TotalCancelado, idTipoDocVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "INSERT into documentodeventa(SubTotal, IGV, TotalCancelado, TipoDocVenta_idTipoDocVenta) values('{}', '{}', '{}', '{}')".format(SubTotal, IGV, TotalCancelado, idTipoDocVenta)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerUltimoDocumentoDeVentaID(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaUltimoDocumentoDeVenta = "SELECT idDocumentodeVenta FROM documentodeventa ORDER BY idDocumentodeVenta DESC LIMIT 1"
        cursor.execute(ConsultaUltimoDocumentoDeVenta)
        objUltimoDocumentoDeVentaID = cursor.fetchone()
        objUltimoDocumentoDeVenta = objUltimoDocumentoDeVentaID[0]
        return objUltimoDocumentoDeVenta
    