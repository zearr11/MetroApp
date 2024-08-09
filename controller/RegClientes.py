from PyQt5 import uic
from controller import MenuPrincipal
from dao import RegistroUserDao
import re
class RegClientes:
    
    def __init__(self):
        self.newCient = uic.loadUi("view/FRM_REG_CLIENT.ui")
        self.newCient.setWindowTitle("Gestion de Clientes")
        
        self.Conexion = RegistroUserDao.RegUserDB()
        Documentos = self.Conexion.DataDocumentos()
        self.newCient.cb_tipoDNI_client.addItems(Documentos)
        
        self.newCient.bt_guardar_cl.clicked.connect(self.GuardadoCliente)
        
        self.newCient.bt_cancelar_cl.clicked.connect(self.CancelarClient)
        self.newCient.show()
        
    def CancelarClient(self):
        self.newCient.close()
        self.menu = MenuPrincipal.Menu()
        
    def GuardadoCliente(self):
        self.ValidacionDataCliente()
        
    def ValidacionDataCliente(self):
        self.Nombre = self.newCient.le_name_client.text()
        self.Apellido = self.newCient.le_lastname_client.text()
        self.NumeroDoc = self.newCient.le_dni_client.text()
        self.Direccion = self.newCient.le_direcc_client.text()
        self.Telefono = self.newCient.le_telf_client.text()
        self.Email = self.newCient.le_email_client.text()
        
        self.TipoDOC = self.newCient.cb_tipoDNI_client.currentText()
        
        if len(self.Nombre) == 0 or len(self.Apellido) == 0 or len(self.NumeroDoc) == 0 or len(self.Direccion) == 0 or len(self.Telefono) == 0 or len(self.Email) == 0:
            self.newCient.warning.setText("¡Ningun campo debe estar vacio!")
            print("ELPEPE")
        else:
            if self.TipoDOC == "Seleccione":
                self.newCient.warning.setText("¡Selecciona el Tipo de Documento!")
                print("etesech")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.Email):
                    self.newCient.warning.setText("¡El correo electrónico no es válido!")
                    
                else:
                    if len(self.Nombre)>45:
                        self.newCient.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Nombres")
                        
                    else:
                        if len(self.Apellido)>45:
                            self.newCient.warning.setText("¡Error! Solo se permiten hasta 45 caracteres en Apellidos")
                            
                        else:
                            if len(self.Telefono) != 9:
                                self.newCient.warning.setText("Numero de Telefono inválido")
                                
                            else:
                                if self.TipoDOC == "DNI":
                                    dni_regex = r'^\d{8}$'
                                    if not re.match(dni_regex, self.NumeroDoc):
                                        self.newCient.warning.setText("¡El DNI no es válido! Debe tener 8 dígitos")
                                    else:
                                        self.newCient.warning.setText("")
                                        #self.ValidacionClCorrecta()
                                
                                elif self.TipoDOC == "CE":
                                    ce_regex = r'^[a-zA-Z0-9]{9}$'
                                    if not re.match(ce_regex, self.NumeroDoc):
                                        self.newCient.warning.setText("¡El Carnet de Extranjería no es válido! Debe tener 9 caracteres alfanuméricos.")
                                    else:
                                        self.newCient.warning.setText("")
                                        #self.ValidacionClCorrecta()
    
    def ValidacionClCorrecta(self):
        IdDoc = self.Conexion.ObtenerDocumentoID(self.TipoDOC)
        
        self.Conexion.InsertTablaContacto(self.Telefono, self.Email)
        idContac = self.Conexion.ObtenerContactoID(self.Telefono, self.Email)
        
        self.Conexion.InsertTablaPersona(self.Nombre, self.Apellido, self.NumeroDoc, IdDoc, idContac)
        idPersona = self.Conexion.ObtenerPersonaID(self.Nombre, self.Apellido, self.NumeroDoc, IdDoc, idContac)
        
        self.Conexion.InsertTablaCliente(self.Direccion, idPersona, IdDoc, idContac)
        
        self.newCient.warning.setText("¡Registro exitoso!")