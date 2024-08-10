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
        
        