from PyQt5 import uic
from controller import MenuPrincipal
from dao import CategoriaDao
from model import ProveedorModel
import re


class RegProveedorFRM:
    
    def __init__(self):
        self.newProv = uic.loadUi("view/FRM_REG_PROVE.ui")
        self.newProv.setWindowTitle("Gestion de Proveedores")
        
        #Cargado de Dao en ComboBox
        ConnectCategoriaDao = CategoriaDao.CategoriaBD()
        Categoria = ConnectCategoriaDao.DataCategoria()
        self.newProv.cb_rubro_prov.addItems(Categoria)
        
        self.newProv.bt_cancelar_prov.clicked.connect(self.CancelarProv)
        self.newProv.bt_guardar_prov.clicked.connect(self.GuardarProv)
        self.newProv.show()
        
    def CancelarProv(self):
        self.newProv.close()
        self.menu = MenuPrincipal.MenuFRM()
        
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
        
        
        
    