from util import ConexionBD

class MedidaVentaBD:
    
    def DataMedidaVenta(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT MedidaVenta FROM medidaventa")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerMedidaVentaID(self, MedidaVenta):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaMedidaVentaID = "SELECT idMedidaVenta FROM medidaventa where MedidaVenta = '{}'".format(MedidaVenta)
        cursor.execute(ConsultaMedidaVentaID)
        objMedidaVentaID = cursor.fetchone()
        objMedidaVenta = objMedidaVentaID[0]
        return objMedidaVenta