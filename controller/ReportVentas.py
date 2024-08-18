from PyQt5 import uic
from controller import MenuPrincipal
from dao import UsuarioDao, VentaDao, DetalleVentaDao

class ReportVentasFRM:
    
    def __init__(self):
        self.reportVent = uic.loadUi("view/FRM_REPORT_VENTA.ui")
        self.reportVent.setWindowTitle("Reporte de Ventas")
        self.reportVent.widget_2.hide()
        
        self.ConexionUser = UsuarioDao.UsuarioBD()
        self.ConexionVenta = VentaDao.VentaBD()
        self.ConexionDetalleVenta = DetalleVentaDao.DetalleVentaBD()
        self.DataUser = self.ConexionUser.AllDataNombreDeUsuarios(2)
        self.reportVent.cb_filtro.addItems(self.DataUser)
        self.reportVent.cb_filtro.setCurrentText("Seleccione")
        
        #Botones Widget 1
        self.reportVent.btCancelar.clicked.connect(self.BtCancelarWd1)
        self.reportVent.btGenerar.clicked.connect(self.BtGenerarWd1)
        
        #Boton Wdiget 2
        self.reportVent.bTretorno.clicked.connect(self.BtRetorno)
        
        self.reportVent.show()
        
    def HideWidgets(self):
        self.reportVent.widget_1.hide()
        self.reportVent.widget_2.hide()
        
    def ShowWidget(self, prmtro):
        if prmtro == self.reportVent.widget_1:
            if self.reportVent.widget_1.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
        else:
            if prmtro == self.reportVent.widget_2:
                if self.reportVent.widget_2.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
    
    def BtCancelarWd1(self):
        self.reportVent.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def BtRetorno(self):
        self.BtCancelarWd1()
        
    def BtGenerarWd1(self):
        ProductTotalesVendidos = 0
        DineroRecaudado = 0
        qdate1 = self.reportVent.desde_de.date()
        DateDesde = qdate1.toString("yyyy-MM-dd")
        qdate2 = self.reportVent.hasta_de.date()
        DateHasta = qdate2.toString("yyyy-MM-dd")
        Agente = self.reportVent.cb_filtro.currentText()
        
        if self.Comprobador(Agente) is True:
            idUsuario = self.ConexionUser.UbicadorDeUsuarioXNombreYApellido(Agente, 2)
            VentasTotalesLst = self.ConexionVenta.ConsultaTablaVentasxUser(DateDesde, DateHasta, idUsuario)
            
            ProductTotalesLst = self.ConexionDetalleVenta.ObtenerCantidadProdVendXUserandFecha(DateDesde, DateHasta, idUsuario)
            for i in range(len(ProductTotalesLst)):
                ProductTotalesVendidos += int(ProductTotalesLst[i])
                
            DineroRecaudadoLst = self.ConexionDetalleVenta.ObtenerTotalDineroObtenido(DateDesde, DateHasta, idUsuario)
            for k in range(len(DineroRecaudadoLst)):
                DineroRecaudado += float(DineroRecaudadoLst[k])
                
            VentasT = str(len(VentasTotalesLst))
            ProductTotalesVendidos = str(ProductTotalesVendidos)
            DineroRecaudado = str(round(DineroRecaudado, 2))
            
            self.AplicacionReporte(VentasT, ProductTotalesVendidos, DineroRecaudado)
            #print(Agente)
            #print(idUsuario)
            #print(len(VentasTotales))
            #print(ProductTotalesVendidos)
            #print(DineroRecaudado)
            #print(DateDesde)
            #print(DateHasta)
            self.ShowWidget(self.reportVent.widget_2)
        else:
            if self.Comprobador(Agente) is False:
                self.reportVent.warning.setText("¡Ingrese un usuario válido!")
        
    def AplicacionReporte(self, VentasT, NproductosVendidos, DineroRecaudado):
        self.reportVent.warning.setText("")
        self.reportVent.ventasT_le.setText(VentasT)
        self.reportVent.prodT_le.setText(NproductosVendidos)
        self.reportVent.dineroT_le.setText("S/ " + DineroRecaudado)

        
    def Comprobador(self, usuario):
        if usuario not in self.DataUser:
            return False
        else:
            return True
        