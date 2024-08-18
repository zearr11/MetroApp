from util import ConexionBD


class DetalleCompraBD:
    
    def InsertTablaDetalleCompra(self, CantProdUni, TotalxProd, idProducto, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into detallecompra(CantidadProdCompr, TotalXProd, Producto_idProducto, Compra_idCompra) values ('{}', '{}', '{}', '{}')".format(CantProdUni, TotalxProd, idProducto, idCompra)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerProdComprados(self, idCompra):####PRUEBA
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerDatosDeVenta = "SELECT p.idProducto, p.Descripcion, p.Marca, mv.MedidaVenta, p.Precio, dv.CantidadProdCompr, dv.TotalXProd from detallecompra dv inner join producto p on dv.Producto_idProducto = p.idProducto inner join medidaventa mv on p.MedidaVenta_idMedidaVenta = mv.idMedidaVenta where dv.Compra_idCompra = '{}'".format(idCompra)
        cursor.execute(ObtenerDatosDeVenta)
        return cursor.fetchall()
    
    def ObtenerAllProdDescYCant(self, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerAllProdDescYCant = "select p.Descripcion, dc.CantidadProdCompr from detallecompra dc inner join producto p on p.idProducto = Producto_idProducto where Compra_idCompra = '{}'".format(idCompra)
        cursor.execute(ObtenerAllProdDescYCant)
        return cursor.fetchall()
    
    def ObtenerIDdetalleCompras(self, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerIDdetalleCompras = "select idDetalleCompra from detallecompra where Compra_idCompra = '{}'".format(idCompra)
        cursor.execute(ObtenerIDdetalleCompras)
        return cursor.fetchall()
    
    def ObtenerIDAllProductosCompras(self, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerIDAllProductosCompras = "select Producto_idProducto from detallecompra where Compra_idCompra = '{}'".format(idCompra)
        cursor.execute(ObtenerIDAllProductosCompras)
        return cursor.fetchall()
    
    def ObtenerCantidadAumentada(self, idDetalleCompra, idProducto, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerCantidadAumentada = "select CantidadProdCompr from detallecompra where idDetalleCompra = '{}' and Producto_idProducto = '{}' and Compra_idCompra = '{}'".format(idDetalleCompra, idProducto, idCompra)
        cursor.execute(ObtenerCantidadAumentada)
        ObtenerCantidadAumentadaS = cursor.fetchone()
        ObtenerCantidadAumentadaOne = ObtenerCantidadAumentadaS[0]
        return ObtenerCantidadAumentadaOne
    
    def ObtenerCantidadProdComprXUserandFecha(self, DateDesde, DateHasta, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Consulta = "select dv.CantidadProdCompr from detallecompra dv inner join compra v on v.idCompra = dv.Compra_idCompra inner join usuario u on u.idUsuario = v.Usuario_idUsuario where v.Fecha between '{}' and '{}' and u.idUsuario = '{}'".format(DateDesde, DateHasta, idUsuario)
        cursor.execute(Consulta)
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def ObtenerTotalDineroGastado(self, DateDesde, DateHasta, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Consulta = "select dv.TotalXProd from detallecompra dv inner join compra v on v.idCompra = dv.Compra_idCompra inner join usuario u on u.idUsuario = v.Usuario_idUsuario where v.Fecha between '{}' and '{}' and u.idUsuario = '{}'".format(DateDesde, DateHasta, idUsuario)
        cursor.execute(Consulta)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
