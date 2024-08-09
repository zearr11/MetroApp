from PyQt5 import uic
from controller import Login, PoliticasSeguridad, RegClientes, RegProductos, RegVenta, RegProveedor, GenPedCompra


class MenuFRM:
    
    def __init__(self):
        self.menu = uic.loadUi("view/FRM_MEN_PRINCIPAL.ui")
        self.menu.setWindowTitle("Menu Principal")
        
        #Funcion de botones con derivacion a FRM
        self.menu.vent_1.clicked.connect(self.acceso_reg_clientes)
        self.menu.vent_2.clicked.connect(self.acceso_reg_produc)
        self.menu.vent_3.clicked.connect(self.acceso_reg_vent)
        
        self.menu.compr_1.clicked.connect(self.acceso_reg_prov)
        self.menu.compr_2.clicked.connect(self.acceso_gen_pedcompr)
        
        self.menu.segur_1.clicked.connect(self.acceso_pol_seguridad)
        self.menu.bt_cerrar_sesion.clicked.connect(self.cierre_sesion)
        
        #Funcion de botones sin derivacion
        self.menu.bt_ingreso_ventas.clicked.connect(self.ingreso_ventas)
        self.menu.bt_ingreso_compras.clicked.connect(self.ingreso_compras)
        self.menu.bt_ingreso_almacen.clicked.connect(self.ingreso_almacen)
        self.menu.bt_ingreso_reportes.clicked.connect(self.ingreso_reportes)
        self.menu.bt_ingreso_seguridad.clicked.connect(self.ingreso_seguridad)
        
        #Ocultacion de SubMenus e Inicio de Menu
        self.HideWidgets()
        self.menu.show()
    
    
    #Gestion Menu Principal
    def HideWidgets(self):
        self.menu.accion_almacen.hide()
        self.menu.accion_compras.hide()
        self.menu.accion_reportes.hide()
        self.menu.accion_seguridad.hide()
        self.menu.accion_ventas.hide()
        
    def ShowWidget(self, widget):
        self.HideWidgets()
        widget.show()
        
    def ingreso_ventas(self):
        self.ShowWidget(self.menu.accion_ventas)
        
    def ingreso_compras(self):
        self.ShowWidget(self.menu.accion_compras)
        
    def ingreso_almacen(self):
        self.ShowWidget(self.menu.accion_almacen)
        
    def ingreso_reportes(self):
        self.ShowWidget(self.menu.accion_reportes)
        
    def ingreso_seguridad(self):
        self.ShowWidget(self.menu.accion_seguridad)
    
    
    #Gestion Acceso a Otros FRM
    
    #BOTON ingreso_ventas:
    def acceso_reg_clientes(self):
        self.menu.close()
        self.newCient = RegClientes.RegClientesFRM()
    def acceso_reg_produc(self):
        self.menu.close()
        self.newProduct = RegProductos.RegProductosFRM()
    def acceso_reg_vent(self):
        self.menu.close()
        self.newVenta = RegVenta.RegVentaFRM()
        
    #BOTON ingreso_compras: 
    def acceso_reg_prov(self):
        self.menu.close()
        self.newProv = RegProveedor.RegProveedorFRM()

    def acceso_gen_pedcompr(self):
        self.menu.close()
        self.newPedCompr = GenPedCompra.GenPedCompraFRM()
    
    #BOTON ingreso_almacen: 
    
    
    #BOTON ingreso_reportes: 
    
    
    #BOTON ingreso_seguridad: 
    def acceso_pol_seguridad(self):
        self.menu.close()
        self.poli = PoliticasSeguridad.PoliticasSeguridadFRM()
        
    
    def cierre_sesion(self):
        self.menu.close()
        self.log = Login.LoginFRM()