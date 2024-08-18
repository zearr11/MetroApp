from PyQt5 import uic
from controller import MenuPrincipal
from dao import GuiaEntradaDao, ReporteSalidaDao
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt

class GenInventarioFRM:
    
    def __init__(self):
        self.genInv = uic.loadUi("view/FRM_GEN_INVENTARIO.ui")
        self.genInv.setWindowTitle("Generar el Inventario")
        
        #ConexionesDao
        self.ConexionGuiaEntradaDao = GuiaEntradaDao.GuiaEntradaBD()
        self.ConexionReporteDeSalidaDao = ReporteSalidaDao.ReporteSalidaBD()
        
        #Ocultado Inicial de Widget 2
        self.genInv.widget_2.hide()
        
        #Botones Widget 1
        self.genInv.btCancelar.clicked.connect(self.BtCancelarFRM1)
        self.genInv.btGenerar.clicked.connect(self.BtGenerarFRM1)
        
        #Boton Widget 2
        self.genInv.bTretorno.clicked.connect(self.BtRetornoMenu)
        
        self.genInv.show()
    
    #########################
    #Programacion Bt Widget 1
    
    def BtCancelarFRM1(self):
        self.genInv.close()
        self.menu = MenuPrincipal.MenuFRM()
    
    def BtGenerarFRM1(self):
        qdate1 = self.genInv.desde_de.date()
        DateDesde = qdate1.toString("yyyy-MM-dd")
        qdate2 = self.genInv.hasta_de.date()
        DateHasta = qdate2.toString("yyyy-MM-dd")
        self.LlenadoTablaEntrada(DateDesde, DateHasta)
        self.LlenadoTablaSalida(DateDesde, DateHasta)
        self.genInv.widget_1.hide()
        self.genInv.widget_2.show()
        
    def LlenadoTablaEntrada(self, DateDesde, DateHasta):
        TbEntrada = self.ConexionGuiaEntradaDao.ConsultaTablaEntradaProductos(DateDesde, DateHasta)
        Cantidad = len(TbEntrada)
        self.genInv.tw_entrada.verticalHeader().setVisible(False)
        self.genInv.tw_entrada.setRowCount(Cantidad)
        Fila = 0
        for obj in TbEntrada:
            self.genInv.tw_entrada.setItem(Fila, 0, QTableWidgetItem(str(obj[0])))
            self.genInv.tw_entrada.setItem(Fila, 1, QTableWidgetItem(str(obj[1])))
            self.genInv.tw_entrada.setItem(Fila, 2, QTableWidgetItem(obj[2]))
            self.genInv.tw_entrada.setItem(Fila, 3, QTableWidgetItem(obj[3]))
            self.genInv.tw_entrada.setItem(Fila, 4, QTableWidgetItem(obj[4]))
            self.genInv.tw_entrada.setItem(Fila, 5, QTableWidgetItem(str(obj[5])))
            Fila +=1
            
        for row in range(self.genInv.tw_entrada.rowCount()):
            for column in range(self.genInv.tw_entrada.columnCount()):
                item = self.genInv.tw_entrada.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
        
        self.genInv.tw_entrada.resizeColumnsToContents()
        self.genInv.tw_entrada.setEditTriggers(QTableWidget.NoEditTriggers)
        
        if len(TbEntrada) == 0:
            self.genInv.tw_entrada.hide()
        else:
            pass
        
    def LlenadoTablaSalida(self, DateDesde, DateHasta):
        TbSalida = self.ConexionReporteDeSalidaDao.ConsultaTablaSalidaProductos(DateDesde, DateHasta)
        Cantidad = len(TbSalida)
        self.genInv.tw_salida.verticalHeader().setVisible(False)
        
        self.genInv.tw_salida.setRowCount(Cantidad)
        Fila = 0
        for obj in TbSalida:
            self.genInv.tw_salida.setItem(Fila, 0, QTableWidgetItem(str(obj[0])))
            self.genInv.tw_salida.setItem(Fila, 1, QTableWidgetItem(str(obj[1])))
            self.genInv.tw_salida.setItem(Fila, 2, QTableWidgetItem(obj[2]))
            self.genInv.tw_salida.setItem(Fila, 3, QTableWidgetItem(obj[3]))
            self.genInv.tw_salida.setItem(Fila, 4, QTableWidgetItem(str(obj[4])))
            Fila +=1
            
        for row in range(self.genInv.tw_salida.rowCount()):
            for column in range(self.genInv.tw_salida.columnCount()):
                item = self.genInv.tw_salida.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
        
        self.genInv.tw_salida.resizeColumnsToContents()
        self.genInv.tw_salida.setEditTriggers(QTableWidget.NoEditTriggers)
        
        if len(TbSalida) == 0:
            self.genInv.tw_salida.hide()
        else:
            pass


    #########################
    #Programacion Bt Widget 2
    
    def BtRetornoMenu(self):
        self.BtCancelarFRM1()