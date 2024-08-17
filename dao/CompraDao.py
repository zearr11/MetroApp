from util import ConexionBD

class CompraBD:
    
    def InsertTablaCompra(self, Fecha, Estado, idUsuario, idDocumentoVenta, idProveedor):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "INSERT into compra(Fecha, Estado, Usuario_idUsuario, DocumentodeVenta_idDocumentodeVenta, Proveedor_idProveedor) values ( '{}', '{}', '{}', '{}', '{}')".format(Fecha, Estado, idUsuario, idDocumentoVenta, idProveedor)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerCompraID(self, Fecha, idUsuario, idDocumentoVenta, idProveedor):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCompra = "select idCompra from compra where Fecha = '{}' and Usuario_idUsuario = '{}' and DocumentodeVenta_idDocumentodeVenta = '{}' and Proveedor_idProveedor = '{}'".format(Fecha, idUsuario, idDocumentoVenta, idProveedor)
        cursor.execute(ConsultaCompra)
        objCompraID = cursor.fetchone()
        objCompra = objCompraID[0]
        return objCompra
    
    def DatosCompra(self, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        DtaCompra = "Select p_u.Nombres, p_u.Apellidos, dv.NumeroDocumentoVenta, b.RazonSocial, b.RUC, ve.Fecha, dv.SubTotal, dv.IGV, dv.TotalCancelado from compra ve INNER JOIN usuario u ON ve.Usuario_idUsuario = u.idUsuario INNER JOIN persona p_u ON u.Persona_idPersona=p_u.idPersona INNER JOIN documentodeventa dv ON ve.DocumentodeVenta_idDocumentodeVenta=dv.idDocumentodeVenta INNER JOIN proveedor b ON ve.Proveedor_idProveedor = b.idProveedor where idCompra = '{}'".format(idCompra)
        cursor.execute(DtaCompra)
        return cursor.fetchone()
    
    def ConsultaTablaCompras(self):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerTablaCompras = "Select ve.idCompra, p_u.Nombres, p_u.Apellidos, ve.Fecha, dv.NumeroDocumentoVenta, b.RazonSocial, b.RUC, dv.TotalCancelado, ve.Estado from compra ve INNER JOIN usuario u ON ve.Usuario_idUsuario = u.idUsuario INNER JOIN persona p_u ON u.Persona_idPersona=p_u.idPersona INNER JOIN documentodeventa dv ON ve.DocumentodeVenta_idDocumentodeVenta=dv.idDocumentodeVenta  INNER JOIN proveedor b ON ve.Proveedor_idProveedor = b.idProveedor order by idCompra asc"
        cursor.execute(ObtenerTablaCompras)
        return cursor.fetchall()
    
    def ObtenerIDsAllCompras(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("select idCompra from compra where Estado = 'En curso'")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def UpdateEstadoCompra(self, Estado, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "update compra set Estado = '{}' where idCompra = '{}'".format(Estado, idCompra)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
