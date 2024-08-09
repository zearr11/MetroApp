
#1
class DatosCLASS:
    def __init__(self, telefono, email):
        self.__telefono = telefono
        self.__email = email
        
    #CAMBIAR DATOS 
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    def set_email(self, email):
        self.__email = email
    
    #OBTENER DATOS
    def get_telefono(self):
        return self.__telefono
    
    def get_email(self):
        return self.__email


#2
class TipoDOC_CLASS:
    def __init__(self, TypeDoc):
        self.__tipoDoc = TypeDoc
        
    def get_tipo_doc(self):
        return self.__tipoDoc
  
    
#3
class Rubro_CLASS:
    def __init__(self, TipoRubro):
        self.__TipoRubro = TipoRubro
        
    def get_TipoRubro(self):
        return self.__TipoRubro


#4
class PersonaCLASS(DatosCLASS, TipoDOC_CLASS):
    def __init__(self, Nombres, Apellidos, TypeDoc, Num_doc, telefono, email):
        super().__init__(telefono, email)
        TipoDOC_CLASS.__init__(self, TypeDoc)
        self.__nombresPer = Nombres
        self.__apellidosPer = Apellidos
        self.__num_docPer = Num_doc
        
    #CAMBIAR DATOS:
    def set_nombres(self, nombres):
        self.__nombresPer = nombres
        
    def set_apellidos(self, apellidos):
        self.__apellidosPer = apellidos
        
    def set_num_doc(self, num_doc):
        self.__num_docPer = num_doc
        
        
    #OBTENER DATOS
    def get_nombres(self):
        return self.__nombresPer
        
    def get_apellidos(self):
        return self.__apellidosPer
        
    def get_num_doc(self):
        return self.__num_docPer
    
    
    
    

