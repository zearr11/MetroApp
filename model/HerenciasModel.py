

#1
class ContactoCLASS:
    def __init__(self, Telefono, Email):
        self.__Telefono = Telefono
        self.__Email = Email
        
    #CAMBIAR DATOS 
    def set_Telefono(self, Telefono):
        self.__Telefono = Telefono
        
    def set_Email(self, email):
        self.__Email = email
    
    #OBTENER DATOS
    def get_Telefono(self):
        return self.__Telefono
    
    def get_Email(self):
        return self.__Email


#2
class TipoDocumentoCLASS:
    def __init__(self, TipoDoc):
        self.__TipoDoc = TipoDoc
        
    def set_TipoDoc(self, TipoDoc):
        self.__TipoDoc = TipoDoc
        
    def get_TipoDoc(self):
        return self.__TipoDoc
    
    
#3 
class NumeroDocumentoCLASS(TipoDocumentoCLASS):
    def __init__(self, NumeroDoc, TipoDoc):
        super().__init__(TipoDoc)
        self.__NumeroDoc = NumeroDoc
        
    def set_NumeroDoc(self, NumeroDoc):
        self.__NumeroDoc = NumeroDoc
        
    def get_NumeroDoc(self):
        return self.__NumeroDoc
  
    
#4
class CategoriaCLASS:
    def __init__(self, TipoCategoria):
        self.__TipoCategoria = TipoCategoria
    
    def set_TipoCategoria(self, TipoCategoria):
        self.__TipoCategoria = TipoCategoria
        
    def get_TipoCategoria(self):
        return self.__TipoCategoria
    
    
#5
class CargoCLASS:
    def __init__(self, TipoCargo):
        self.__TipoCargo = TipoCargo
        
    def set_TipoCargo(self, TipoCargo):
        self.__TipoCargo = TipoCargo

    def get_TipoCargo(self):
        return self.__TipoCargo


#6
class PermisosCLASS:
    def __init__(self, TipoPermiso):
        self.__TipoPermiso = TipoPermiso
        
    def set_TipoPermiso(self, TipoPermiso):
        self.__TipoPermiso = TipoPermiso

    def get_TipoPermiso(self):
        return self.__TipoPermiso


#7
class PersonaCLASS(ContactoCLASS, NumeroDocumentoCLASS):
    def __init__(self, Nombres, Apellidos, Telefono, Email, NumeroDoc, TipoDoc):
        super().__init__(Telefono, Email)
        NumeroDocumentoCLASS.__init__(self, NumeroDoc, TipoDoc)
        self.__Nombres = Nombres
        self.__Apellidos = Apellidos
        
    #CAMBIAR DATOS:
    def set_Nombres(self, Nombres):
        self.__Nombres = Nombres
        
    def set_Apellidos(self, Apellidos):
        self.__Apellidos = Apellidos
        
    #OBTENER DATOS
    def get_Nombres(self):
        return self.__Nombres
        
    def get_Apellidos(self):
        return self.__Apellidos
    

#8
class MedioPagoCLASS:
    def __init__(self, TipoPago):
        self.__TipoPago = TipoPago
        
    def set_TipoPago(self, TipoPago):
        self.__TipoPago = TipoPago
        
    def get_TipoPago(self):
        return self.__TipoPago
    
    
#9
class EstadoCLASS:
    def __init__(self, Estado):
        self.__Estado = Estado
        
    def set_Estado(self, Estado):
        self.__Estado = Estado
        
    def get_Estado(self):
        return self.__Estado


#10
class MedidaVentaCLASS:
    def __init__(self, MedidaVenta):
        self.__MedidaVenta = MedidaVenta
        
    def set_MedidaVenta(self, MedidaVenta):
        self.__MedidaVenta = MedidaVenta
        
    def get_MedidaVenta(self):
        return self.__MedidaVenta
    
