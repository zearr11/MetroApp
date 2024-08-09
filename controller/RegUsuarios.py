from PyQt5 import uic
from controller import PoliticasSeguridad
from dao import CargoDao, PermisoDao, DocumentoDao
from model import Usuarios
import re


class RegUsuariosFRM:
    
    def __init__(self):
        self.newUser = uic.loadUi("view/FRM_REG_USER_NUEVO.ui")
        self.newUser.setWindowTitle("Gestion de Usuarios")
        
        #Cargado de Dao's en ComboBox's
        ConnectCargoDao = CargoDao.CargoBD()
        ConnectPermisoDao = PermisoDao.PermisoBD()
        ConnectDocumentoDao = DocumentoDao.DocumentoBD()
        Cargos = ConnectCargoDao.DataCargo()
        Permisos = ConnectPermisoDao.DataPermisos()
        Documentos = ConnectDocumentoDao.DataDocumentos()
        self.newUser.cb_rol_reg.addItems(Cargos)
        self.newUser.cb_permisos_reg.addItems(Permisos)
        self.newUser.cb_tipoDNI_personal.addItems(Documentos)
        
        #Boton Cancelar Retorna al FRM Politicas de Seguridad
        self.newUser.bt_cancelar.clicked.connect(self.CancelarReg)
        #Boton Guardar almacena los datos en la BD
        self.newUser.bt_guardar.clicked.connect(self.GuardadoData)
        #Inicio de FRM Reg Usuarios
        self.newUser.show()
        
        
    def CancelarReg(self):
        self.newUser.close()
        self.poli = PoliticasSeguridad.PoliticasSeguridadFRM()
        
        
    def GuardadoData(self):
        self.ValidacionDatos()
        
        
    def ValidacionDatos(self):
        #Asignacion de variables a los line edit
        self.Nombre = self.newUser.le_name_personal.text()
        self.Apellido = self.newUser.le_lastname_personal.text()
        self.Celular = self.newUser.le_celular_personal.text()
        self.NumeroDNI = self.newUser.le_numeroDNI_personal.text()
        self.UsuarioName = self.newUser.le_user_reg.text()
        self.email = self.newUser.le_correo_reg.text()
        self.passwordUser = self.newUser.le_pass_reg.text()
        
        #Asignacion de variables a los qcomboBox
        self.TipoDOC = self.newUser.cb_tipoDNI_personal.currentText()
        self.Rol = self.newUser.cb_rol_reg.currentText()
        self.Permise = self.newUser.cb_permisos_reg.currentText()
        
        #Validacion de datos
        if len(self.Nombre)==0 or len(self.Apellido)==0 or len(self.Celular)==0 or len(self.NumeroDNI)==0 or len(self.UsuarioName)==0 or len(self.email)==0 or len(self.passwordUser)==0:
            self.newUser.warning.setText("¡Ningun campo debe estar vacio!")
            
        else:
            if self.TipoDOC == "Seleccione" or self.Rol == "Seleccione" or self.Permise == "Seleccione":
                self.newUser.warning.setText("¡No olvides seleccionar los desplegables!")
                
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.email):
                    self.newUser.warning.setText("¡El correo electrónico no es válido!")
                    
                else:
                    if len(self.Nombre)>45:
                        self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Nombres")
                        
                    else:
                        if len(self.Apellido)>45:
                            self.newUser.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Apellidos")
                            
                        else:
                            if len(self.Celular) != 9:
                                self.newUser.warning.setText("Numero de Telefono inválido")
                                
                            else:
                                password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
                                if not re.match(password_regex, self.passwordUser):
                                    self.newUser.warning.setText("¡La contraseña debe tener al menos 8 caracteres, incluir letras, números y al menos un carácter especial!")
                                
                                else:
                                    if len(self.UsuarioName)<5 or len(self.UsuarioName)>8:
                                        self.newUser.warning.setText("¡Nombre de Usuario inválido, no cumple los requerimientos!")
                                    else:
                                        if self.TipoDOC == "DNI":
                                            dni_regex = r'^\d{8}$'
                                            if not re.match(dni_regex, self.NumeroDNI):
                                                self.newUser.warning.setText("¡El DNI no es válido! Debe tener 8 dígitos")
                                            else:
                                                self.newUser.warning.setText("")
                                                self.ValidacionCorrecta()
                                
                                        elif self.TipoDOC == "CE":
                                            ce_regex = r'^[a-zA-Z0-9]{9}$'
                                            if not re.match(ce_regex, self.NumeroDNI):
                                                self.newUser.warning.setText("¡El Carnet de Extranjería no es válido! Debe tener 9 caracteres alfanuméricos.")
                                            else:
                                                self.newUser.warning.setText("")
                                                self.ValidacionCorrecta()       
                                    
                                
    def ValidacionCorrecta(self):
        #Cargado de Datos e Incio de La Clase UsuariosCLASS para el Ingreso de Datos en la BD
        DatosUsuario = Usuarios.UsuariosCLASS(self.UsuarioName, self.passwordUser, self.Nombre, self.Apellido, self.TipoDOC, self.NumeroDNI, self.Celular, self.email, self.Rol, self.Permise)
        DatosUsuario.Nuevo_Usuario()        
        
        #Registrado correctamente
        self.newUser.warning.setText("¡Registro exitoso!")