from model.HerenciasModel import MedioPagoCLASS
from model.UsuariosModel import UsuariosCLASS
from model.ClientesModel import ClienteCLASS
from model.DocumentoDeVentaModel import DocumentoDeVentaCLASS

class VentaCLASS(MedioPagoCLASS, UsuariosCLASS, ClienteCLASS, DocumentoDeVentaCLASS):
    
    def __init__(self, idUser, idCliente, TipoPago, NumeroDocVent):
        super().__init__(TipoPago)
        UsuariosCLASS.__init__(self, idUser)
        ClienteCLASS.__init__(self, idCliente)
        DocumentoDeVentaCLASS.__init__(self, NumeroDocumento=NumeroDocVent)
        