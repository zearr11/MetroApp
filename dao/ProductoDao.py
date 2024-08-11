from util import ConexionBD


class ProductoBD:
    
    def InsertTablaProducto(self, Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "INSERT into producto(Descripcion, Marca, Cantidad, Precio, MedidaVenta_idMedidaVenta, Estado_idEstado, Categoria_idCategoria) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()