from model.UsuariosModel import UsuariosCLASS
from dao import LoginDao

class LogUsersModelCLASS(UsuariosCLASS):
    
    def __init__(self, idUser):
        super().__init__(idUser)
        
    def LogsEnAppInsert(self):
        IdUserLog = self.get_NombUser()
        
        CLog = LoginDao.LoginBD()
        CLog.InsertTablaLog(IdUserLog)
        
        