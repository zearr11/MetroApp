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
        