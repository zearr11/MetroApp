from util import ConexionBD


class PermisoBD:
    
    def DataPermisos(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoPermiso FROM permisos")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]
    
    def ObtenerPermisoID(self, permiso):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPermiso = "SELECT idPermisos FROM permisos WHERE TipoPermiso = '{}'".format(permiso)
        cursor.execute(ConsultaPermiso)
        objPermisoID = cursor.fetchone()
        objPermiso = objPermisoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objPermiso