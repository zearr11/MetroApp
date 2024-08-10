from util import ConexionBD


class CategoriaBD:
    
    def DataCategoria(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoCategoria FROM categoria")
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def ObtenerCategoriaID(self, TipoCategoria):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCategoria = "SELECT idCategoria FROM categoria WHERE TipoCategoria = '{}'".format(TipoCategoria)
        cursor.execute(ConsultaCategoria)
        objCategoriaID = cursor.fetchone()
        objCategoria = objCategoriaID[0]
        return objCategoria