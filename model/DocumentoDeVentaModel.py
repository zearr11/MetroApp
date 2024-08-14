from model.TipoDocVentaModel import TipoDocVentaCLASS

class DocumentoDeVentaCLASS(TipoDocVentaCLASS):
    def __init__(self, TipoDocVenta, NumeroDocumento, SubTotal, IGV, TotalT):
        super().__init__(TipoDocVenta)
        self.__NumeroDocumento = NumeroDocumento
        self.__SubTotal = SubTotal
        self.__IGV = IGV
        self.__TotalT = TotalT
        
    def get_NumeroDocumento(self):
        return self.__NumeroDocumento  
    
    def get_SubTotal(self):
        return self.__SubTotal 

    def get_IGV(self):
        return self.__IGV
    
    def get_TotalT(self):
        return self.__TotalT
    