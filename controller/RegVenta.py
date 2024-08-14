from PyQt5 import uic
from controller import MenuPrincipal, DocVentaBolFact
from dao import ClienteDao, MedioPagoDao, ProductoDao, TipoDocVentaDao, NumeroDocumentoDao, DocumentoDeVentaDao, LoginDao, VentaDao, DetalleVentaDao
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt
from datetime import datetime

class RegVentaFRM:
    
    def __init__(self):
        self.newVenta = uic.loadUi("view/FRM_REG_VENTA.ui")
        self.newVenta.setWindowTitle("Gestion de Ventas")
        self.ListaProductosAdquiridos = []
        self.ObjProductoID = []
        self.ObjCantidadProd = []
        self.ObjPrecioTxProd = []
        self.TotalT = 0

        #
        self.ConnectNumeroDocumentoClientes = ClienteDao.ClienteBD()
        self.ConnectMedioPago = MedioPagoDao.MedioPagoBD()
        self.ConnectTipoDocVenta = TipoDocVentaDao.TipoDocVentaBD()##############
        self.ConnectProducto = ProductoDao.ProductoBD()
        
        DtNumeroDocumento = self.ConnectNumeroDocumentoClientes.ObtenerNumeroDocumentoCliente()
        DtMedioPago = self.ConnectMedioPago.DataMedioPago()
        DtProducto = self.ConnectProducto.DataProducto()
        DtDocVenta = self.ConnectTipoDocVenta.DataTipoDocVenta()###############
        
        self.newVenta.cb_tipoDNI_vent.addItems(DtNumeroDocumento)
        self.newVenta.cb_medioP_vent.addItems(DtMedioPago)
        self.newVenta.cb_product_vent.addItems(DtProducto)
        self.newVenta.cb_tipodoc_vent.addItems(DtDocVenta)######################
        self.newVenta.cb_tipoDNI_vent.setCurrentText("")
        self.newVenta.cb_product_vent.setCurrentText("")
        #
        self.newVenta.tw_venta.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#OCUPACION DE TABLA COMPLETA
        
        self.newVenta.bt_cancelar_vent.clicked.connect(self.CancelarProduct)
        self.newVenta.bt_add_prod_vent.clicked.connect(self.AgregarProducto)
        self.newVenta.bt_clear_reg_vent.clicked.connect(self.LimpiarRegistro)
        self.newVenta.bt_guardar_vent.clicked.connect(self.GuardadoVenta)
        self.newVenta.show()
        
    #########################################################################################################
    #BOTONES PRINCIPALES  
    def CancelarProduct(self):
        self.newVenta.close()
        self.menu = MenuPrincipal.MenuFRM()
        
        
    def LimpiarRegistro(self):
        if len(self.ListaProductosAdquiridos) == 0:
            self.newVenta.cb_tipoDNI_vent.setCurrentText("")
            self.newVenta.cb_medioP_vent.setCurrentText("Seleccione")
            self.newVenta.cb_product_vent.setCurrentText("")
            self.newVenta.le_cant_vent.setText("")
        else:
            if len(self.ListaProductosAdquiridos) > 0:
                self.newVenta.tw_venta.setRowCount(0)
                self.newVenta.cb_tipoDNI_vent.setEnabled(True)
                self.newVenta.cb_medioP_vent.setEnabled(True)
                self.newVenta.cb_tipodoc_vent.setEnabled(True)
                self.newVenta.cb_tipoDNI_vent.setCurrentText("")
                self.newVenta.cb_medioP_vent.setCurrentText("Seleccione")
                self.newVenta.cb_tipodoc_vent.setCurrentText("Seleccione")
                self.newVenta.cb_product_vent.setCurrentText("")
                self.newVenta.le_cant_vent.setText("")
                self.DatosVenta.clear()
                self.ListaProductosAdquiridos.clear()   
    
    
    def GuardadoVenta(self):   
        from controller import DocVentaBolFact
        if len(self.ListaProductosAdquiridos) == 0:
            self.newVenta.warning_regvent.setText("¡Para registrar la venta debes agregar productos!")
        else:
            self.AsignacionValoresAListaProductos()
        
    def AgregarProducto(self):
        self.SeleccionadorDNI = self.newVenta.cb_tipoDNI_vent.currentText()
        self.MedPago = self.newVenta.cb_medioP_vent.currentText()
        self.ProductSelect = self.newVenta.cb_product_vent.currentText()
        self.CantidadProduct = self.newVenta.le_cant_vent.text()
        self.TipoDocVenta = self.newVenta.cb_tipodoc_vent.currentText()#######
        
        if self.SeleccionadorDNI == "":
            self.newVenta.warning_regvent.setText("¡Indique el documento del cliente!")
        else:
            if self.MedPago == "Seleccione":
                self.newVenta.warning_regvent.setText("¡Indique el medio de pago!")
            else:
                if self.TipoDocVenta == "Seleccione":
                        self.newVenta.warning_regvent.setText("¡Indique el tipo de documento de venta!")
                else:
                    if self.ProductSelect == "":
                            self.newVenta.warning_regvent.setText("¡Indique el nombre del producto que desea agregar!")
                    else:
                        try:
                            int(self.CantidadProduct)
                        except:
                            self.newVenta.warning_regvent.setText("¡Ingrese un valor numérico en el campo 'Cantidad'!")
                        else:
                            self.AgregadoAdicional()
                            Lst1 = self.ConnectProducto.ObtenerProducto2(self.ProductSelect)
                            self.TotalxProduct = round((float(float(Lst1[4]) * float(self.CantidadProduct))),2)
                            #
                            Fila = self.newVenta.tw_venta.rowCount()
                            self.newVenta.tw_venta.insertRow(Fila) 
                            #
                            self.newVenta.tw_venta.setItem(Fila, 0, QTableWidgetItem(str(Lst1[0])))
                            self.newVenta.tw_venta.setItem(Fila, 1, QTableWidgetItem(Lst1[1]))
                            self.newVenta.tw_venta.setItem(Fila, 2, QTableWidgetItem(Lst1[2]))
                            self.newVenta.tw_venta.setItem(Fila, 3, QTableWidgetItem(Lst1[3]))
                            self.newVenta.tw_venta.setItem(Fila, 4, QTableWidgetItem(("S/ ")+str(Lst1[4])))
                            self.newVenta.tw_venta.setItem(Fila, 5, QTableWidgetItem(self.CantidadProduct))
                            self.newVenta.tw_venta.setItem(Fila, 6, QTableWidgetItem(("S/ ")+str(self.TotalxProduct)))
            
                            for row in range(self.newVenta.tw_venta.rowCount()):
                                for column in range(self.newVenta.tw_venta.columnCount()):
                                    item = self.newVenta.tw_venta.item(row, column)
                                    if item:
                                        item.setTextAlignment(Qt.AlignCenter)
        
                            self.newVenta.tw_venta.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                            self.newVenta.tw_venta.setEditTriggers(QTableWidget.NoEditTriggers)
                            self.newVenta.warning_regvent.setText("")
                        
                            Almacenador = []
                            Almacenador.append(Lst1[0])#ID PRODUCTO
                            Almacenador.append(int(self.CantidadProduct))#CANTIDAD DE PRODUCTOS ADQUIRIDOS
                            Almacenador.append(self.TotalxProduct)#TOTAL UNITARIO = PRECIO PRODUCTO * CANTIDAD
                            self.ListaProductosAdquiridos.append(Almacenador)
                            self.ClearAndBloquing()
                            #print(self.ListaProductosAdquiridos)
                            #print(self.DatosVenta)
    #########################################################################################################
    
    #########################################################################################################
    #METODOS COMPLEMENTARIOS                    
    def AgregadoAdicional(self):
        if len(self.ListaProductosAdquiridos) > 0:
            pass
        else:
            self.DatosVenta = []
            self.DatosVenta.append(self.SeleccionadorDNI) #NUMERO DNI CLIENTE [0]
            self.DatosVenta.append(self.MedPago) #TIPO DE MEDIO DE PAGO [1]
            self.DatosVenta.append(self.TipoDocVenta)#TIPO DOCUMENTO VENTA [2]
    
    
    def ClearAndBloquing(self):
        if len(self.ListaProductosAdquiridos) == 1:
            self.newVenta.cb_tipodoc_vent.setEnabled(False)
            self.newVenta.cb_tipoDNI_vent.setEnabled(False)
            self.newVenta.cb_medioP_vent.setEnabled(False)
            self.newVenta.cb_product_vent.setCurrentText("")
            self.newVenta.le_cant_vent.setText("")
        else:
            self.newVenta.cb_product_vent.setCurrentText("")
            self.newVenta.le_cant_vent.setText("")
    #########################################################################################################
            
    #METODOS PARA OBTENCION DE DATOS:
    def AsignacionValoresAListaProductos(self):
        for i in range(len(self.ListaProductosAdquiridos)):
            compr = self.ListaProductosAdquiridos[i]
            self.ObjProductoID.append(compr[0])
            self.ObjCantidadProd.append(compr[1])
            self.ObjPrecioTxProd.append(compr[2])
            self.TotalT += compr[2]
        
        self.IGV = self.TotalT*0.18
        self.SubTotal = self.TotalT - self.IGV
        self.FinalizadorRegistroVenta()

        
    def FinalizadorRegistroVenta(self):
        NumeroDNIc = self.DatosVenta[0]
        TipoMedPagoC = self.DatosVenta[1]
        TipoDocVenta = self.DatosVenta[2]

        #1 self.ObjProductoID
        #2 self.ObjCantidadProd
        #3 self.SubTotal
        #4 self.IGV
        #5 self.TotalT        
        
        ConnectLoginUser = LoginDao.LoginBD()
        ConnectDaoNumeroDocumento = NumeroDocumentoDao.NumeroDocumentoBD()
        ConnectDaoDocumentoVenta = DocumentoDeVentaDao.DocumentodeVentaCLASS()
        ConnectDaoVenta = VentaDao.VentaBD()
        ConnectDaoDetalleVenta = DetalleVentaDao.DetalleVentaBD()
        
        #Fecha de Venta
        actual = datetime.now()
        FechaVenta = actual.date()
        
        idTipoDocVenta = self.ConnectTipoDocVenta.ObtenerTipoDocVentaID(TipoDocVenta)
        idMedPago = self.ConnectMedioPago.ObtenerMedioPagoID(TipoMedPagoC)
        idNumeroDocCliente = ConnectDaoNumeroDocumento.ObtenerNumeroDocumentoID2(NumeroDNIc)
        idUsuario = ConnectLoginUser.ObtenerUltimoUsuario()
        idCliente = self.ConnectNumeroDocumentoClientes.ObtenerClienteIDXdni(idNumeroDocCliente)
        
        #Insert en Tabla Documento de Venta
        ConnectDaoDocumentoVenta.InsertTablaDocumentodeVenta(self.SubTotal, self.IGV, self.TotalT, idTipoDocVenta)
        
        #Obtencion de ID de Documento de Venta
        idDocumentoVenta = ConnectDaoDocumentoVenta.ObtenerUltimoDocumentoDeVentaID()
        
        #Insert en Tabla Venta
        ConnectDaoVenta.InsertTablaVenta(FechaVenta, idMedPago, idUsuario, idCliente, idDocumentoVenta)
        idVenta = ConnectDaoVenta.ObtenerVentaID(FechaVenta, idMedPago, idUsuario, idCliente, idDocumentoVenta)
        
        #Insert en Tabla DetalleVenta
        for insertar in range(len(self.ListaProductosAdquiridos)):
            ConnectDaoDetalleVenta.InsertTablaDetalleVenta(self.ObjCantidadProd[insertar], self.ObjPrecioTxProd[insertar], self.ObjProductoID[insertar], idVenta)
    
        self.MostradoDocumento()
        
    def MostradoDocumento(self):
        self.newVenta.close()
        self.docventa = DocVentaBolFact.DocVentaBolFactFRM()