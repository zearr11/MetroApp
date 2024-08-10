from PyQt5 import uic
from controller import PoliticasSeguridad
from dao import CargoDao, PermisoDao, TipoDocumentoDao
from model import UsuariosModel
import re


class RegUsuariosFRM:
    
    def __init__(self):
        self.newUser = uic.loadUi("view/FRM_REG_USER_NUEVO.ui")
        self.newUser.setWindowTitle("Gestion de Usuarios")
        
        #Cargado de Dao's en ComboBox's
        ConnectCargoDao = CargoDao.CargoBD()
        ConnectPermisoDao = PermisoDao.PermisoBD()
        ConnectTipoDocumentoDao = TipoDocumentoDao.TipoDocumentoBD()
        Cargos = ConnectCargoDao.DataCargo()
        Permisos = ConnectPermisoDao.DataPermisos()
        TipoDocumento = ConnectTipoDocumentoDao.DataTipoDocumento()
        self.newUser.cb_rol_reg.addItems(Cargos)
        self.newUser.cb_permisos_reg.addItems(Permisos)
        self.newUser.cb_tipoDNI_personal.addItems(TipoDocumento)
        
        #Boton Cancelar Retorna al FRM Politicas de Seguridad
        self.newUser.bt_cancelar.clicked.connect(self.CancelarReg)
        #Boton Guardar almacena los datos en la BD
        self.newUser.bt_guardar.clicked.connect(self.SaveUsuario)
        #Inicio de FRM Reg Usuarios
        self.newUser.show()
        
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