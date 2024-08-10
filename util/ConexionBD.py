import mysql.connector

class ConectBaseData:
    def __init__(self):
        self.conexionBD = mysql.connector.connect(user="root",
                                     password="123456",
                                     host="localhost",
                                     database="mydb",
                                     port="3306")
        