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
        