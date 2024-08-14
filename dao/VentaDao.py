from util import ConexionBD

class VentaBD:
    
    def InsertTablaVenta(self, Fecha, idMedioPago, idUsuario, idCliente, idDocumentoVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into venta(Fecha, MedioPago_idMedioPago, Usuario_idUsuario, Cliente_idCliente, DocumentodeVenta_idDocumentodeVenta) values ( '{}', '{}', '{}', '{}', '{}')".format(Fecha, idMedioPago, idUsuario, idCliente, idDocumentoVenta)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerVentaID(self, Fecha, idMedioPago, idUsuario, idCliente, idDocumentoVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaVenta = "select idVenta from venta where Fecha = '{}' and MedioPago_idMedioPago = '{}' and Usuario_idUsuario = '{}' and Cliente_idCliente = '{}' and DocumentodeVenta_idDocumentodeVenta = '{}'".format(Fecha, idMedioPago, idUsuario, idCliente, idDocumentoVenta)
        cursor.execute(ConsultaVenta)
        objVentaID = cursor.fetchone()
        objVenta = objVentaID[0]
        return objVenta
    
    def ObtenerUltimaVentaID(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaUltimaVentaID = "SELECT idVenta FROM VENTA ORDER BY idVenta DESC LIMIT 1"
        cursor.execute(ConsultaUltimaVentaID)
        objUltimaVentaID = cursor.fetchone()
        objUltimaVenta = objUltimaVentaID[0]
        return objUltimaVenta
    
    def DatosVenta(self, idVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        DtaVenta = "SELECT p_u.Nombres,p_u.Apellidos,dv.NumeroDocumentoVenta,p_c.Nombres,p_c.Apellidos,nd.NumeroDoc,ve.Fecha,l.TipoPago,wa.TipoDocVenta,dv.Subtotal,dv.IGV,dv.TotalCancelado FROM venta ve INNER JOIN usuario u ON ve.Usuario_idUsuario=u.idUsuario INNER JOIN persona p_u ON u.Persona_idPersona=p_u.idPersona INNER JOIN documentodeventa dv ON ve.DocumentodeVenta_idDocumentodeVenta=dv.idDocumentodeVenta INNER JOIN mediopago l ON ve.MedioPago_idMedioPago=l.idMedioPago INNER JOIN cliente c ON ve.Cliente_idCliente=c.idCliente INNER JOIN persona p_c ON c.Persona_idPersona=p_c.idPersona INNER JOIN numerodocumento nd ON p_c.NumeroDocumento_idNumeroDocumento=nd.idNumeroDocumento INNER JOIN tipodocventa wa ON wa.idTipoDocVenta=dv.TipoDocVenta_idTipoDocVenta WHERE ve.idVenta='{}'".format(idVenta)
        cursor.execute(DtaVenta)
        return cursor.fetchone()