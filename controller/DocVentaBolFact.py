from PyQt5 import uic
from dao import VentaDao, DocumentoDeVentaDao, TipoDocVentaDao, DetalleVentaDao
from PyQt5.QtWidgets import QTableWidgetItem
from controller import MenuPrincipal

class DocVentaBolFactFRM:
    def __init__(self):
        self.docventa = uic.loadUi("view/FRM_DOC_VENTA.ui")
        self.docventa.setWindowTitle("Documento de Venta")
        
        self.VentaDao = VentaDao.VentaBD()
        self.DocVentDao = DocumentoDeVentaDao.DocumentodeVentaCLASS()
        self.TipoDocVentaDao = TipoDocVentaDao.TipoDocVentaBD()
        self.DetalleVentaDao = DetalleVentaDao.DetalleVentaBD()
        
        self.docventa.bt_retornoMenu.clicked.connect(self.RetornoMenu)
        
        self.InsertEnTabla()
        self.docventa.show()
        
    def InsertEnTabla(self):
        
        #Obtener ID de Venta y Productos Vendidos
        self.idVenta = self.VentaDao.ObtenerUltimaVentaID()
        LstProdVendidos = self.DetalleVentaDao.ObtenerProdVendidos(self.idVenta)
        Cantidad = len(LstProdVendidos)
        self.docventa.tw_venta.setRowCount(Cantidad)
        Fila = 0
        
        for i in LstProdVendidos:
            self.docventa.tw_venta.setItem(Fila, 0, QTableWidgetItem(str(i[0])))
            self.docventa.tw_venta.setItem(Fila, 1, QTableWidgetItem(i[1]))
            self.docventa.tw_venta.setItem(Fila, 2, QTableWidgetItem(i[2]))
            self.docventa.tw_venta.setItem(Fila, 3, QTableWidgetItem(i[3]))
            self.docventa.tw_venta.setItem(Fila, 4, QTableWidgetItem("S/ " + str(round(float(i[4]), 2))))
            self.docventa.tw_venta.setItem(Fila, 5, QTableWidgetItem(i[5]))
            self.docventa.tw_venta.setItem(Fila, 6, QTableWidgetItem("S/ " + str(round(float(i[6]), 2))))
            Fila +=1
            
        self.DataVenta()
            
    def RetornoMenu(self):
        self.docventa.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def DataVenta(self):
        Data = self.VentaDao.DatosVenta(self.idVenta)
        self.docventa.n_user.setText(Data[0]+" "+Data[1])
        self.docventa.n_cliente.setText(Data[3]+" "+Data[4])
        self.docventa.dni_cliente.setText(Data[5])
        self.docventa.lb_fcha.setText(str(Data[6]))
        self.docventa.pago.setText(Data[7])
        self.docventa.subt.setText("S/ " + str(round(float(Data[9]), 2)))
        self.docventa.igvt.setText("S/ " + str(round(float(Data[10]), 2)))
        self.docventa.totalt.setText("S/ " + str(round(float(Data[11]), 2)))
        
        
        if Data[8] == "Boleta":
            self.docventa.bol_fact.setText("Boleta de Venta Electrónica")
            self.docventa.n_boleta.setText("BOL-"+Data[2])
        else:
            if Data[8] == "Factura":
                self.docventa.bol_fact.setText("Factura de Venta Electrónica")
                self.docventa.n_boleta.setText("FAC-"+Data[2])
        
        
        
        
        
        