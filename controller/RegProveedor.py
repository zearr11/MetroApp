from PyQt5 import uic
from controller import MenuPrincipal
from dao import RubroDao
from model import Proveedor
import re


class RegProveedorFRM:
    
    def __init__(self):
        self.newProv = uic.loadUi("view/FRM_REG_PROVE.ui")
        self.newProv.setWindowTitle("Gestion de Proveedores")
        
        ConnectRubroDao = RubroDao.RubroBD()
        Rubro = ConnectRubroDao.DataRubro()
        self.newProv.cb_rubro_prov.addItems(Rubro)
        
        self.newProv.bt_cancelar_prov.clicked.connect(self.CancelarProv)
        self.newProv.bt_guardar_prov.clicked.connect(self.GuardarProv)
        self.newProv.show()
        
        
    def CancelarProv(self):
        self.newProv.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def GuardarProv(self):
        self.ValidacionProvDatos()
        
    def ValidacionProvDatos(self):
        self.RazonSocial = self.newProv.le_razon_soc.text()
        self.RUC = self.newProv.le_ruc.text()
        self.Direccion = self.newProv.le_direcc_prov.text()
        self.Telefono = self.newProv.le_telf_prov.text()
        self.Email = self.newProv.le_email_prov.text()
        self.Rubro = self.newProv.cb_rubro_prov.currentText()
        
        #Validacion de Datos
        if len(self.RazonSocial) == 0 or len(self.RUC) == 0 or len(self.Direccion) == 0 or len(self.Telefono) == 0 or len(self.Email) == 0:
            self.newProv.warning.setText("¡Ningun campo debe estar vacio!")
            
        else:
            if self.Rubro == "Seleccione":
                self.newProv.warning.setText("¡Selecciona el Rubro correspondiente!")
                
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, self.Email):
                    self.newProv.warning.setText("¡El correo electrónico no es válido!")
                    
                else:
                    if len(self.Telefono) != 9:
                        self.newProv.warning.setText("¡Numero de Telefono inválido!")
                        
                    else:
                        if len(self.RUC) != 11:
                            self.newProv.warning.setText("¡Ruc Invalido!")
                        
                        else:
                            self.newProv.warning.setText("")
                            self.ValidacionCorrecta()
                            
                        
    def ValidacionCorrecta(self):
        DatosProveedor = Proveedor.ProveedorCLASS(self.RazonSocial, self.Rubro, self.RUC, self.Direccion, self.Telefono, self.Email)
        DatosProveedor.Nuevo_Proveedor()
        
        #Registrado correctamente
        self.newProv.warning.setText("¡Registro exitoso!")