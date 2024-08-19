from PyQt5 import uic
from controller import MenuPrincipal
from util import ConexionBD


class GenBackUpFRM:
    
    def __init__(self):
        self.backup = uic.loadUi("view/FRM_BACK_UP_BD.ui")
        self.backup.setWindowTitle("Generar BackUp de la Base de Datos")
        self.BDcon = ConexionBD.ConectBaseData()
        
        #Asignacion a los Botones
        self.backup.btGenerar.clicked.connect(self.BtGenBackUp)
        self.backup.btCancelar.clicked.connect(self.BtCancelAccion) 
        
        self.backup.show()
        
    #Programacion de Botones:
    def BtGenBackUp(self):
        c = self.BDcon.GenBackUp()
        
        if c is True:
            self.backup.warning.setText("¡Back Up realizado con éxito!")
        else:
            if c is False:
                self.backup.warning.setText("¡Error! No se pudo hacer el BackUp")
    
    def BtCancelAccion(self):
        self.backup.close()
        self.menu = MenuPrincipal.MenuFRM()