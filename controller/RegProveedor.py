from PyQt5 import uic
from controller import MenuPrincipal
from dao import CategoriaDao, ProveedorDao
from model import ProveedorModel
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt
import re


class RegProveedorFRM:
    
    def __init__(self):
        self.newProv = uic.loadUi("view/FRM_REG_PROVE.ui")
        self.newProv.setWindowTitle("Gestion de Proveedores")
        self.HideWidgets()
        
        #Cargado de Dao en ComboBox
        self.ConnectProveedorDao = ProveedorDao.ProveedorBD()
        ConnectCategoriaDao = CategoriaDao.CategoriaBD()
        self.CategoriaC = ConnectCategoriaDao.DataCategoria()
        
        self.newProv.tw_showProv.cellClicked.connect(self.ClickTablaProve)
        
        self.newProv.bt_nuevo_prov.clicked.connect(self.NuevoRegProveedor)
        self.newProv.bt_mod_prov.clicked.connect(self.ModifProveedor)
        self.newProv.bt_cancelar_prov.clicked.connect(self.CancelarProv)
        self.newProv.bt_guardar_prov.clicked.connect(self.GuardarProv)
        self.newProv.pb_actualizar.clicked.connect(self.ActualizaProvee)
        self.newProv.show()
        
    #################################################################################
    
    def HideWidgets(self):
        self.newProv.window_1_pv.hide()
        self.newProv.window_2_mod.hide()        
        
    def ShowWidget(self, prmtro):
        if prmtro == self.newProv.window_1_pv:
            if self.newProv.window_1_pv.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
                self.CargadoRegProveedor()
        else:
            if prmtro == self.newProv.window_2_mod:
                if self.newProv.window_2_mod.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
                    self.CargadoModProveedor()
                    
    def CargadoRegProveedor(self):
        self.newProv.cb_rubro_prov.clear()
        self.newProv.cb_rubro_prov.addItems(self.CategoriaC)
        
    def CargadoModProveedor(self):
        self.newProv.qc_rubroMod.clear()
        self.newProv.qc_rubroMod.addItems(self.CategoriaC)
        self.LlenadoTabla()
        self.BloquearTXTProve()
        
        
    #################################################################################    
    #BOTONES GESTION PROVEEDOR
    def CancelarProv(self):
        self.newProv.close()
        self.menu = MenuPrincipal.MenuFRM()
    
    def NuevoRegProveedor(self):
        self.ShowWidget(self.newProv.window_1_pv)
        
    def ModifProveedor(self):
        self.ShowWidget(self.newProv.window_2_mod)
        
    #################################################################################
    
    
    def GuardarProv(self):
        self.ValidacionProvLV1()
        
    def ValidacionProvLV1(self):
        self.RazonSocial = self.newProv.le_razon_soc.text()
        self.NumeroRUC = self.newProv.le_ruc.text()
        self.Direccion = self.newProv.le_direcc_prov.text()
        self.Telefono = self.newProv.le_telf_prov.text()
        self.Email = self.newProv.le_email_prov.text()
        self.Categoria = self.newProv.cb_rubro_prov.currentText()
        
        if len(self.RazonSocial) == 0 or len(self.NumeroRUC) == 0 or len(self.Direccion) == 0 or len(self.Telefono) == 0 or len(self.Email) == 0:
            self.newProv.warning.setText("¡Ningun campo debe estar vacio!")
        else:
            if self.Categoria == "Seleccione":
                self.newProv.warning.setText("¡Selecciona el Rubro correspondiente!") 
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.Email):
                    self.newProv.warning.setText("¡El correo electrónico no es válido!")
                else:
                    self.ValidacionProvLV2()
                    
    def ValidacionProvLV2(self):
        if len(self.Telefono) != 7:
            self.newProv.warning.setText("¡El numero de telefono ingresado no es válido! \nDebe tener 7 digitos")
        else:
            if len(self.NumeroRUC) != 11:  
                self.newProv.warning.setText("¡El numero RUC ingresado no es válido! \nDebe tener 11 digitos")
            else:
                self.newProv.warning.setText("")
                self.ValidacionProvCorrecta()
                
    def ValidacionProvCorrecta(self):
        DtProveedor = ProveedorModel.ProveedorCLASS(self.RazonSocial, self.NumeroRUC, self.Direccion, self.Telefono, self.Email, self.Categoria)
        DtProveedor.Nuevo_Proveedor()
        self.newProv.warning.setText("¡Registro exitoso!")
        
        
    #####################################################################################
    #MODIFICAR PROVE
    
    def LlenadoTabla(self):
        LstProv = self.ConnectProveedorDao.ConsultaTablaProveedor()
        Cantidad = len(LstProv)
        self.newProv.tw_showProv.verticalHeader().setVisible(False)
        self.newProv.tw_showProv.setRowCount(Cantidad)
        Fila = 0
        for objProv in LstProv:
            self.newProv.tw_showProv.setItem(Fila, 0, QTableWidgetItem(str(objProv[0])))
            self.newProv.tw_showProv.setItem(Fila, 1, QTableWidgetItem(objProv[1]))
            self.newProv.tw_showProv.setItem(Fila, 2, QTableWidgetItem(objProv[2]))
            self.newProv.tw_showProv.setItem(Fila, 3, QTableWidgetItem(objProv[3]))
            self.newProv.tw_showProv.setItem(Fila, 4, QTableWidgetItem(objProv[4]))
            self.newProv.tw_showProv.setItem(Fila, 5, QTableWidgetItem(str(objProv[5])))
            self.newProv.tw_showProv.setItem(Fila, 6, QTableWidgetItem(objProv[6]))
            Fila +=1
        for row in range(self.newProv.tw_showProv.rowCount()):
            for column in range(self.newProv.tw_showProv.columnCount()):
                item = self.newProv.tw_showProv.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
        self.newProv.tw_showProv.resizeColumnsToContents()
        self.newProv.tw_showProv.setEditTriggers(QTableWidget.NoEditTriggers)
        
    def BloquearTXTProve(self):
        self.newProv.le_razon_social_mod.setEnabled(False)
        self.newProv.le_ruc_mod.setEnabled(False)
        self.newProv.qc_rubroMod.setEnabled(False)
        self.newProv.le_telfMOD.setEnabled(False)
        self.newProv.le_direccMod.setEnabled(False)
        self.newProv.le_emailMod.setEnabled(False)
        
    def ClickTablaProve(self, fila):
        idProv= self.newProv.tw_showProv.item(fila, 0).text()
        self.objProduct = self.ConnectProveedorDao.ObtenerProveedor(idProv)
        self.newProv.le_razon_social_mod.setText(self.objProduct[1])
        self.newProv.le_razon_social_mod.setEnabled(True)
        self.newProv.le_ruc_mod.setText(self.objProduct[2])
        self.newProv.le_ruc_mod.setEnabled(True)
        self.newProv.le_direccMod.setText(self.objProduct[3])
        self.newProv.le_direccMod.setEnabled(True) 
        self.newProv.le_emailMod.setText(self.objProduct[4])
        self.newProv.le_emailMod.setEnabled(True)
        self.newProv.le_telfMOD.setText(str(self.objProduct[5]))
        self.newProv.le_telfMOD.setEnabled(True)
        self.newProv.qc_rubroMod.setCurrentText(self.objProduct[6])
        self.newProv.qc_rubroMod.setEnabled(True)
        self.newProv.warning_mod.setText("")
    
    def ActualizaProvee(self):
        self.CambioRazonS = self.newProv.le_razon_social_mod.text()
        self.CambioRUC = self.newProv.le_ruc_mod.text()
        self.CambioDirecc = self.newProv.le_direccMod.text()
        self.CambioEmail = self.newProv.le_emailMod.text()
        self.CambioTelf = self.newProv.le_telfMOD.text()
        self.CambioRubro = self.newProv.qc_rubroMod.currentText()
        
        if len(self.CambioRazonS) == 0 or len(self.CambioRUC) == 0 or len(self.CambioDirecc) == 0 or len(self.CambioTelf) == 0 or len(self.CambioEmail) == 0:
            self.newProv.warning_mod.setText("¡Ningun campo debe estar vacio!")
        else:
            if self.CambioRubro == "Seleccione":
                self.newProv.warning_mod.setText("¡Selecciona el Rubro correspondiente!") 
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.CambioEmail):
                    self.newProv.warning_mod.setText("¡El correo electrónico no es válido!")
                else:
                    if len(self.CambioTelf) != 7:
                        self.newProv.warning_mod.setText("¡El numero de telefono ingresado no es válido! Debe tener 7 digitos")
                    else:
                        if len(self.CambioRUC) != 11:  
                            self.newProv.warning_mod.setText("¡El numero RUC ingresado no es válido! Debe tener 11 digitos")
                        else:
                            self.newProv.warning_mod.setText("")
                            DtNewProveedor = ProveedorModel.ProveedorCLASS(self.objProduct[1], self.objProduct[2], self.objProduct[3], self.objProduct[5], self.objProduct[4], self.objProduct[6])
                            DtNewProveedor.Actualizar_Proveedor(self.CambioRazonS, self.CambioRUC, self.CambioDirecc, self.CambioTelf, self.CambioEmail, self.CambioRubro, self.objProduct[0])
                            self.newProv.warning_mod.setText("¡Datos de Proveedor actualizados con éxito!")
                            self.BloquearTXTProve()
                            self.LlenadoTabla()
                            
                            
        