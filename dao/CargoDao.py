from util import ConexionBD


class CargoBD:
    
    def DataCargo(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoCargo FROM cargo")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]
    
    def ObtenerCargoID(self, cargo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCargo = "SELECT idCargo FROM cargo WHERE TipoCargo = '{}'".format(cargo)
        cursor.execute(ConsultaCargo)
        objCargoID = cursor.fetchone()
        objCargo = objCargoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objCargo