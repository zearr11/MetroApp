from util import ConexionBD


class CargoBD:
    
    def DataCargo(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoCargo FROM cargo")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerCargoID(self, TipoCargo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCargo = "SELECT idCargo FROM cargo WHERE TipoCargo = '{}'".format(TipoCargo)
        cursor.execute(ConsultaCargo)
        objCargoID = cursor.fetchone()
        objCargo = objCargoID[0]
        return objCargo