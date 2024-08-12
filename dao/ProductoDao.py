from util import ConexionBD


class ProductoBD:
    
    def InsertTablaProducto(self, Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "INSERT into producto(Descripcion, Marca, Cantidad, Precio, MedidaVenta_idMedidaVenta, Estado_idEstado, Categoria_idCategoria) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ConsultaTablaProducto(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTablaProducto = "SELECT c.idProducto, c.Descripcion, c.Marca, i.MedidaVenta, c.Precio, c.Cantidad, t.TipoCategoria, o.Estado FROM producto c INNER JOIN medidaventa i ON c.MedidaVenta_idMedidaVenta = i.idMedidaVenta INNER JOIN categoria t ON c.Categoria_idCategoria = t.idCategoria INNER JOIN estado o ON c.Estado_idEstado = o.idEstado"
        cursor.execute(ConsultaTablaProducto)
        return cursor.fetchall()
    
    def ObtenerProducto(self, idProducto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerProducto = "SELECT c.idProducto, c.Descripcion, c.Marca, i.MedidaVenta, c.Precio, c.Cantidad, t.TipoCategoria, o.Estado FROM producto c INNER JOIN medidaventa i ON c.MedidaVenta_idMedidaVenta = i.idMedidaVenta INNER JOIN categoria t ON c.Categoria_idCategoria = t.idCategoria INNER JOIN estado o ON c.Estado_idEstado = o.idEstado where c.idProducto = '{}'".format(idProducto)
        cursor.execute(ObtenerProducto)
        return cursor.fetchone()
    
    def UpdateProducto(self, Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria, idProducto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE producto SET Descripcion = '{}', Marca = '{}' , Cantidad = '{}' , Precio = '{}' , MedidaVenta_idMedidaVenta = '{}' , Estado_idEstado = '{}' , Categoria_idCategoria = '{}' where idProducto = '{}'".format(Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria, idProducto)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()