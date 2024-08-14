from util import ConexionBD

class MedioPagoBD:
    
    def DataMedioPago(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoPago FROM mediopago")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerMedioPagoID(self, TipoPago):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTipoPago = "SELECT idMedioPago FROM mediopago WHERE TipoPago = '{}'".format(TipoPago)
        cursor.execute(ConsultaTipoPago)
        ConsultaTipoPagoID = cursor.fetchone()
        objTipoPago = ConsultaTipoPagoID[0]
        return objTipoPago