from PyQt5 import uic
from controller import PoliticasSeguridad
from dao import CargoDao, PermisoDao, TipoDocumentoDao, UsuarioDao
from model import UsuariosModel
from PyQt5.QtWidgets import QTableWidgetItem
import re


class RegUsuariosFRM:

    def __init__(self, c):
        self.newUser = uic.loadUi("view/FRM_REG_USER_NUEVO.ui")
        self.newUser.setWindowTitle("Gestion de Usuarios")
        
        ConnectCargoDao = CargoDao.CargoBD()
        ConnectPermisoDao = PermisoDao.PermisoBD()
        ConnectTipoDocumentoDao = TipoDocumentoDao.TipoDocumentoBD()
        
        Cargos = ConnectCargoDao.DataCargo()
        Permisos = ConnectPermisoDao.DataPermisos()
        TipoDocumento = ConnectTipoDocumentoDao.DataTipoDocumento()
        
        self.OcultarWidgets()
        if c == True:
            self.newUser.wd_regUser.show()
            #Cargado de Dao's en ComboBox's
            self.newUser.cb_rol_reg.addItems(Cargos)
            self.newUser.cb_permisos_reg.addItems(Permisos)
            self.newUser.cb_tipoDNI_personal.addItems(TipoDocumento)
            #Botones
            self.newUser.bt_cancelar.clicked.connect(self.CancelarReg)
            self.newUser.bt_guardar.clicked.connect(self.SaveUsuario)
            
        else:
            self.newUser.wd_modUser.show()
            self.UsuarioDao = UsuarioDao.UsuarioBD()
            self.ListarUsuarios()
            self.newUser.tw_showUser.setColumnWidth(6, 125)
            self.newUser.tw_showUser.setColumnWidth(7, 75)
            self.newUser.tw_showUser.setColumnWidth(8, 135)
            #Cargado de Dao's en ComboBox's
            self.newUser.qcb_cargo.addItems(Cargos)
            self.newUser.qcb_permisos.addItems(Permisos)
            #Desactivado de Entrada de Texto
            self.BloquearTextoMod()
            #Botones
            self.newUser.bt_cancelar_cl.clicked.connect(self.RegresarChanges)
            self.newUser.tw_showUser.cellClicked.connect(self.ClickEnTabla)
            self.newUser.pb_actualizar.clicked.connect(self.SaveChangesUser)
    
        self.newUser.show()
        
    def OcultarWidgets(self):
        self.newUser.wd_modUser.hide()
        self.newUser.wd_regUser.hide()
        
    def BloquearTextoMod(self):
        self.newUser.le_usuario.setEnabled(False)
        self.newUser.le_pass.setEnabled(False)
        self.newUser.le_name.setEnabled(False)
        self.newUser.le_last.setEnabled(False)
        self.newUser.le_tipDoc.setEnabled(False)
        self.newUser.le_numDoc.setEnabled(False)
        self.newUser.le_celu.setEnabled(False)
        self.newUser.le_email.setEnabled(False)
        self.newUser.qcb_cargo.setEnabled(False)
        self.newUser.qcb_permisos.setEnabled(False)

########################################################################   
# WIDGET REGISTRO DE NUEVO USUARIO

    def CancelarReg(self):
        self.newUser.close()
        self.poli = PoliticasSeguridad.PoliticasSeguridadFRM()
        
    def SaveUsuario(self):
        self.ValidacionLV1()
        
    def ValidacionLV1(self):
        #Line's Edit's
        self.Nombres = self.newUser.le_name_personal.text()
        self.Apellidos = self.newUser.le_lastname_personal.text()
        self.Celular = self.newUser.le_celular_personal.text()
        self.NumeroDNI = self.newUser.le_numeroDNI_personal.text()
        self.NombreUser = self.newUser.le_user_reg.text()
        self.Email = self.newUser.le_correo_reg.text()
        self.Password = self.newUser.le_pass_reg.text()
        #QCombo's Box
        self.TipoDoc = self.newUser.cb_tipoDNI_personal.currentText()
        self.Cargo = self.newUser.cb_rol_reg.currentText()
        self.Permisos = self.newUser.cb_permisos_reg.currentText()
        
        if len(self.Nombres)==0 or len(self.Apellidos)==0 or len(self.Celular)==0 or len(self.NumeroDNI)==0 or len(self.NombreUser)==0 or len(self.Email)==0 or len(self.Password)==0:
            self.newUser.warning.setText("¡Ningun campo debe estar vacio!")
        else:
            if self.TipoDoc == "Seleccione" or self.Cargo == "Seleccione" or self.Permisos == "Seleccione":
                self.newUser.warning.setText("¡No olvides seleccionar los desplegables!")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.Email):
                    self.newUser.warning.setText("¡El correo electrónico no es válido!")
                else:
                    self.ValidacionLV2()
                
    def ValidacionLV2(self):
        if len(self.Nombres)>45:
            self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Nombres'")            
        else:
            if len(self.Apellidos)>45:
                self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Apellidos'")
            else:
                if len(self.Celular) != 9:
                    self.newUser.warning.setText("¡El numero de telefono ingresado no es válido!")
                else:
                    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
                    if not re.match(password_regex, self.Password):
                        self.newUser.warning.setText("¡La contraseña debe tener al menos 8 caracteres, incluir letras, números y al menos un carácter especial!")
                    else:
                        self.ValidacionLV3()
                        
    def ValidacionLV3(self):
        if len(self.NombreUser)<5 or len(self.NombreUser)>8:
            self.newUser.warning.setText("¡El nombre de usuario ingresado no es válido, no cumple los requerimientos!")
        else:
            if self.TipoDoc == "DNI":
                dni_regex = r'^\d{8}$'
                if not re.match(dni_regex, self.NumeroDNI):
                    self.newUser.warning.setText("¡El Numero de DNI ingresado no es válido! Debe tener 8 dígitos")
                else:
                    self.newUser.warning.setText("")
                    self.ValidacionUserCorrecta()
            else:
                if self.TipoDoc == "CE":
                    ce_regex = r'^[a-zA-Z0-9]{9}$'
                    if not re.match(ce_regex, self.NumeroDNI):
                        self.newUser.warning.setText("¡El Carnet de Extranjería ingresado no es válido! Debe tener 9 caracteres alfanuméricos")
                    else:
                        self.newUser.warning.setText("")
                        self.ValidacionUserCorrecta()
    
    def ValidacionUserCorrecta(self):
        RegNuevoUser = UsuariosModel.UsuariosCLASS(self.NombreUser, self.Password, self.Nombres, self.Apellidos, self.Celular, self.Email, self.NumeroDNI, self.TipoDoc, self.Cargo, self.Permisos)
        RegNuevoUser.Nuevo_Usuario()
        self.newUser.warning.setText("¡Registro exitoso!")
        
########################################################################   
# WIDGET MODIFICACION DE USUARIO
    
    def ListarUsuarios(self):
        ListaUser = self.UsuarioDao.ConsultaTablaUsuario()
        Cantidad = len(ListaUser)
        self.newUser.tw_showUser.verticalHeader().setVisible(False)
        self.newUser.tw_showUser.setRowCount(Cantidad)
        Fila = 0
        
        for objUser in ListaUser:
            self.newUser.tw_showUser.setItem(Fila, 0, QTableWidgetItem(str(objUser[0])))
            self.newUser.tw_showUser.setItem(Fila, 1, QTableWidgetItem(objUser[1]))
            self.newUser.tw_showUser.setItem(Fila, 2, QTableWidgetItem(objUser[2]))
            self.newUser.tw_showUser.setItem(Fila, 3, QTableWidgetItem(objUser[3]))
            self.newUser.tw_showUser.setItem(Fila, 4, QTableWidgetItem(objUser[4]))
            self.newUser.tw_showUser.setItem(Fila, 5, QTableWidgetItem(objUser[5]))
            self.newUser.tw_showUser.setItem(Fila, 6, QTableWidgetItem(objUser[6]))
            self.newUser.tw_showUser.setItem(Fila, 7, QTableWidgetItem(str(objUser[7])))
            self.newUser.tw_showUser.setItem(Fila, 8, QTableWidgetItem(objUser[8]))
            self.newUser.tw_showUser.setItem(Fila, 9, QTableWidgetItem(objUser[9]))
            self.newUser.tw_showUser.setItem(Fila, 10, QTableWidgetItem(str(objUser[10])))
            Fila +=1
        
    def ClickEnTabla(self, fila):
        idUser = self.newUser.tw_showUser.item(fila, 0).text()
        self.objUsuario = self.UsuarioDao.ObtenerUsuario(idUser)
        self.newUser.le_usuario.setText(self.objUsuario[1])
        self.newUser.le_usuario.setEnabled(True)
        self.newUser.le_pass.setText(self.objUsuario[2])
        self.newUser.le_pass.setEnabled(True)
        self.newUser.le_name.setText(self.objUsuario[3])
        self.newUser.le_last.setText(self.objUsuario[4])
        self.newUser.le_tipDoc.setText(self.objUsuario[5])
        self.newUser.le_numDoc.setText(self.objUsuario[6])
        self.newUser.le_celu.setText(str(self.objUsuario[7]))
        self.newUser.le_celu.setEnabled(True)
        self.newUser.le_email.setText(self.objUsuario[8])
        self.newUser.le_email.setEnabled(True)
        self.newUser.qcb_cargo.setCurrentText(self.objUsuario[9])
        self.newUser.qcb_cargo.setEnabled(True)
        self.newUser.qcb_permisos.setCurrentText(self.objUsuario[10])
        self.newUser.qcb_permisos.setEnabled(True)
        
    def RegresarChanges(self):
        self.CancelarReg()
        
    def SaveChangesUser(self):
        self.CambioUser = self.newUser.le_usuario.text()
        self.CambioPass = self.newUser.le_pass.text()
        self.CambioCelu = self.newUser.le_celu.text()
        self.CambioEmail = self.newUser.le_email.text()
        self.CambioCargo = self.newUser.qcb_cargo.currentText()
        self.CambioPermiso = self.newUser.qcb_permisos.currentText()
        
        if len(self.CambioUser) == 0 or len(self.CambioPass) == 0 or len(self.CambioCelu) == 0 or len(self.CambioEmail) == 0:
            self.newUser.warning_2.setText("Para actualizar los datos del Usuario, ningun campo debe estar vacio")
        else:
            if self.CambioCargo == "Seleccione" or self.CambioPermiso == 0:
                self.newUser.warning_2.setText("Selecciona un Item válido en los desplegables")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.CambioEmail):
                    self.newUser.warning_2.setText("El correo electrónico ingresado no es válido")
                else:
                    if len(self.CambioUser)<5:
                        self.newUser.warning_2.setText("Usuario inválido, se permite como minimo 5 caracteres en el nombre de usuario")
                    else:
                        if len(self.CambioUser)>8:
                            self.newUser.warning_2.setText("Usuario inválido, se permite como maximo 8 caracteres en el nombre de usuario")
                        else:
                            if len(self.CambioCelu) != 9:
                                self.newUser.warning_2.setText("El numero de telefono ingresado no es válido, debe tener 9 digitos")
                            else:
                                password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
                                if not re.match(password_regex, self.CambioPass):
                                    self.newUser.warning_2.setText("La contraseña debe tener al menos 8 caracteres, incluir letras, números y al menos un carácter especial")
                                else:
                                    DataUpdateUser = UsuariosModel.UsuariosCLASS(self.objUsuario[1], self.objUsuario[2], self.objUsuario[3], self.objUsuario[4], self.objUsuario[7], self.objUsuario[8], self.objUsuario[6], self.objUsuario[5], self.objUsuario[9], self.objUsuario[10])
                                    DataUpdateUser.Actualizar_Usuario(self.CambioUser, self.CambioPass, self.CambioCelu, self.CambioEmail, self.CambioCargo, self.CambioPermiso, self.objUsuario[0])
                                    self.newUser.warning_2.setText("¡Datos del Usuario actualizados con éxito!")
                                    self.BloquearTextoMod()
                                    self.ListarUsuarios()
                                    
        
                    
                
            
    