from util import ConexionBD


class ReporteSalidaBD:
    
    def InsertTablaReporteSalida(self, idGuiaSalida, idProducto, CantidadProd, TotalXproduct):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into reportedesalida(GuiaSalida_idGuiaSalida, Producto_idProducto, CantidadProd, TotalXproduct) values ('{}', '{}', '{}', '{}')".format(idGuiaSalida, idProducto, CantidadProd, TotalXproduct)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ConsultaCantYtotXGuiaSalida(self, idGuiaSalida):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCantYtotXGuiaSalida = "select CantidadProd, TotalXproduct from reportedesalida where GuiaSalida_idGuiaSalida = '{}'".format(idGuiaSalida)
        cursor.execute(ConsultaCantYtotXGuiaSalida)
        return cursor.fetchall()