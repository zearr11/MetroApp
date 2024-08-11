from util import ConexionBD

class EstadoBD:
    
    def DataEstado(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT Estado FROM estado")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerEstadoID(self, Estado):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaEstado = "SELECT idEstado FROM estado where Estado = '{}'".format(Estado)
        cursor.execute(ConsultaEstado)
        objEstadoID = cursor.fetchone()
        objEstado = objEstadoID[0]
        return objEstado
    
    