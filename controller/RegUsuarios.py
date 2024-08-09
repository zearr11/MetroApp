from PyQt5 import uic
from controller import PoliticasSeguridad
from dao import RegistroUserDao
import re

class RegUsuarios:
    
    def __init__(self):
        self.newUser = uic.loadUi("view/FRM_REG_USER_NUEVO.ui")
        self.newUser.setWindowTitle("Gestion de Usuarios")
        
        self.Conexion = RegistroUserDao.RegUserDB()
        Cargos = self.Conexion.DataCargo()
        Permisos = self.Conexion.DataPermisos()
        Documentos = self.Conexion.DataDocumentos()
        self.newUser.cb_rol_reg.addItems(Cargos)
        self.newUser.cb_permisos_reg.addItems(Permisos)
        self.newUser.cb_tipoDNI_personal.addItems(Documentos)
        
        #Boton Cancelar Retorna al FRM Politicas de Seguridad
        self.newUser.bt_cancelar.clicked.connect(self.CancelarReg)
        
        #Boton Guardar almacena los datos en la BD
        self.newUser.bt_guardar.clicked.connect(self.GuardadoData)
        
        self.newUser.show()
        
    def CancelarReg(self):
        self.newUser.close()
        self.poli = PoliticasSeguridad.PoliticasSeguridad()
        
        
    def GuardadoData(self):
        self.ValidacionDatos()
        
    def ValidacionDatos(self):
        
        #Asignacion de variables a los line edit
        Nombre = self.newUser.le_name_personal.text()
        Apellido = self.newUser.le_lastname_personal.text()
        Celular = self.newUser.le_celular_personal.text()
        NumeroDNI = self.newUser.le_numeroDNI_personal.text()
        UsuarioName = self.newUser.le_user_reg.text()
        email = self.newUser.le_correo_reg.text()
        passwordUser = self.newUser.le_pass_reg.text()
        
        #Asignacion de variables a los qcomboBox
        TipoDOC = self.newUser.cb_tipoDNI_personal.currentText()
        Rol = self.newUser.cb_rol_reg.currentText()
        Permise = self.newUser.cb_permisos_reg.currentText()
        
        #Validacion de datos
        if len(Nombre)==0 or len(Apellido)==0 or len(Celular)==0 or len(NumeroDNI)==0 or len(UsuarioName)==0 or len(email)==0 or len(passwordUser)==0:
            self.newUser.warning.setText("¡Ningun campo debe estar vacio!")
            
        else:
            if TipoDOC=="Seleccione" or Rol=="Seleccione" or Permise=="Seleccione":
                self.newUser.warning.setText("¡No olvides seleccionar los desplegables!")
                
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, email):
                    self.newUser.warning.setText("¡El correo electrónico no es válido!")
                    
                else:
                    if len(Nombre)>45:
                        self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Nombres")
                        
                    else:
                        if len(Apellido)>45:
                            self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Apellidos")
                            
                        else:
                            if len(Celular) != 9:
                                self.newUser.warning.setText("Numero de Telefono inválido")
                                
                            else:
                                password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
                                if not re.match(password_regex, passwordUser):
                                    self.newUser.warning.setText("¡La contraseña debe tener al menos 8 caracteres, incluir letras, números y al menos un carácter especial!")
                                
                                else:
                                    if len(UsuarioName)<5 or len(UsuarioName)>8:
                                        self.newUser.warning.setText("¡Nombre de Usuario inválido, no cumple los requerimientos!")
                                    else:
                                        if TipoDOC == "DNI":
                                            dni_regex = r'^\d{8}$'
                                            if not re.match(dni_regex, NumeroDNI):
                                                self.newUser.warning.setText("¡El DNI no es válido! Debe tener 8 dígitos")
                                            else:
                                                self.newUser.warning.setText("")
                                                self.ValidacionCorrecta()
                                
                                        elif TipoDOC == "CE":
                                            ce_regex = r'^[a-zA-Z0-9]{9}$'
                                            if not re.match(ce_regex, NumeroDNI):
                                                self.newUser.warning.setText("¡El Carnet de Extranjería no es válido! Debe tener 9 caracteres alfanuméricos.")
                                            else:
                                                self.newUser.warning.setText("")
                                                self.ValidacionCorrecta()
                                        
                                        
                                    
                                
    def ValidacionCorrecta(self):
        #Asignacion de variables a los line edit
        Nombre = self.newUser.le_name_personal.text()
        Apellido = self.newUser.le_lastname_personal.text()
        Celular = self.newUser.le_celular_personal.text()
        NumeroDNI = self.newUser.le_numeroDNI_personal.text()
        UsuarioName = self.newUser.le_user_reg.text()
        email = self.newUser.le_correo_reg.text()
        passwordUser = self.newUser.le_pass_reg.text()
        
        #Asignacion de variables a los qcomboBox
        TipoDOC1 = self.newUser.cb_tipoDNI_personal.currentText()
        Rol1 = self.newUser.cb_rol_reg.currentText()
        Permise1 = self.newUser.cb_permisos_reg.currentText()
        
        #Consulta en dao
        DaoReg = RegistroUserDao.RegUserDB()
        TipoDOC = DaoReg.ObtenerDocumentoID(TipoDOC1)
        Rol = DaoReg.ObtenerCargoID(Rol1)
        Permise = DaoReg.ObtenerPermisoID(Permise1)
        
        #InsertDataenTablaContacto
        DaoReg.InsertTablaContacto(Celular, email)
        idContacto = DaoReg.ObtenerContactoID(Celular, email)
        
        #InsertDataEnTablaPersona
        DaoReg.InsertTablaPersona(Nombre, Apellido, NumeroDNI, TipoDOC, idContacto)
        idPersona = DaoReg.ObtenerPersonaID(Nombre, Apellido, NumeroDNI, TipoDOC, idContacto)
        
        #InsertDataEnTablaUsuario
        DaoReg.InsertTablaUser(UsuarioName, passwordUser, idPersona, TipoDOC, idContacto, Rol, Permise)
        
        self.newUser.warning.setText("¡Registro exitoso!")