from util import ConexionBD


class GuiaEntradaBD:
    
    def InsertTablaGuiaEntrada(self, FechaRecepcion, recepcion, idDetalleCompra, idProducto, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into guiaentrada(FechaRecepcion, Recepcion, DetalleCompra_idDetalleCompra, DetalleCompra_Producto_idProducto, DetalleCompra_Compra_idCompra) values('{}', '{}', '{}', '{}', '{}')".format(FechaRecepcion, recepcion, idDetalleCompra, idProducto, idCompra)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ConsultaTablaEntradaProductos(self, FechaDesde, FechaHasta):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerTablaEntradaProductos = "select co.idCompra, p.idProducto, concat(p.Descripcion,' ',p.Marca) as Articulo, dc.CantidadProdCompr, ge.Recepcion, ge.FechaRecepcion from guiaentrada ge inner join detallecompra dc on dc.idDetalleCompra = ge.DetalleCompra_idDetalleCompra inner join producto p on p.idProducto = ge.DetalleCompra_Producto_idProducto inner join compra co on co.idCompra = ge.DetalleCompra_Compra_idCompra where ge.FechaRecepcion between '{}' and '{}' order by co.idCompra".format(FechaDesde, FechaHasta)
        cursor.execute(ObtenerTablaEntradaProductos)
        return cursor.fetchall()