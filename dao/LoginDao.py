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
