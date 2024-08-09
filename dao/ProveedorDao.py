from util import ConexionBD


class ProveedorBD:
    
    def ObtenerProveedorID(self, RazonSocial, Numero_RUC, Direccion, idContacto, idRubro):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaProveedor = "SELECT idProveedor FROM proveedor WHERE RazonSocial = '{}' AND RUC = '{}' AND Direccion = '{}' AND Contacto_idContacto = '{}' AND Rubro_idRubro = '{}'".format(RazonSocial, Numero_RUC, Direccion, idContacto, idRubro)
        cursor.execute(ConsultaProveedor)
        objProveedorID = cursor.fetchone()
        objProveedor = objProveedorID[0]
        cursor.close()
        nbd.CloseConexion()
        return objProveedor
    
        
    def InsertTablaProveedor(self, RazonSocial, Numero_RUC, Direccion, idContacto, idRubro):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into proveedor(RazonSocial, RUC, Direccion, Contacto_idContacto, Rubro_idRubro) values('{}', '{}', '{}', '{}', '{}')".format(RazonSocial, Numero_RUC, Direccion, idContacto, idRubro)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        