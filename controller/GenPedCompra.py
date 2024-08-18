from PyQt5 import uic
from controller import MenuPrincipal, DocVentaBolFact
from dao import ProveedorDao, ProductoDao, LoginDao, DocumentoDeVentaDao, CompraDao, DetalleCompraDao
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView
from PyQt5.QtCore import Qt
from datetime import datetime


class GenPedCompraFRM:
    
    def __init__(self):
        self.newPedCompr = uic.loadUi("view/FRM_GEN_PED_COMPR.ui")
        self.newPedCompr.setWindowTitle("Generar Pedido de Compra")
        self.ListaProdSolicitados = []
        
        #Asignacion de Conexiones BD
        self.ConnectProveedorDao = ProveedorDao.ProveedorBD()
        self.ConnectProductoDao = ProductoDao.ProductoBD()
        
        #Botones Superficiales
        self.newPedCompr.bt_cancelar_pedcompr.clicked.connect(self.CancelarPedCompr)
        self.newPedCompr.bt_nuevo_vent.clicked.connect(self.btNuevo)
        self.newPedCompr.bt_listar_vent.clicked.connect(self.btListar)
        
        #Boton Agregar
        self.newPedCompr.bt_add_pr_ped.clicked.connect(self.AgregadoProdInTab)
        #Boton LimpiarRegistro
        self.newPedCompr.bt_clear_ped.clicked.connect(self.btLimpiarReg)
        #Boton GuardarReg
        self.newPedCompr.bt_guardar_ped.clicked.connect(self.GuardarPedidoCompra)
        
        #ClickEnTabla
        self.newPedCompr.tw_PED_COMPR.cellClicked.connect(self.ClickTblCompras)
        
        #Inicio de FRM
        self.ShowWidget(self.newPedCompr.window_1_compr)
        self.newPedCompr.show()
         
    
    #######################################
    #Botones Superficiales
      
    def CancelarPedCompr(self):
        self.newPedCompr.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def btNuevo(self):
        self.ShowWidget(self.newPedCompr.window_1_compr)
        
    def btListar(self):
        self.ShowWidget(self.newPedCompr.window_2_lst)
        
        
    #######################################
    #Funciones de Inicio
    
    def HideWidgets(self):
        self.newPedCompr.window_1_compr.hide()
        self.newPedCompr.window_2_lst.hide()   

    def ShowWidget(self, prmtro):
        if prmtro == self.newPedCompr.window_1_compr:
            if self.newPedCompr.window_1_compr.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
                self.GenPedidoFunciones()
            
        else:
            if prmtro == self.newPedCompr.window_2_lst:
                if self.newPedCompr.window_2_lst.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
                    self.ListarPedidos()
                    if len(self.ListaProdSolicitados) == 0:
                        pass
                    else:
                        self.btLimpiarReg()
                        
                    
    def GenPedidoFunciones(self):
        #Creacion de Listas para Guardado Temporal de Datos
        self.ObjProductoID = []
        self.ObjCantidadProd = []
        self.ObjPrecioTxProd = []
        self.TotalTCompra = 0
        
        #Limpieza de Items
        self.newPedCompr.cb_proveedor.clear()
        self.newPedCompr.cb_product_ped.clear()
        
        #Agregado de Items
        self.DataProveedores = self.ConnectProveedorDao.DataAllProveedor()
        self.DataProductos = self.ConnectProductoDao.DataAllProducto()
        self.newPedCompr.cb_proveedor.addItems(self.DataProveedores)
        self.newPedCompr.cb_product_ped.addItems(self.DataProductos)
        
        #Por defecto los campos estan vacios
        self.newPedCompr.cb_proveedor.setCurrentText("")
        self.newPedCompr.cb_product_ped.setCurrentText("")
        
    def ListarPedidos(self):
        self.LlenadoTablaCompras()
    
    #######################################
    #SISTEMA DE REGISTRO DE COMPRA
    
    def AgregadoProdInTab(self):
        self.newPedCompr.warning_ped.setText("")
        #Asignacion de variables a los botones
        self.Proveedor = self.newPedCompr.cb_proveedor.currentText()
        self.Producto = self.newPedCompr.cb_product_ped.currentText()
        self.Cantidad = self.newPedCompr.le_cant_ped.text()
        
        if self.Proveedor == "" or self.Proveedor not in self.DataProveedores:
            self.newPedCompr.warning_ped.setText("¡Selecciona un Proveedor de la Lista!")
        else:
            if self.Producto == "" or self.Producto not in self.DataProductos:
                self.newPedCompr.warning_ped.setText("¡Selecciona el Producto que solicitas de la Lista!")
            else:
                try:
                    int(self.Cantidad)
                except:
                    self.newPedCompr.warning_ped.setText("¡Ingresa la cantidad!")
                else:
                    self.IngresoInfoProv()
                    
                    ProdSelect = self.ConnectProductoDao.ObtenerProducto2(self.Producto)
                    self.TotalXProducto = round((float(float(ProdSelect[4]) * float(self.Cantidad))),2)
                    
                    self.newPedCompr.tw_showPed.verticalHeader().setVisible(False)
                    Fila = self.newPedCompr.tw_showPed.rowCount()
                    self.newPedCompr.tw_showPed.insertRow(Fila)
                    
                    self.newPedCompr.tw_showPed.setItem(Fila, 0, QTableWidgetItem(str(ProdSelect[0])))
                    self.newPedCompr.tw_showPed.setItem(Fila, 1, QTableWidgetItem(ProdSelect[1]+" "+ProdSelect[2]))
                    self.newPedCompr.tw_showPed.setItem(Fila, 2, QTableWidgetItem(ProdSelect[3]))
                    self.newPedCompr.tw_showPed.setItem(Fila, 3, QTableWidgetItem(("S/ ")+str(ProdSelect[4])))
                    self.newPedCompr.tw_showPed.setItem(Fila, 4, QTableWidgetItem(self.Cantidad))
                    self.newPedCompr.tw_showPed.setItem(Fila, 5, QTableWidgetItem(("S/ ")+str(self.TotalXProducto)))
                    
                    for row in range(self.newPedCompr.tw_showPed.rowCount()):
                        for column in range(self.newPedCompr.tw_showPed.columnCount()):
                            item = self.newPedCompr.tw_showPed.item(row, column)
                            if item:
                                item.setTextAlignment(Qt.AlignCenter)
                                
                    Temp = []
                    Temp.append(ProdSelect[0])#Id del Producto Ingresado
                    Temp.append(int(self.Cantidad))#Cantidad Unitaria
                    Temp.append(self.TotalXProducto)#Precio * Cantidad
                    self.ListaProdSolicitados.append(Temp)

                    #self.newPedCompr.tw_showPed.resizeColumnsToContents()
                    self.newPedCompr.tw_showPed.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.newPedCompr.tw_showPed.setEditTriggers(QTableWidget.NoEditTriggers)
                    self.ClearAndBloquingAfterAdd()
                    self.newPedCompr.warning_ped.setText("")
                    
    #Metodo Complementario               
    def IngresoInfoProv(self):
        if len(self.ListaProdSolicitados) > 0:
            pass
        else:
            self.DataCompra = self.Proveedor
    
    #Metodo Complementario         
    def ClearAndBloquingAfterAdd(self):
        if len(self.ListaProdSolicitados) == 1:
            self.newPedCompr.cb_proveedor.setEnabled(False)
            self.newPedCompr.cb_product_ped.setCurrentText("")
            self.newPedCompr.le_cant_ped.setText("")
            self.newPedCompr.warning_ped.setText("")
        else:
            self.newPedCompr.cb_product_ped.setCurrentText("")
            self.newPedCompr.le_cant_ped.setText("")
            self.newPedCompr.warning_ped.setText("")
    
    #Boton Limpiar    
    def btLimpiarReg(self):
        if len(self.ListaProdSolicitados) == 0:
            self.newPedCompr.cb_proveedor.setCurrentText("")
            self.newPedCompr.cb_product_ped.setCurrentText("")
            self.newPedCompr.le_cant_ped.setText("")
            self.newPedCompr.warning_ped.setText("")
        else:
            if len(self.ListaProdSolicitados) > 0:
                self.ListaProdSolicitados.clear()
                self.newPedCompr.tw_showPed.setRowCount(0)
                self.newPedCompr.cb_proveedor.setEnabled(True)
                self.newPedCompr.cb_proveedor.setCurrentText("")
                self.newPedCompr.cb_product_ped.setCurrentText("")
                self.newPedCompr.le_cant_ped.setText("")
                self.newPedCompr.warning_ped.setText("")
                
    def GuardarPedidoCompra(self):
        if len(self.ListaProdSolicitados) == 0:
            self.newPedCompr.warning_ped.setText("¡Para registrar el pedido debes agregar productos!")
        else:
            self.OrdenadorDeValoresPedido()
            
    def OrdenadorDeValoresPedido(self):
        for i in range(len(self.ListaProdSolicitados)):
            compr = self.ListaProdSolicitados[i]
            self.ObjProductoID.append(compr[0])
            self.ObjCantidadProd.append(compr[1])
            self.ObjPrecioTxProd.append(compr[2])
            self.TotalTCompra += compr[2]
        
        self.IGV = self.TotalTCompra*0.18
        self.SubTotal = self.TotalTCompra - self.IGV
        self.FinalizadorRegPedido()
        
    def FinalizadorRegPedido(self):
        #self.DataCompra (Variable)
        #1 self.ObjProductoID
        #2 self.ObjCantidadProd
        #3 self.SubTotal
        #4 self.IGV
        #5 self.TotalTCompra
        
        ConnectLoginDao = LoginDao.LoginBD()
        ConnectDaoDocumentoCompra = DocumentoDeVentaDao.DocumentodeVentaCLASS()
        ConnectCompraDao = CompraDao.CompraBD()
        ConnectDetalleCompra = DetalleCompraDao.DetalleCompraBD()
        
        actual = datetime.now()
        FechaCompra= actual.date()
        Estate = "En curso"
        
        idUsuario = ConnectLoginDao.ObtenerUltimoUsuario()
        idProveedor = self.ConnectProveedorDao.ObtenerProveedorID2(self.DataCompra)
        ConnectDaoDocumentoCompra.InsertTablaDocumentodeVenta(self.SubTotal, self.IGV, self.TotalTCompra, 3)
        idDocumentoCompra = ConnectDaoDocumentoCompra.ObtenerUltimoDocumentoDeVentaID()

        ConnectCompraDao.InsertTablaCompra(FechaCompra, Estate, idUsuario, idDocumentoCompra, idProveedor)
        self.idCompra = ConnectCompraDao.ObtenerCompraID(FechaCompra, idUsuario, idDocumentoCompra, idProveedor)#

        for ins in range(len(self.ListaProdSolicitados)):
            ConnectDetalleCompra.InsertTablaDetalleCompra(self.ObjCantidadProd[ins], self.ObjPrecioTxProd[ins], self.ObjProductoID[ins], self.idCompra)
            
        self.MostrarFact()
        
    def MostrarFact(self):
        self.newPedCompr.close()
        self.docventa = DocVentaBolFact.DocVentaBolFactFRM(idCompr=self.idCompra)
        
    #######################################
    #SISTEMA DE LISTA DE COMPRAS
    
    def LlenadoTablaCompras(self):
        ConnectCompraDao = CompraDao.CompraBD()
        TbCompras = ConnectCompraDao.ConsultaTablaCompras()
        Cantidad = len(TbCompras)
        self.newPedCompr.tw_PED_COMPR.verticalHeader().setVisible(False)
        self.newPedCompr.tw_PED_COMPR.setRowCount(Cantidad)
        Fila = 0
        
        for obj in TbCompras:
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 0, QTableWidgetItem(str(obj[0])))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 1, QTableWidgetItem((obj[1]+" "+(obj[2]))))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 2, QTableWidgetItem(str(obj[3])))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 3, QTableWidgetItem("FAC-"+obj[4]))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 4, QTableWidgetItem(obj[5]))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 5, QTableWidgetItem(obj[6]))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 6, QTableWidgetItem("S/ "+str(obj[7])))
            self.newPedCompr.tw_PED_COMPR.setItem(Fila, 7, QTableWidgetItem(obj[8]))
            Fila +=1
            
        for row in range(self.newPedCompr.tw_PED_COMPR.rowCount()):
            for column in range(self.newPedCompr.tw_PED_COMPR.columnCount()):
                item = self.newPedCompr.tw_PED_COMPR.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
        
        self.newPedCompr.tw_PED_COMPR.resizeColumnsToContents()
        self.newPedCompr.tw_PED_COMPR.setEditTriggers(QTableWidget.NoEditTriggers)
        
    def ClickTblCompras(self, fila):
        idCompra = self.newPedCompr.tw_PED_COMPR.item(fila, 0).text()
        self.newPedCompr.close()
        self.docventa = DocVentaBolFact.DocVentaBolFactFRM(idCompr=idCompra)