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
    
    def ObtenerProducto2(self, Descripcion):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerProducto2 = "SELECT c.idProducto, c.Descripcion, c.Marca, i.MedidaVenta, c.Precio FROM producto c INNER JOIN medidaventa i ON c.MedidaVenta_idMedidaVenta = i.idMedidaVenta WHERE  c.Estado_idEstado = 2 AND c.Descripcion = '{}'".format(Descripcion)
        cursor.execute(ObtenerProducto2)
        return cursor.fetchone()
    
    def UpdateProducto(self, Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria, idProducto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE producto SET Descripcion = '{}', Marca = '{}' , Cantidad = '{}' , Precio = '{}' , MedidaVenta_idMedidaVenta = '{}' , Estado_idEstado = '{}' , Categoria_idCategoria = '{}' where idProducto = '{}'".format(Descripcion, Marca, Cantidad, Precio, idMedidaVenta, idEstado, idCategoria, idProducto)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
        
    def DataProducto(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT Descripcion FROM producto WHERE Estado_idEstado = 2")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def DataAllProducto(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT Descripcion FROM producto")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def UpdateCantProd(self, Cantidad, idProducto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE producto SET Cantidad = '{}' where idProducto = '{}'".format(Cantidad, idProducto)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
    
    def ObtenerCantidadProd(self, idProducto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerCantidadProd = "select cantidad from producto where idProducto = '{}'".format(idProducto)
        cursor.execute(ObtenerCantidadProd)
        ObtenerCantidadProdS = cursor.fetchone()
        ObtenerCantidadProdOne = ObtenerCantidadProdS[0]
        return ObtenerCantidadProdOne
    
    def ObtenerArtXcat(self, idCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Consulta = "SELECT concat(p.Descripcion,' ',p.Marca) as Articulo from producto p where Categoria_idCategoria = '{}'".format(idCategoria)
        cursor.execute(Consulta)
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    