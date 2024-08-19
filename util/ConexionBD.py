import mysql.connector
from datetime import datetime
import subprocess
import os

class ConectBaseData:
    def __init__(self):
        self.conexionBD = mysql.connector.connect(user="root",
                                     password="123456",
                                     host="localhost",
                                     database="mydb",
                                     port="3306")
        
    def GenBackUp(self):
        self.usuario = self.conexionBD.user
        self.password = self.conexionBD._password
        self.host = self.conexionBD._host
        self.bd = self.conexionBD.database
        
        backUnico = datetime.now().strftime("%Y%m%d_%H%M%S")
        rutabup = f"backUpsBD/backup_{backUnico}.sql"
         
        query = f"mysqldump -u {self.usuario} -p{self.password} -h {self.host} {self.bd} > {rutabup}"
        
        try:
            subprocess.run(query, shell=True, check=True)
        except:
            return False
        else:
            return True
        
    def RestoreBD(self, nbackup):
        self.usuario = self.conexionBD.user
        self.password = self.conexionBD._password
        self.host = self.conexionBD._host
        self.bd = self.conexionBD.database
        
        ArchRestore = f"backUpsBD/{nbackup}"
        self.puerto = self.conexionBD._port
        
        print(ArchRestore)
        
        query = f'mysql -u {self.usuario} -p{self.password} -h {self.host} -P {self.puerto} {self.bd} < {ArchRestore}'
        
        try:
            os.system(query)
        except:
            return False
        else:
            return True
        