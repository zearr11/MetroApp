from util import ConexionBD


class TipoDocVentaBD:
    
    def DataTipoDocVenta(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoDocVenta FROM tipodocventa")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerTipoDocVentaID(self, TipoDocVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTipoDocVenta = "SELECT idTipoDocVenta FROM tipodocventa WHERE TipoDocVenta = '{}'".format(TipoDocVenta)
        cursor.execute(ConsultaTipoDocVenta)
        ConsultaTipoDocVentaID = cursor.fetchone()
        objTipoDocVenta = ConsultaTipoDocVentaID[0]
        return objTipoDocVenta