from PyQt5 import uic
from controller import MenuPrincipal
from dao import TipoDocumentoDao, ClienteDao
from model import ClientesModel
import re
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt


class RegClientesFRM:
    
    def __init__(self):
        self.newCient = uic.loadUi("view/FRM_REG_CLIENT.ui")
        self.newCient.setWindowTitle("Gestion de Clientes")
        
        self.HideWidgets()
        
        #Cargado de Dao en ComboBox
        self.ConnectClienteDao = ClienteDao.ClienteBD()
        ConnectDocumentoDao = TipoDocumentoDao.TipoDocumentoBD()
        self.Documentos = ConnectDocumentoDao.DataTipoDocumento()

        self.newCient.tw_showClient.cellClicked.connect(self.ClickTablaClientes)
        self.newCient.bt_guardar_cl.clicked.connect(self.GuardadoCliente)
        self.newCient.bt_cancelar_cl.clicked.connect(self.CancelarClient)
        self.newCient.pb_actualizarClient.clicked.connect(self.SaveCambiosCliente)
        
        self.newCient.bt_nuevo_cl.clicked.connect(self.BtNuevo)
        self.newCient.bt_modCl.clicked.connect(self.BtModificar)
        
        self.newCient.show()
        
        
        
    def HideWidgets(self):
        self.newCient.window_1_cl.hide()
        self.newCient.window_2_Mod.hide()
        
    def ShowWidget(self, widget):
        if widget == self.newCient.window_1_cl:
            if self.newCient.window_1_cl.isVisible():
                pass
            else:
                self.HideWidgets()
                widget.show()
                self.CargadoRegCliente()
        else:
            if widget == self.newCient.window_2_Mod:
                if self.newCient.window_2_Mod.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    widget.show()
                    self.CargadoModCliente()
                    
                    
    def CargadoRegCliente(self):
        self.newCient.cb_tipoDNI_client.clear()
        self.newCient.cb_tipoDNI_client.addItems(self.Documentos)
        
    def CargadoModCliente(self):
        self.newCient.qc_tdoc.clear()
        self.newCient.qc_tdoc.addItems(self.Documentos)
        
        self.ListarTablaCliente()
        self.newCient.tw_showClient.resizeColumnsToContents()
        self.newCient.tw_showClient.setEditTriggers(QTableWidget.NoEditTriggers)
        self.BloquearTxtCliente()
        
        
    def BtNuevo(self):
        self.ShowWidget(self.newCient.window_1_cl)
        
    def BtModificar(self):
        self.ShowWidget(self.newCient.window_2_Mod)
    
    
######################################################################### 
    def CancelarClient(self):
        self.newCient.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def GuardadoCliente(self):
        self.ValidaccionC_LV1()
        
    def ValidaccionC_LV1(self):
        self.Nombres = self.newCient.le_name_client.text()
        self.Apellidos = self.newCient.le_lastname_client.text()
        self.NumeroDoc = self.newCient.le_dni_client.text()
        self.Direccion = self.newCient.le_direcc_client.text()
        self.Telefono = self.newCient.le_telf_client.text()
        self.Email = self.newCient.le_email_client.text()
        self.TipoDOC = self.newCient.cb_tipoDNI_client.currentText()
        
        if len(self.Nombres) == 0 or len(self.Apellidos) == 0 or len(self.NumeroDoc) == 0 or len(self.Direccion) == 0 or len(self.Telefono) == 0 or len(self.Email) == 0:
            self.newCient.warning.setText("¡Ningun campo debe estar vacio!")
        else:
            if self.TipoDOC == "Seleccione":
                self.newCient.warning.setText("¡Selecciona el Tipo de Documento!")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.Email):
                    self.newCient.warning.setText("¡El correo electrónico no es válido!")
                else:
                    if len(self.Nombres)>45:
                        self.newCient.warning.setText("¡Error! Solo se permiten hasta 45 \ncaracteres en el campo 'Nombres'")
                    else:
                        if len(self.Apellidos)>45:
                            self.newCient.warning.setText("¡Error! Solo se permiten hasta 45 \ncaracteres en el campo 'Apellidos'")
                        else:
                            self.ValidaccionC_LV2()
    
    def ValidaccionC_LV2(self):
        if len(self.Telefono) != 9:
            self.newCient.warning.setText("¡El numero de telefono ingresado no es válido!")               
        else:
            if self.TipoDOC == "DNI":
                dni_regex = r'^\d{8}$'
                if not re.match(dni_regex, self.NumeroDoc):
                    self.newCient.warning.setText("¡El Numero de DNI ingresado no es válido! \nDebe tener 8 dígitos")
                else:
                    self.newCient.warning.setText("")
                    self.ValidacionClCorrecta()
                                
            elif self.TipoDOC == "CE":
                ce_regex = r'^[a-zA-Z0-9]{9}$'
                if not re.match(ce_regex, self.NumeroDoc):
                    self.newCient.warning.setText("¡El Carnet de Extranjería ingresado no es válido! \nDebe tener 9 caracteres alfanuméricos")
                else:
                    self.newCient.warning.setText("")
                    self.ValidacionClCorrecta()
    
    def ValidacionClCorrecta(self):
        DtCliente = ClientesModel.ClienteCLASS(self.Nombres, self.Apellidos, self.Telefono, self.Email, self.NumeroDoc, self.TipoDOC, self.Direccion)
        DtCliente.Nuevo_Cliente()
        self.newCient.warning.setText("¡Registro exitoso!")
        
#########################################################################

    def BloquearTxtCliente(self):
        self.newCient.le_modName.setEnabled(False)
        self.newCient.qc_tdoc.setEnabled(False)
        self.newCient.le_ndoc.setEnabled(False)
        self.newCient.le_correomod.setEnabled(False)
        self.newCient.le_lastmod.setEnabled(False)
        self.newCient.le_direccMod.setEnabled(False)
        self.newCient.le_celuMod.setEnabled(False)
        
    def ListarTablaCliente(self):
        LstClientes = self.ConnectClienteDao.ConsultaTablaCliente()
        Cantidad = len(LstClientes)
        self.newCient.tw_showClient.verticalHeader().setVisible(False)
        self.newCient.tw_showClient.setRowCount(Cantidad)
        Fila = 0
        
        for objCliente in LstClientes:
            self.newCient.tw_showClient.setItem(Fila, 0, QTableWidgetItem(str(objCliente[0])))
            self.newCient.tw_showClient.setItem(Fila, 1, QTableWidgetItem(objCliente[1]))
            self.newCient.tw_showClient.setItem(Fila, 2, QTableWidgetItem(objCliente[2]))
            self.newCient.tw_showClient.setItem(Fila, 3, QTableWidgetItem(objCliente[3]))
            self.newCient.tw_showClient.setItem(Fila, 4, QTableWidgetItem(objCliente[4]))
            self.newCient.tw_showClient.setItem(Fila, 5, QTableWidgetItem(objCliente[5]))
            self.newCient.tw_showClient.setItem(Fila, 6, QTableWidgetItem(str(objCliente[6])))
            self.newCient.tw_showClient.setItem(Fila, 7, QTableWidgetItem(objCliente[7]))
            Fila +=1
            
        for row in range(self.newCient.tw_showClient.rowCount()):
            for column in range(self.newCient.tw_showClient.columnCount()):
                item = self.newCient.tw_showClient.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
                    
    def ClickTablaClientes(self, fila):
        self.idCliente = self.newCient.tw_showClient.item(fila, 0).text()
        self.objCliente = self.ConnectClienteDao.ObtenerCliente(self.idCliente)
        self.newCient.le_modName.setText(self.objCliente[1])
        self.newCient.le_modName.setEnabled(True)
        self.newCient.le_lastmod.setText(self.objCliente[2])
        self.newCient.le_lastmod.setEnabled(True)
        #
        self.newCient.qc_tdoc.setCurrentText(self.objCliente[3])
        #
        self.newCient.le_ndoc.setText(self.objCliente[4])
        self.newCient.le_ndoc.setEnabled(True)
        self.newCient.le_direccMod.setText(self.objCliente[5])
        self.newCient.le_direccMod.setEnabled(True)
        self.newCient.le_celuMod.setText(str(self.objCliente[6]))
        self.newCient.le_celuMod.setEnabled(True)
        self.newCient.le_correomod.setText(self.objCliente[7])
        self.newCient.le_correomod.setEnabled(True)
        self.newCient.warningMOD.setText("")
        
    def SaveCambiosCliente(self):
        self.CambioNomCliente = self.newCient.le_modName.text()
        self.CambioApeCliente = self.newCient.le_lastmod.text()
        #self.CambioTipoDoc = self.newCient.qc_tdoc.currentText()
        self.CambioNumCliente = self.newCient.le_ndoc.text()
        self.CambioDireccionCliente = self.newCient.le_direccMod.text()
        self.CambioTelfCliente = self.newCient.le_celuMod.text()
        self.CambioEmailCliente = self.newCient.le_correomod.text()
        
        if self.newCient.le_modName.isEnabled():
            if len(self.CambioNomCliente) == 0 or len(self.CambioApeCliente) == 0 or len(self.CambioNumCliente) == 0 or len(self.CambioDireccionCliente) == 0 or len(self.CambioTelfCliente) == 0 or len(self.CambioEmailCliente) == 0:
                self.newCient.warningMOD.setText("¡Para actualizar los datos, ningun campo debe estar vacío!")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.CambioEmailCliente):
                    self.newCient.warningMOD.setText("¡El correo electrónico no es válido!")
                else:
                    if len(self.CambioNomCliente)>45:
                        self.newCient.warningMOD.setText("Solo se permiten hasta 45 caracteres en el campo 'Nombres'")
                    else:
                        if len(self.CambioApeCliente)>45:
                            self.newCient.warningMOD.setText("Solo se permiten hasta 45 caracteres en el campo 'Apellidos'")
                        else:
                            if len(self.CambioTelfCliente) != 9:
                                self.newCient.warningMOD.setText("¡El numero de celular ingresado no es válido!")  
                            else:
                                if self.objCliente[3] == "DNI":
                                    dni_regex = r'^\d{8}$'
                                    if not re.match(dni_regex, self.CambioNumCliente):
                                        self.newCient.warningMOD.setText("¡El Numero de DNI ingresado no es válido!")
                                    else:
                                        self.newCient.warningMOD.setText("")
                                        CambioCliente = ClientesModel.ClienteCLASS(self.objCliente[1], self.objCliente[2], self.objCliente[6], self.objCliente[7], self.objCliente[4], self.objCliente[3], self.objCliente[5])
                                        CambioCliente.Update_Cliente(self.CambioNomCliente, self.CambioApeCliente, self.CambioTelfCliente, self.CambioEmailCliente, self.CambioNumCliente, self.objCliente[3], self.CambioDireccionCliente, self.objCliente[0])
                                        self.newCient.warningMOD.setText("¡Datos de Cliente actualizados con éxito!")
                                        self.BloquearTxtCliente()
                                        self.ListarTablaCliente()
                                        self.newCient.tw_showClient.resizeColumnsToContents()
                                        self.newCient.tw_showClient.setEditTriggers(QTableWidget.NoEditTriggers)
                                
                                elif self.objCliente[3] == "CE":
                                    ce_regex = r'^[a-zA-Z0-9]{9}$'
                                    if not re.match(ce_regex, self.CambioNumCliente):
                                        self.newCient.warningMOD.setText("¡El Carnet de Extranjería ingresado no es válido!")
                                    else:
                                        self.newCient.warningMOD.setText("")
                                        CambioCliente = ClientesModel.ClienteCLASS(self.objCliente[1], self.objCliente[2], self.objCliente[6], self.objCliente[7], self.objCliente[4], self.objCliente[3], self.objCliente[5])
                                        CambioCliente.Update_Cliente(self.CambioNomCliente, self.CambioApeCliente, self.CambioTelfCliente, self.CambioEmailCliente, self.CambioNumCliente, self.objCliente[3], self.CambioDireccionCliente, self.objCliente[0])
                                        self.newCient.warningMOD.setText("¡Datos de Cliente actualizados con éxito!")
                                        self.BloquearTxtCliente()
                                        self.ListarTablaCliente()
                                        self.newCient.tw_showClient.resizeColumnsToContents()
                                        self.newCient.tw_showClient.setEditTriggers(QTableWidget.NoEditTriggers)
                                
        else:
            self.newCient.warningMOD.setText("¡Para modificar un registro, primero seleccionalo en la tabla!")