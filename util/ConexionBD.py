import mysql.connector
from datetime import datetime
import subprocess

class ConectBaseData:
    def __init__(self):
        self.conexionBD = mysql.connector.connect(user="root",
                                     password="123456",
                                     host="localhost",
                                     database="mydb",
                                     port="3306")
        
    def GenBackUp(self):
        usuario = self.conexionBD.user
        password = self.conexionBD._password
        host = self.conexionBD._host
        bd = self.conexionBD.database
        
        backUnico = datetime.now().strftime("%Y%m%d_%H%M%S")
        rutabup = f"backUpsBD/backup_{backUnico}.sql" 
        query = f"mysqldump -u {usuario} -p{password} -h {host} {bd} > {rutabup}"
        
        try:
            subprocess.run(query, shell=True, check=True)
        except:
            return False
        else:
            return True