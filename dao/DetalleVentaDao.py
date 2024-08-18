from util import ConexionBD


class DetalleVentaBD:
    
    def InsertTablaDetalleVenta(self, CantProd, TotalProd, idProducto, idVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into detalleventa(CantidadProd, Total, Producto_idProducto, Venta_idVenta) values ('{}', '{}', '{}', '{}')".format(CantProd, TotalProd, idProducto, idVenta)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerProdVendidos(self, idVenta):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerDatosDeVenta = "SELECT p.idProducto, p.Descripcion, p.Marca, mv.MedidaVenta, p.Precio, dv.CantidadProd, dv.Total from detalleventa dv inner join producto p on dv.Producto_idProducto = p.idProducto inner join medidaventa mv on p.MedidaVenta_idMedidaVenta = mv.idMedidaVenta where Venta_idVenta = '{}'".format(idVenta)
        cursor.execute(ObtenerDatosDeVenta)
        return cursor.fetchall()
    
    def ObtenerCantidadProdVendXUserandFecha(self, DateDesde, DateHasta, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Consulta = "select dv.CantidadProd from detalleventa dv inner join venta v on v.idVenta = dv.Venta_idVenta inner join usuario u on u.idUsuario = v.Usuario_idUsuario where v.Fecha between '{}' and '{}' and u.idUsuario = '{}'".format(DateDesde, DateHasta, idUsuario)
        cursor.execute(Consulta)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerTotalDineroObtenido(self, DateDesde, DateHasta, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Consulta = "select dv.Total from detalleventa dv inner join venta v on v.idVenta = dv.Venta_idVenta inner join usuario u on u.idUsuario = v.Usuario_idUsuario where v.Fecha between '{}' and '{}' and u.idUsuario = '{}'".format(DateDesde, DateHasta, idUsuario)
        cursor.execute(Consulta)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
        
        