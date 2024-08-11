from PyQt5 import uic
from controller import MenuPrincipal
from dao import CategoriaDao, MedidaVentaDao, EstadoDao
from model import ProductoModel


class RegProductosFRM:
    
    def __init__(self):
        self.newProduct = uic.loadUi("view/FRM_REG_PROD_NUEVO.ui")
        self.newProduct.setWindowTitle("Gestion de Productos")
        
        self.HideWidgets()
        
        
        ConnectCategoria = CategoriaDao.CategoriaBD()
        ConnectMedidaVenta = MedidaVentaDao.MedidaVentaBD()
        ConnectEstado = EstadoDao.EstadoBD()
        Categoria = ConnectCategoria.DataCategoria()
        MedidaVenta = ConnectMedidaVenta.DataMedidaVenta()
        Estado = ConnectEstado.DataEstado()
        self.newProduct.cb_cat_prod.addItems(Categoria)
        self.newProduct.cb_medida_prod.addItems(MedidaVenta)
        self.newProduct.cb_state_prod.addItems(Estado)
        
        self.newProduct.bt_cancelar_prod.clicked.connect(self.CancelarProduct)
        self.newProduct.bt_nuevo_prod.clicked.connect(self.BtNuevo)
        self.newProduct.bt_mod.clicked.connect(self.BtModificar)
        self.newProduct.bt_guardar.clicked.connect(self.GuardadoProducto)
        self.newProduct.show()
    
    #BotonesSistema
    def CancelarProduct(self):
        self.newProduct.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def HideWidgets(self):
        self.newProduct.wd_reg_produ.hide()
        self.newProduct.wd_prod_mod.hide()
    
    def ShowWidget(self, prmtro):
        self.HideWidgets()
        prmtro.show()
        
    def BtModificar(self):
        self.ShowWidget(self.newProduct.wd_prod_mod)
        
    def BtNuevo(self):
        self.ShowWidget(self.newProduct.wd_reg_produ)
    #
    
    #
    def GuardadoProducto(self):
        self.ValidacionProd()
    
    def ValidacionProd(self):
        self.Descripcion = self.newProduct.le_descrip_prod.text()
        self.MarcaProd = self.newProduct.le_marca_prod.text()
        self.CantidadAlmacen = self.newProduct.le_stk.text()
        self.PrecioProd = self.newProduct.le_prec_prod.text()
        
        self.Categoria = self.newProduct.cb_cat_prod.currentText()
        self.Medida = self.newProduct.cb_medida_prod.currentText()
        self.EstadoProd = self.newProduct.cb_state_prod.currentText()
        
        if len(self.Descripcion) == 0 or len(self.MarcaProd) == 0 or len(self.CantidadAlmacen) == 0 or len(self.PrecioProd) == 0:
            self.newProduct.warning_1.setText("¡Ningun campo debe estar vacio!")
        else:
            if self.Categoria == "Seleccione" or self.Medida == "Seleccione" or self.EstadoProd == "Seleccione":
                self.newProduct.warning_1.setText("¡No olvides seleccionar los desplegables!")
            else:
                try:
                    float(self.PrecioProd)
                except ValueError:
                    self.newProduct.warning_1.setText("¡Error! El campo 'Precio' debe contener solo números")
                else:
                    if len(self.Descripcion) > 45:
                        self.newProduct.warning_1.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Descripcion'")
                    else:
                        if len(self.MarcaProd) > 45:
                            self.newProduct.warning_1.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Marca'")
                        else:
                            try:
                                int(self.CantidadAlmacen)
                            except ValueError:
                                self.newProduct.warning_1.setText("¡Error! El campo 'Cantidad' debe contener solo números enteros")
                            else:
                                self.ValidacionProdCorrecta()
                                
    def ValidacionProdCorrecta(self):
        objProducto = ProductoModel.ProductoCLASS(self.Descripcion, self.MarcaProd, self.CantidadAlmacen, self.Medida, self.PrecioProd, self.EstadoProd, self.Categoria)
        objProducto.Nuevo_Producto()
        self.newProduct.warning_1.setText("¡Registro Exitoso!")