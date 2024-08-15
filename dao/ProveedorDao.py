from util import ConexionBD


class ProveedorBD:
    
    def ObtenerProveedorID(self, RazonSocial, Numero_RUC, Direccion, idContacto, idCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaProveedor = "SELECT idProveedor FROM proveedor WHERE RazonSocial = '{}' AND RUC = '{}' AND Direccion = '{}' AND Contacto_idContacto = '{}' AND Categoria_idCategoria = '{}'".format(RazonSocial, Numero_RUC, Direccion, idContacto, idCategoria)
        cursor.execute(ConsultaProveedor)
        objProveedorID = cursor.fetchone()
        objProveedor = objProveedorID[0]
        return objProveedor
        
    def InsertTablaProveedor(self, RazonSocial, Numero_RUC, Direccion, idContacto, idCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into proveedor(RazonSocial, RUC, Direccion, Contacto_idContacto, Categoria_idCategoria) values('{}', '{}', '{}', '{}', '{}')".format(RazonSocial, Numero_RUC, Direccion, idContacto, idCategoria)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ConsultaTablaProveedor(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTablaProveedor = "SELECT p.idProveedor, p.RazonSocial, p.RUC, p.Direccion, c.Email, c.Telefono, a.TipoCategoria from proveedor p inner join contacto c on p.Contacto_idContacto = c.idContacto inner join categoria a on p.Categoria_idCategoria = a.idCategoria"
        cursor.execute(ConsultaTablaProveedor)
        return cursor.fetchall()
    
    def ObtenerProveedor(self, idProve):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerProveedor = "SELECT p.idProveedor, p.RazonSocial, p.RUC, p.Direccion, c.Email, c.Telefono, a.TipoCategoria from proveedor p inner join contacto c on p.Contacto_idContacto = c.idContacto inner join categoria a on p.Categoria_idCategoria = a.idCategoria where p.idProveedor = '{}'".format(idProve)
        cursor.execute(ObtenerProveedor)
        return cursor.fetchone()
        
    def UpdateProveedor(self, RazonSocial, nRUC, Direccion, idCategoria, idProveedor):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE proveedor SET RazonSocial = '{}', RUC ='{}', Direccion = '{}', Categoria_idCategoria = '{}' WHERE idProveedor = '{}'".format(RazonSocial, nRUC, Direccion, idCategoria, idProveedor)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()