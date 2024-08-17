from util import ConexionBD


class GuiaEntradaBD:
    
    def InsertTablaGuiaEntrada(self, recepcion, idDetalleCompra, idProducto, idCompra):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into guiaentrada(Recepcion, DetalleCompra_idDetalleCompra, DetalleCompra_Producto_idProducto, DetalleCompra_Compra_idCompra) values('{}', '{}', '{}', '{}')".format(recepcion, idDetalleCompra, idProducto, idCompra)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()