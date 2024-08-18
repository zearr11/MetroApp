from PyQt5 import uic
from controller import MenuPrincipal
from dao import UsuarioDao, DetalleCompraDao, CompraDao

class ReportComprasFRM:
    
    def __init__(self):
        self.reportCompr = uic.loadUi("view/FRM_REPORT_COMPRAS.ui")
        self.reportCompr.setWindowTitle("Reporte de Compras")
        self.reportCompr.widget_2.hide()
        
        self.ConexionUser = UsuarioDao.UsuarioBD()
        self.ConexionCompras = CompraDao.CompraBD()
        self.ConexionDetalleCompras = DetalleCompraDao.DetalleCompraBD()
        self.DataUser = self.ConexionUser.AllDataNombreDeUsuarios(3)
        self.reportCompr.cb_filtro.addItems(self.DataUser)
        self.reportCompr.cb_filtro.setCurrentText("Seleccione")
        
        #Botones Widget 1
        self.reportCompr.btCancelar.clicked.connect(self.BtCancelarWd1)
        self.reportCompr.btGenerar.clicked.connect(self.BtGenerarWd1)
        
        #Boton Widget 2
        self.reportCompr.bTretorno.clicked.connect(self.BtRetorno)
        
        self.reportCompr.show()
        
    def HideWidgets(self):
        self.reportCompr.widget_1.hide()
        self.reportCompr.widget_2.hide()
        
    def ShowWidget(self, prmtro):
        if prmtro == self.reportCompr.widget_1:
            if self.reportCompr.widget_1.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
        else:
            if prmtro == self.reportCompr.widget_2:
                if self.reportCompr.widget_2.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
    
    def BtCancelarWd1(self):
        self.reportCompr.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def BtRetorno(self):
        self.BtCancelarWd1()
        
    def BtGenerarWd1(self):
        ProductTotalesComprados = 0
        DineroGastado = 0
        qdate1 = self.reportCompr.desde_de.date()
        DateDesde = qdate1.toString("yyyy-MM-dd")
        qdate2 = self.reportCompr.hasta_de.date()
        DateHasta = qdate2.toString("yyyy-MM-dd")
        Agente = self.reportCompr.cb_filtro.currentText()
        
        if self.Comprobador(Agente) is True:
            #
            idUsuario = self.ConexionUser.UbicadorDeUsuarioXNombreYApellido(Agente, 3)
            ComprasTotalesLst = self.ConexionCompras.ConsultaTablaComprasxUser(DateDesde, DateHasta, idUsuario)
            
            ProductTotalesLst = self.ConexionDetalleCompras.ObtenerCantidadProdComprXUserandFecha(DateDesde, DateHasta, idUsuario)#
            for i in range(len(ProductTotalesLst)):#
                ProductTotalesComprados += int(ProductTotalesLst[i])#
                
            DineroRecaudadoLst = self.ConexionDetalleCompras.ObtenerTotalDineroGastado(DateDesde, DateHasta, idUsuario)#
            for k in range(len(DineroRecaudadoLst)):#
                DineroGastado += float(DineroRecaudadoLst[k])#
                
            ComprasT = str(len(ComprasTotalesLst))
            ProductTotalesComprados = str(ProductTotalesComprados)
            DineroGastado = str(round(DineroGastado, 2))
            
            self.AplicacionReporte(ComprasT, ProductTotalesComprados, DineroGastado)
            #
            #print(Agente)
            #print(idUsuario)
            #print(len(VentasTotales))
            #print(ProductTotalesVendidos)
            #print(DineroRecaudado)
            #print(DateDesde)
            #print(DateHasta)
            self.ShowWidget(self.reportCompr.widget_2)
        else:
            if self.Comprobador(Agente) is False:
                self.reportCompr.warning.setText("¡Ingrese un usuario válido!")
        
    def AplicacionReporte(self, ComprasT, NproductosComprados, DineroGastado):
        self.reportCompr.warning.setText("")
        self.reportCompr.comprasT_le.setText(ComprasT)
        self.reportCompr.prodT_le.setText(NproductosComprados)
        self.reportCompr.dineroT_le.setText("S/ " + DineroGastado)

        
    def Comprobador(self, usuario):
        if usuario not in self.DataUser:
            return False
        else:
            return True