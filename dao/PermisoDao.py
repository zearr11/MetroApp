from util import ConexionBD


class PermisoBD:
    
    def DataPermisos(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoPermiso FROM permisos")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerPermisoID(self, TipoPermiso):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPermiso = "SELECT idPermisos FROM permisos WHERE TipoPermiso = '{}'".format(TipoPermiso)
        cursor.execute(ConsultaPermiso)
        objPermisoID = cursor.fetchone()
        objPermiso = objPermisoID[0]
        return objPermiso