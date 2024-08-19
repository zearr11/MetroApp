from PyQt5 import uic
from util import ConexionBD
from PyQt5.QtWidgets import QFileSystemModel
from controller import MenuPrincipal


class RestaurarBD:
    
    def __init__(self):
        self.restore = uic.loadUi("view/FRM_RESTORE_BD.ui")
        self.restore.setWindowTitle("Restaurar la Base de Datos")
        self.bdconexion = ConexionBD.ConectBaseData()
        
        # Asignacion de Botones
        self.restore.btRegresar.clicked.connect(self.CancelarRestauracion)
        self.restore.btRestaurar.clicked.connect(self.RestaurarBD)
        
        self.arch = QFileSystemModel()
        Rt = "backUpsBD/"
        self.arch.setRootPath(Rt)
        
        self.restore.lst_vw.setModel(self.arch)
        self.restore.lst_vw.setRootIndex(self.arch.index(Rt))
        self.restore.lst_vw.selectionModel().selectionChanged.connect(self.Seleccion)
        
        self.restore.show()
        
    def CancelarRestauracion(self):
        self.restore.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def Seleccion(self):
        # Obtener los índices seleccionados
        SeleccionIndices = self.restore.lst_vw.selectionModel().selectedIndexes()
        
        if SeleccionIndices:
            Indice = SeleccionIndices[0]
            NameArchivo = self.arch.fileName(Indice)
            return NameArchivo
        else:
            return False
        
    def RestaurarBD(self):
        if self.Seleccion() is False:
            self.restore.warning.setText("¡Selecciona el BackUp a Restaurar!")
        else:
            if self.Seleccion() is not False:
                NameArchivo = self.Seleccion()
                self.restore.warning.setText("")
                c = self.bdconexion.RestoreBD(NameArchivo)

                if c is True:
                    self.restore.warning.setText("¡Restauración realizada con éxito!")
                else:
                    if c is False:
                        self.restore.warning.setText("¡Error! No se pudo restaurar")
