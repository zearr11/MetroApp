from PyQt5 import uic
from controller import MenuPrincipal
from dao import CompraDao, DetalleCompraDao, GuiaEntradaDao, ProductoDao
from datetime import datetime


class GuiaEntradaFRM:
    
    def __init__(self):
        self.guiaetd = uic.loadUi("view/FRM_GUIA_ENTRADA.ui")
        self.guiaetd.setWindowTitle("Guia de Entrada") 
        
        self.guiaetd.ventana2.hide()
        
        #Asignacion de Datos a ComboBox de Ventana 1
        self.ConexionCompraDao = CompraDao.CompraBD()
        self.ConexionGuiaEntradaDao = GuiaEntradaDao.GuiaEntradaBD()
        self.ConexionProductoDao = ProductoDao.ProductoBD()
        DataIdCompras = self.ConexionCompraDao.ObtenerIDsAllCompras()
        self.DataIdComprasSTR = [str(id) for id in DataIdCompras] 
        self.guiaetd.cb_cod_guias.addItems(self.DataIdComprasSTR)
        self.guiaetd.cb_cod_guias.setCurrentText("")
        
        self.guiaetd.btCancelar1.clicked.connect(self.BtCancelarFRM1)
        self.guiaetd.bt_reg_ingreso.clicked.connect(self.btRegIngresoFRM1)
        
        self.guiaetd.siguiente_bt.clicked.connect(self.BtNextFRM2)
        self.guiaetd.bt_cancelar2.clicked.connect(self.BtCancelarFRM2)
        self.guiaetd.bt_finish.clicked.connect(self.BtFinish)
        
        self.guiaetd.show()       
    
    #####################################################################
    #Botones Iniciales FMR1
     
    def BtCancelarFRM1(self):
        self.guiaetd.close()
        self.menu = MenuPrincipal.MenuFRM()
        
    def btRegIngresoFRM1(self):
        self.CodigoGuiaInput = self.guiaetd.cb_cod_guias.currentText()
        if len(self.CodigoGuiaInput) == 0:
            self.guiaetd.warningFRM1.setText("¡Ingresa un codigo de guía!")
        else:
            if self.CodigoGuiaInput not in self.DataIdComprasSTR:
                self.guiaetd.warningFRM1.setText("Codigo de Guia no encontrado")
            else:
                self.guiaetd.warningFRM1.setText("")
                self.guiaetd.ventana1.hide()
                self.guiaetd.ventana2.show()
                self.CargadoInterfaz2()
                
        
    #####################################################################
    #Inicio y Cargado de FRM2
    
    def CargadoInterfaz2(self):
        self.guiaetd.bt_finish.hide()
        self.alteradorProd = 0
        self.alteradorCant = 0
        #
        self.ConexionDetalleCompraDao = DetalleCompraDao.DetalleCompraBD()
        self.ProdCompr = self.ConexionDetalleCompraDao.ObtenerAllProdDescYCant(self.CodigoGuiaInput)
        #
        self.C = 0
        self.LstProd = []
        self.LstCant = []
        #
        self.Altenate = []
        self.Observacion = []
        #
        for i in range(len(self.ProdCompr)):
            va = self.ProdCompr[i]
            self.LstProd.append(va[0])
            self.LstCant.append(va[1])
        #
        self.guiaetd.cod_guia.setText(self.CodigoGuiaInput)
        self.CambiaProductos()
    
    def CambiaProductos(self):
        self.guiaetd.prod_m.setText(self.LstProd [self.alteradorProd])
        self.guiaetd.cant_m.setText(self.LstCant[self.alteradorCant])
        if len(self.ProdCompr) == 1:
            self.guiaetd.bt_finish.show()
            self.guiaetd.siguiente_bt.hide()
        else:
            if self.alteradorProd == len(self.ProdCompr)-1:
                self.guiaetd.bt_finish.show()
                self.guiaetd.siguiente_bt.hide()
                self.ReseteoRadioButton()
    #    
    def BtNextFRM2(self):
        if self.alteradorProd >= len(self.ProdCompr)-1:
            self.guiaetd.warning_GUIA.setText("")
            pass
        else:
            if self.ComprobadorYGuardado() == True:
                self.guiaetd.warning_GUIA.setText("")
                self.alteradorProd +=1
                self.alteradorCant +=1
                self.CambiaProductos()
                self.ReseteoRadioButton()
            
    def BtCancelarFRM2(self):
        self.BtCancelarFRM1()
        
    def BtFinish(self):
        if len(self.ProdCompr) == 1:
            self.ComprobadorYGuardado()
            if len(self.Altenate) > 0:
                self.guiaetd.warning_GUIA.setText("")
                self.BloqueoRadioButton()
                self.guiaetd.bt_finish.setEnabled(False)
                self.FinalizadorReg()
                self.guiaetd.warning_GUIA.setText("")
                self.guiaetd.warning_GUIA.setText("Registro de Entrada Guardado con Éxito")
        else:
            if self.alteradorProd == len(self.ProdCompr)-1:
                self.ComprobadorYGuardado()
                if len(self.Altenate) == len(self.ProdCompr):
                    self.guiaetd.warning_GUIA.setText("")
                    self.BloqueoRadioButton()
                    self.guiaetd.bt_finish.setEnabled(False)
                    self.FinalizadorReg()
                    self.guiaetd.warning_GUIA.setText("Registro de Entrada Guardado con Éxito")
                    
                
    def ReseteoRadioButton(self):
        self.guiaetd.rb_si.setAutoExclusive(False)
        self.guiaetd.rb_no.setAutoExclusive(False)

        self.guiaetd.rb_si.setChecked(False)
        self.guiaetd.rb_no.setChecked(False)
    
        self.guiaetd.rb_si.setAutoExclusive(True)
        self.guiaetd.rb_no.setAutoExclusive(True)
        
    def BloqueoRadioButton(self):
        self.ReseteoRadioButton()
        self.guiaetd.rb_si.setEnabled(False)
        self.guiaetd.rb_no.setEnabled(False)
                
    #
    def ComprobadorYGuardado(self):
        if self.guiaetd.rb_si.isChecked() == True and len(self.ProdCompr)-1 == self.alteradorProd and self.C == 0:
            self.Altenate.append("Si")
            self.C = 1
            return False
        else:
            if self.guiaetd.rb_no.isChecked() == True and len(self.ProdCompr)-1 == self.alteradorProd and self.C == 0:
                self.Altenate.append("No")
                self.C = 1
                return False
            else:
                if self.guiaetd.rb_no.isChecked() == False and self.guiaetd.rb_si.isChecked() == False:
                    self.guiaetd.warning_GUIA.setText("¡Indica si el producto fue recibido!") 
                    return False
                else:
                    if self.guiaetd.rb_si.isChecked()== True and self.C == 0:
                        self.Altenate.append("Si")
                        return True
                    else:
                        if self.guiaetd.rb_no.isChecked()== True and self.C == 0:
                            self.Altenate.append("No")
                            return True
                        
    def FinalizadorReg(self):
        
        #Recepcion es = self.Altenate[k]
        self.LstDetalleCompraTup = self.ConexionDetalleCompraDao.ObtenerIDdetalleCompras(self.CodigoGuiaInput) #idDetalleCompra Lista
        self.LstIDproductsTup = self.ConexionDetalleCompraDao.ObtenerIDAllProductosCompras(self.CodigoGuiaInput) #idProductos Lista
        #idCompra es = self.CodigoGuiaInput
        self.LstDetalleCompra = [item[0] for item in self.LstDetalleCompraTup]
        self.LstIDproducts = [item[0] for item in self.LstIDproductsTup]
        
        #print(self.LstDetalleCompra)
        #print(self.LstIDproducts)
        #print(self.CodigoGuiaInput)
        
        #Fecha de Recepcion
        actual = datetime.now()
        FechaRecepcion = actual.date()
        
        for k in range(len(self.ProdCompr)):
            self.ConexionGuiaEntradaDao.InsertTablaGuiaEntrada(FechaRecepcion, self.Altenate[k], self.LstDetalleCompra[k], self.LstIDproducts[k], self.CodigoGuiaInput)
        
        for l in range(len(self.ProdCompr)):
            CantidadProd = self.ConexionProductoDao.ObtenerCantidadProd(self.LstIDproducts[l])
            CantidadPedProd = self.ConexionDetalleCompraDao.ObtenerCantidadAumentada(self.LstDetalleCompra[l], self.LstIDproducts[l], self.CodigoGuiaInput)
            Aumento = int(CantidadProd) + int(CantidadPedProd)
            
            if self.Altenate[l] == "Si":
                self.ConexionProductoDao.UpdateCantProd(Aumento, self.LstIDproducts[l])
            else:
                pass
                
            
        NewEstado = "Atendido"
        self.ConexionCompraDao.UpdateEstadoCompra(NewEstado, self.CodigoGuiaInput)
        
        