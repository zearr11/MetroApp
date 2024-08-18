from PyQt5 import uic
from controller import MenuPrincipal
from dao import ClienteDao, MedioPagoDao, ProductoDao, LoginDao, NumeroDocumentoDao, GuiaSalidaDao, ReporteSalidaDao
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView
from PyQt5.QtCore import Qt
from datetime import datetime

class GuiaSalidaFRM:
    
    def __init__(self):
        self.guiasal = uic.loadUi("view/FRM_GUIA_SALIDA.ui")
        self.guiasal.setWindowTitle("Guia de Salida")
        
        self.ConnectNumeroDocumentoClientes = ClienteDao.ClienteBD()
        self.ConnectMedioPago = MedioPagoDao.MedioPagoBD()
        self.ConnectProducto = ProductoDao.ProductoBD()
        
        self.DtNumeroDocumento = self.ConnectNumeroDocumentoClientes.ObtenerNumeroDocumentoCliente()
        self.DtMedioPago = self.ConnectMedioPago.DataMedioPago()
        self.DtProducto = self.ConnectProducto.DataProducto()
        
        #Botones Superiores
        self.guiasal.bt_cancelar.clicked.connect(self.BtCancelar)
        self.guiasal.bt_nuevo.clicked.connect(self.BtNuevo)
        self.guiasal.bt_listar.clicked.connect(self.BtListar)
        
        #Botones Reg Guia de Entrada
        self.guiasal.bt_addProd.clicked.connect(self.AgregarProduct)
        self.guiasal.bt_clear.clicked.connect(self.BtLimpiarReg)
        self.guiasal.bt_finalizar.clicked.connect(self.BtFinishReg)
        
        self.Showdiget(self.guiasal.window_1)
        self.guiasal.show()
        
        
    def HideWidgets(self):
        self.guiasal.window_1.hide()
        self.guiasal.window_2.hide()
        
        
    def Showdiget(self, prmtro):
        if prmtro == self.guiasal.window_1:
            if self.guiasal.window_1.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
                self.RegistroGuiaSalidaCargado()
                
        else:
            if prmtro == self.guiasal.window_2:
                if self.guiasal.window_2.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
                    self.ListarGuiasSalidaCargado()
                    
    def RegistroGuiaSalidaCargado(self):
        self.guiasal.cb_docC.clear()
        self.guiasal.cb_product.clear()
        self.guiasal.cb_medPag.clear()
        
        self.ListaProductosEnSalida = []
        self.ObjProductoID = []
        self.ObjCantidadProd = []
        self.ObjPrecioTxProd = []
        
        self.guiasal.cb_docC.addItems(self.DtNumeroDocumento)
        self.guiasal.cb_product.addItems(self.DtProducto)
        self.guiasal.cb_medPag.addItems(self.DtMedioPago)
        
        self.guiasal.cb_docC.setCurrentText("")
        self.guiasal.cb_product.setCurrentText("")
        
    def ListarGuiasSalidaCargado(self):
        self.ListarGuiasSalida()
        
    ################################################################################
    # Funcion de Botones Superiores
    
    def BtCancelar(self):
        self.guiasal.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def BtNuevo(self):
        self.HideWidgets()
        self.Showdiget(self.guiasal.window_1)
        
    def BtListar(self):
        self.HideWidgets()
        self.Showdiget(self.guiasal.window_2)
            
    
    ################################################################################
    # Inicio de Registro de Guia de Entrada 
    
    ### Metodos Complementarios: ###
    
    def ComprobadorCantidad(self):
        CxP = self.ConnectProducto.ObtenerCantidadProd(self.IDprodTemp)
        if int(self.CantidadProduct) > int(CxP):
            return False
        else:
            return True
    
    def AgregarProduct(self):
        self.SeleccionadorDNI = self.guiasal.cb_docC.currentText()
        self.MedPago = self.guiasal.cb_medPag.currentText()
        self.ProductSelect = self.guiasal.cb_product.currentText()
        self.CantidadProduct = self.guiasal.le_cantP.text()
        
        if self.SeleccionadorDNI == "" or self.SeleccionadorDNI not in self.DtNumeroDocumento:
            self.guiasal.warning_1.setText("¡Indique el documento del cliente!")
        else:
            if self.MedPago == "Seleccione":
                self.guiasal.warning_1.setText("¡Indique el medio de pago!")
            else:
                if self.ProductSelect == "" or self.ProductSelect not in self.DtProducto:
                        self.guiasal.warning_1.setText("¡Indique el nombre del producto que desea agregar!")
                else:
                    try:
                        int(self.CantidadProduct)
                    except:
                        self.guiasal.warning_1.setText("¡Ingrese un valor numérico en el campo 'Cantidad'!")
                    else:
                        Lst1 = self.ConnectProducto.ObtenerProducto2(self.ProductSelect)
                        self.IDprodTemp = Lst1[0]
                        if self.ComprobadorCantidad() is True:
                            self.AgregadoAdicional()
                            self.EnvioInfo()
                            
                            self.TotalxProduct = round((float(float(Lst1[4]) * float(self.CantidadProduct))),2)
                            #
                            Fila = self.guiasal.tw_data.rowCount()
                            self.guiasal.tw_data.insertRow(Fila) 
                            #
                            self.guiasal.tw_data.setItem(Fila, 0, QTableWidgetItem(str(Lst1[0])))
                            self.guiasal.tw_data.setItem(Fila, 1, QTableWidgetItem(Lst1[1]))
                            self.guiasal.tw_data.setItem(Fila, 2, QTableWidgetItem(Lst1[2]))
                            self.guiasal.tw_data.setItem(Fila, 3, QTableWidgetItem(Lst1[3]))
                            self.guiasal.tw_data.setItem(Fila, 4, QTableWidgetItem(("S/ ")+str(Lst1[4])))
                            self.guiasal.tw_data.setItem(Fila, 5, QTableWidgetItem(self.CantidadProduct))
                            self.guiasal.tw_data.setItem(Fila, 6, QTableWidgetItem(("S/ ")+str(self.TotalxProduct)))
                
                            for row in range(self.guiasal.tw_data.rowCount()):
                                for column in range(self.guiasal.tw_data.columnCount()):
                                    item = self.guiasal.tw_data.item(row, column)
                                    if item:
                                        item.setTextAlignment(Qt.AlignCenter)
            
                            self.guiasal.tw_data.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                            self.guiasal.tw_data.setEditTriggers(QTableWidget.NoEditTriggers)
                            self.guiasal.warning_1.setText("")
                            
                            Almacenador = []
                            Almacenador.append(Lst1[0])#ID PRODUCTO
                            Almacenador.append(int(self.CantidadProduct))#CANTIDAD DE PRODUCTOS EN SALIDA
                            Almacenador.append(self.TotalxProduct)#TOTAL UNITARIO = PRECIO PRODUCTO * CANTIDAD
                            self.ListaProductosEnSalida.append(Almacenador)
                            
                            #Nueva Propiedad
                            index = self.guiasal.cb_product.findText(self.ProductSelect)
                            if index != -1:
                                self.guiasal.cb_product.removeItem(index)
        
                            self.ClearAndBloq()   
                        else:
                            if self.ComprobadorCantidad() is False:
                                self.guiasal.warning_1.setText("Sin existencias suficientes, cambie cantidad") 
                     
    def AgregadoAdicional(self):
        if len(self.ListaProductosEnSalida) > 0:
            pass
        else:
            self.DatosInfo = []
            self.DatosInfo.append(self.SeleccionadorDNI) #NUMERO DNI CLIENTE [0]
            self.DatosInfo.append(self.MedPago) #TIPO DE MEDIO DE PAGO [1]
            
    def ClearAndBloq(self):
        if len(self.ListaProductosEnSalida) == 1:
            self.guiasal.cb_docC.setEnabled(False)
            self.guiasal.cb_medPag.setEnabled(False)
            self.guiasal.cb_product.setCurrentText("")
            self.guiasal.le_cantP.setText("")
        else:
            self.guiasal.cb_product.setCurrentText("")
            self.guiasal.le_cantP.setText("")
                
    def EnvioInfo(self):
        if len(self.ListaProductosEnSalida) == 0:
            self.DataEnvio = self.ConnectNumeroDocumentoClientes.ObtenerClienteXdni(self.SeleccionadorDNI)
            self.guiasal.le_direccion.setText(str(self.DataEnvio[0]))
            self.guiasal.le_telf.setText(str(self.DataEnvio[1]))
            self.guiasal.le_nameC.setText(str(self.DataEnvio[2]))
        else:
            pass
    
    ################################
    
    # Botones de Reg Guia de Entrada
    
    def BtLimpiarReg(self):
        if len(self.ListaProductosEnSalida) == 0:
            self.guiasal.cb_medPag.setCurrentText("Seleccione")
            self.guiasal.cb_product.setCurrentText("")
            self.guiasal.le_cantP.setText("")
        else:
            if len(self.ListaProductosEnSalida) > 0:
                self.guiasal.cb_product.clear()
                self.guiasal.cb_product.addItems(self.DtProducto)
                
                self.guiasal.tw_data.setRowCount(0)
                self.guiasal.cb_docC.setEnabled(True)
                self.guiasal.cb_medPag.setEnabled(True)
                self.guiasal.cb_docC.setCurrentText("")
                self.guiasal.cb_medPag.setCurrentText("Seleccione")
                self.guiasal.cb_product.setCurrentText("")
                self.guiasal.le_cantP.setText("")
                self.DatosInfo.clear()
                self.ListaProductosEnSalida.clear()
                
    def BtFinishReg(self):
        if len(self.ListaProductosEnSalida) == 0:
            self.guiasal.warning_1.setText("¡Para finalizar el registro, primero debes agregar productos!")
        else:
            self.OrdenadorDeVariables()
        
    def OrdenadorDeVariables(self):
        for k in range(len(self.ListaProductosEnSalida)):
            sali = self.ListaProductosEnSalida[k]
            self.ObjProductoID.append(sali[0])
            self.ObjCantidadProd.append(sali[1])
            self.ObjPrecioTxProd.append(sali[2])
            
        self.FinalizadorRegistroGuiaSalida()
            
    def FinalizadorRegistroGuiaSalida(self):
        NumeroDNIc = self.DatosInfo[0]
        TipoMedPagoC = self.DatosInfo[1]

        #self.ObjProductoID 
        #self.ObjCantidadProd
        #self.ObjPrecioTxProd
        
        actual = datetime.now()
        FechaGS = actual.date()
        
        ConexionConLog = LoginDao.LoginBD()
        ConnectDaoNumeroDocumento = NumeroDocumentoDao.NumeroDocumentoBD()
        ConnectGuiaSalidaDao = GuiaSalidaDao.GuiaSalidaBD()
        ConnectReportSalida = ReporteSalidaDao.ReporteSalidaBD()
        
        idNumeroDocCliente = ConnectDaoNumeroDocumento.ObtenerNumeroDocumentoID2(NumeroDNIc)
        idCliente = self.ConnectNumeroDocumentoClientes.ObtenerClienteIDXdni(idNumeroDocCliente)
        idUsuario = ConexionConLog.ObtenerUltimoUsuario()
        idMedPago = self.ConnectMedioPago.ObtenerMedioPagoID(TipoMedPagoC)
        
        #Insert en Tabla GuiaSalida
        ConnectGuiaSalidaDao.InsertTablaGuiaSalida(FechaGS, idMedPago, idUsuario, idCliente)
        idGuiaSalidA = ConnectGuiaSalidaDao.ObtenerUltimaGuiaSalidaID()
        
        #Insert en Tabla Reporte Salida
        for x in range(len(self.ListaProductosEnSalida)):
            ConnectReportSalida.InsertTablaReporteSalida(idGuiaSalidA, self.ObjProductoID[x], self.ObjCantidadProd[x], self.ObjPrecioTxProd[x])
        
        self.Descontador()
        self.BloqueoFinal()
        
            
    def BloqueoFinal(self):
        self.guiasal.cb_docC.setEnabled(False)
        self.guiasal.cb_medPag.setEnabled(False)
        self.guiasal.cb_product.setEnabled(False)
        self.guiasal.le_cantP.setEnabled(False)
        self.guiasal.bt_clear.setEnabled(False)
        self.guiasal.bt_finalizar.setEnabled(False)
        self.guiasal.bt_addProd.setEnabled(False)
        self.guiasal.warning_1.setText("¡Guia de Salida Registrada Exitosamente!")
        
    def Descontador(self):
        for h in range(len(self.ListaProductosEnSalida)):
            CantProd = self.ConnectProducto.ObtenerCantidadProd(self.ObjProductoID[h])
            CantReduce = self.ObjCantidadProd[h]
            NewCant = int(CantProd) - int(CantReduce)
            self.ConnectProducto.UpdateCantProd(NewCant, self.ObjProductoID[h])
            
    ##########################################################################
    
    # Inicio de Listar Guias de Salida
    
    def ListarGuiasSalida(self):
        ConnectGuiaSalidaDao = GuiaSalidaDao.GuiaSalidaBD()
        ConnectReportSalida = ReporteSalidaDao.ReporteSalidaBD()
        
        TbGuiaSalidaP = ConnectGuiaSalidaDao.ConsultaTablaGuiaSalida()
        Cantidad = len(TbGuiaSalidaP)
        self.guiasal.tw_reg_guisal.verticalHeader().setVisible(False)
        self.guiasal.tw_reg_guisal.setRowCount(Cantidad)
        Fila = 0
        
        
        for obj in TbGuiaSalidaP:
            CantYtoT = ConnectReportSalida.ConsultaCantYtotXGuiaSalida(obj[0])
            Cantidad = 0
            PrecioF = 0
            for k in range(len(CantYtoT)):
                Valor = CantYtoT[k]
                Cantidad += int(Valor[0])
                PrecioF += float(Valor[1])
            self.guiasal.tw_reg_guisal.setItem(Fila, 0, QTableWidgetItem(str(obj[0])))
            self.guiasal.tw_reg_guisal.setItem(Fila, 1, QTableWidgetItem(str(obj[1])))
            self.guiasal.tw_reg_guisal.setItem(Fila, 2, QTableWidgetItem((obj[2]+" "+obj[3])))
            self.guiasal.tw_reg_guisal.setItem(Fila, 3, QTableWidgetItem((obj[4]+" "+obj[5])))
            self.guiasal.tw_reg_guisal.setItem(Fila, 4, QTableWidgetItem(str(obj[6])))
            self.guiasal.tw_reg_guisal.setItem(Fila, 5, QTableWidgetItem(obj[7]))
            self.guiasal.tw_reg_guisal.setItem(Fila, 6, QTableWidgetItem(obj[8]))
            self.guiasal.tw_reg_guisal.setItem(Fila, 7, QTableWidgetItem(str(Cantidad)))
            self.guiasal.tw_reg_guisal.setItem(Fila, 8, QTableWidgetItem("S/ "+str(PrecioF)))
            Fila +=1
            
        for row in range(self.guiasal.tw_reg_guisal.rowCount()):
            for column in range(self.guiasal.tw_reg_guisal.columnCount()):
                item = self.guiasal.tw_reg_guisal.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
        
        self.guiasal.tw_reg_guisal.resizeColumnsToContents()
        self.guiasal.tw_reg_guisal.setEditTriggers(QTableWidget.NoEditTriggers)

                
     
                
                    
        