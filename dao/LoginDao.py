from util import ConexionBD


class LoginBD:
        
    def ConsultaLogin(self, NombUser, Password):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaLog = "SELECT idUsuario FROM usuario WHERE BINARY NombUser = '{}' AND BINARY Password = '{}'".format(NombUser, Password)
        cursor.execute(ConsultaLog)
        objLogin= cursor.fetchone()
        
        if objLogin is None:
            return False
        else:
            return True
        
    def ObtenerUsuarioLogin(self, NombUser, Password):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaUsuarioLogin = "SELECT idUsuario FROM usuario WHERE NombUser = '{}' AND Password = '{}'".format(NombUser, Password)
        cursor.execute(ConsultaUsuarioLogin)
        objUsuarioLogID = cursor.fetchone()
        objUsuarioLog = objUsuarioLogID[0]
        return objUsuarioLog
    
    def InsertTablaLog(self, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "INSERT into logusers(Usuario_idUsuario) values('{}')".format(idUsuario)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
    
    def ObtenerUltimoUsuario(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaUltimoUsuario = "SELECT Usuario_idUsuario FROM logusers ORDER BY idLogUsers DESC LIMIT 1"
        cursor.execute(ConsultaUltimoUsuario)
        objUltimoUsuarioID = cursor.fetchone()
        objUltimoUsuario = objUltimoUsuarioID[0]
        return objUltimoUsuario
    
    def ConsultaPermiso(self, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPermiso = "SELECT pe.idPermisos from usuario u inner join permisos pe on pe.idPermisos = Permisos_idPermisos where u.idUsuario = '{}'".format(idUsuario)
        cursor.execute(ConsultaPermiso)
        objPermisoID = cursor.fetchone()
        objPermiso = objPermisoID[0]
        return objPermiso