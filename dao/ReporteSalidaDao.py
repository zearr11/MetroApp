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
    
    def ConsultaTablaSalidaProductos(self, FechaDesde, FechaHasta):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerTablaEntradaProductos = "select gs.idGuiaSalida, p.idProducto, CONCAT(p.Descripcion, ' ', p.Marca) AS Articulo, rs.CantidadProd, gs.Fecha from reportedesalida rs inner join guiasalida gs on rs.GuiaSalida_idGuiaSalida = gs.idGuiaSalida inner join producto p on rs.Producto_idProducto = p.idProducto where gs.Fecha between '{}' and '{}' order by gs.idGuiaSalida asc".format(FechaDesde, FechaHasta)
        cursor.execute(ObtenerTablaEntradaProductos)
        return cursor.fetchall()