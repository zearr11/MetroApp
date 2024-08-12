from PyQt5 import uic
from controller import MenuPrincipal
from dao import CategoriaDao, MedidaVentaDao, EstadoDao, ProductoDao
from model import ProductoModel
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import Qt


class RegProductosFRM:
    
    def __init__(self):
        self.newProduct = uic.loadUi("view/FRM_REG_PROD_NUEVO.ui")
        self.newProduct.setWindowTitle("Gestion de Productos")
        
        self.HideWidgets()
        self.ProductoDao = ProductoDao.ProductoBD()
        
        self.newProduct.tw_showProduct.cellClicked.connect(self.ClickTblProd)
        
        self.newProduct.bt_cancelar_prod.clicked.connect(self.CancelarProduct)
        self.newProduct.bt_nuevo_prod.clicked.connect(self.BtNuevo)
        self.newProduct.bt_mod.clicked.connect(self.BtModificar)
        self.newProduct.bt_guardar.clicked.connect(self.GuardadoProducto)
        self.newProduct.pb_actualizar.clicked.connect(self.SaveChangesProd)
        self.newProduct.show()
    
    
    #CARGADO DE WIDGETS
    def HideWidgets(self):
        self.newProduct.wd_reg_produ.hide()
        self.newProduct.wd_prod_mod.hide()
    
    def ShowWidget(self, prmtro):
        if prmtro == self.newProduct.wd_reg_produ:
            if self.newProduct.wd_reg_produ.isVisible():
                pass
            else:
                self.HideWidgets()
                prmtro.show()
                self.CargadoRegistro()
        else:
            if prmtro == self.newProduct.wd_prod_mod:
                if self.newProduct.wd_prod_mod.isVisible():
                    pass
                else:
                    self.HideWidgets()
                    prmtro.show()
                    self.CargadoMoficacion()
    
    def CargadoRegistro(self):
        self.newProduct.cb_cat_prod.clear()
        self.newProduct.cb_medida_prod.clear()
        self.newProduct.cb_state_prod.clear()
        #
        ConnectCategoria = CategoriaDao.CategoriaBD()
        ConnectMedidaVenta = MedidaVentaDao.MedidaVentaBD()
        ConnectEstado = EstadoDao.EstadoBD()
        #
        Categoria = ConnectCategoria.DataCategoria()
        MedidaVenta = ConnectMedidaVenta.DataMedidaVenta()
        Estado = ConnectEstado.DataEstado()
        #
        self.newProduct.cb_cat_prod.addItems(Categoria)
        self.newProduct.cb_medida_prod.addItems(MedidaVenta)
        self.newProduct.cb_state_prod.addItems(Estado)
        
    def CargadoMoficacion(self):
        self.newProduct.qc_categoria.clear()
        self.newProduct.qc_medida.clear()
        self.newProduct.qc_estado.clear()
        #
        ConnectCategoria = CategoriaDao.CategoriaBD()
        ConnectMedidaVenta = MedidaVentaDao.MedidaVentaBD()
        ConnectEstado = EstadoDao.EstadoBD()
        #
        Categoria = ConnectCategoria.DataCategoria()
        MedidaVenta = ConnectMedidaVenta.DataMedidaVenta()
        Estado = ConnectEstado.DataEstado()
        #
        self.newProduct.qc_categoria.addItems(Categoria)
        self.newProduct.qc_medida.addItems(MedidaVenta)
        self.newProduct.qc_estado.addItems(Estado)
        #
        self.ListarProductos()
        self.newProduct.tw_showProduct.resizeColumnsToContents()
        self.newProduct.tw_showProduct.setEditTriggers(QTableWidget.NoEditTriggers)
        self.BloquearTxtProd()
    
    #BOTONES DEL SISTEMA
    def CancelarProduct(self):
        self.newProduct.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def BtModificar(self):
        self.ShowWidget(self.newProduct.wd_prod_mod)
        
    def BtNuevo(self):
        self.ShowWidget(self.newProduct.wd_reg_produ)
 
    
    #################################################################################################
    #REGISTROS DE PRODUCTOS
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
        

    #################################################################################################
    #MODIFICACION DE PRODUCTOS
    
    def BloquearTxtProd(self):
        self.newProduct.le_descrip.setEnabled(False)
        self.newProduct.qc_medida.setEnabled(False)
        self.newProduct.qc_estado.setEnabled(False)
        self.newProduct.qc_categoria.setEnabled(False)
        self.newProduct.qc_marca.setEnabled(False)
        self.newProduct.qc_precio.setEnabled(False)
        self.newProduct.qc_cantidad.setEnabled(False)
        
    def ListarProductos(self):
        ListProducts = self.ProductoDao.ConsultaTablaProducto()
        Cantidad = len(ListProducts)
        self.newProduct.tw_showProduct.verticalHeader().setVisible(False)
        self.newProduct.tw_showProduct.setRowCount(Cantidad)
        Fila = 0
        for objUser in ListProducts:
            self.newProduct.tw_showProduct.setItem(Fila, 0, QTableWidgetItem(str(objUser[0])))
            self.newProduct.tw_showProduct.setItem(Fila, 1, QTableWidgetItem(objUser[1]))
            self.newProduct.tw_showProduct.setItem(Fila, 2, QTableWidgetItem(objUser[2]))
            self.newProduct.tw_showProduct.setItem(Fila, 3, QTableWidgetItem(objUser[3]))
            self.newProduct.tw_showProduct.setItem(Fila, 4, QTableWidgetItem(objUser[4]))
            self.newProduct.tw_showProduct.setItem(Fila, 5, QTableWidgetItem(objUser[5]))
            self.newProduct.tw_showProduct.setItem(Fila, 6, QTableWidgetItem(objUser[6]))
            self.newProduct.tw_showProduct.setItem(Fila, 7, QTableWidgetItem(str(objUser[7])))
            Fila +=1
        for row in range(self.newProduct.tw_showProduct.rowCount()):
            for column in range(self.newProduct.tw_showProduct.columnCount()):
                item = self.newProduct.tw_showProduct.item(row, column)
                if item:
                    item.setTextAlignment(Qt.AlignCenter)
                    
    def ClickTblProd(self, fila):
        idProd = self.newProduct.tw_showProduct.item(fila, 0).text()
        self.objProduct = self.ProductoDao.ObtenerProducto(idProd)
        self.newProduct.le_descrip.setText(self.objProduct[1])
        self.newProduct.le_descrip.setEnabled(True)
        self.newProduct.qc_marca.setText(self.objProduct[2])
        self.newProduct.qc_marca.setEnabled(True)
        self.newProduct.qc_medida.setCurrentText(self.objProduct[3])
        self.newProduct.qc_medida.setEnabled(True) 
        self.newProduct.qc_precio.setText(self.objProduct[4])
        self.newProduct.qc_precio.setEnabled(True)
        self.newProduct.qc_cantidad.setText(self.objProduct[5])
        self.newProduct.qc_cantidad.setEnabled(True)
        self.newProduct.qc_categoria.setCurrentText(self.objProduct[6])
        self.newProduct.qc_categoria.setEnabled(True)
        self.newProduct.qc_estado.setCurrentText(self.objProduct[7])
        self.newProduct.qc_estado.setEnabled(True)
        self.newProduct.warning_2.setText("")
        
    def SaveChangesProd(self):
        self.CambioDescripcion = self.newProduct.le_descrip.text()
        self.CambioMarca = self.newProduct.qc_marca.text()
        self.CambioPrecio = self.newProduct.qc_precio.text()
        self.CambioCantidad = self.newProduct.qc_cantidad.text()
        
        self.CambioMedida = self.newProduct.qc_medida.currentText()
        self.CambioEstado = self.newProduct.qc_estado.currentText()
        self.CambioCategoria = self.newProduct.qc_categoria.currentText()
        
        if self.newProduct.le_descrip.isEnabled():
            if len(self.CambioDescripcion) == 0 or len(self.CambioMarca) == 0 or len(self.CambioPrecio) == 0 or len(self.CambioCantidad) == 0:
                self.newProduct.warning_2.setText("Para actualizar los datos del Producto, ningun campo debe estar vacio")
            else:
                if self.CambioMedida == "Seleccione" or self.CambioEstado == "Seleccione" or self.CambioCategoria == "Seleccione":
                    self.newProduct.warning_2.setText("Selecciona un Item válido en los desplegables")
                else:
                    try:
                        float(self.CambioPrecio)
                    except ValueError:
                        self.newProduct.warning_2.setText("¡Error! El campo 'Precio' solo puede contener números")
                    else:
                        if len(self.CambioDescripcion) > 45:
                            self.newProduct.warning_2.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Descripcion'")
                        else:
                            if len(self.CambioMarca) > 45:
                                self.newProduct.warning_2.setText("¡Error! Solo se permiten hasta 45 caracteres en el campo 'Marca'")
                            else:
                                try:
                                    int(self.CambioCantidad)
                                except ValueError:
                                    self.newProduct.warning_2.setText("¡Error! El campo 'Cantidad' solo puede contener números enteros")
                                else:
                                    DataUpdateProducto = ProductoModel.ProductoCLASS(self.objProduct[1], self.objProduct[2], self.objProduct[5], self.objProduct[3], self.objProduct[4], self.objProduct[7], self.objProduct[6])
                                    DataUpdateProducto.Actualizar_Producto(self.CambioDescripcion, self.CambioMarca, self.CambioPrecio, self.CambioCantidad, self.CambioMedida, self.CambioEstado, self.CambioCategoria, self.objProduct[0])
                                    self.newProduct.warning_2.setText("¡Datos de Producto actualizados con éxito!")
                                    self.BloquearTxtProd()
                                    self.ListarProductos()
                                    self.newProduct.tw_showProduct.resizeColumnsToContents()
                                    self.newProduct.tw_showProduct.setEditTriggers(QTableWidget.NoEditTriggers)
        else:
            self.newProduct.warning_2.setText("¡Para modificar un producto, primero seleccionalo en la tabla!")
            