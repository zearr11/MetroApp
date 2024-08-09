from util import ConexionBD

class UsuarioBD():
        
    def ConsultaLogin(self, user, clave):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaLog = "SELECT idUsuario FROM usuario WHERE BINARY NombUser = '{}' AND BINARY Password = '{}'".format(user, clave)
        cursor.execute(ConsultaLog)
        objLogin= cursor.fetchone()
        cursor.close()
        nbd.CloseConexion()
        
        if objLogin is None:
            return False
        else:
            return True
    
