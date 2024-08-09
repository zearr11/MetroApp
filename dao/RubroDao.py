from util import ConexionBD


class RubroBD:
    
    def DataRubro(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoRubro FROM rubro")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]

    def ObtenerRubroID(self, TipoRubro):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaRubro = "SELECT idRubro FROM rubro WHERE TipoRubro = '{}'".format(TipoRubro)
        cursor.execute(ConsultaRubro)
        objRubroID = cursor.fetchone()
        objRubro = objRubroID[0]
        cursor.close()
        nbd.CloseConexion()
        return objRubro