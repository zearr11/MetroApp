from util import ConexionBD


class ContactoBD:
    
    def ObtenerContactoID(self, Telefono, Email):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaContacto = "SELECT idContacto FROM contacto WHERE Telefono = '{}' AND Email = '{}'".format(Telefono, Email)
        cursor.execute(ConsultaContacto)
        objContactoID = cursor.fetchone()
        objContacto = objContactoID[0]
        return objContacto
    
    def InsertTablaContacto(self, Telefono, Email): 
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into contacto(Telefono, Email) values ('{}', '{}')".format(Telefono, Email)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def UpdateContacto(self, Telefono, Email, idContacto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE contacto SET Telefono = '{}', Email ='{}' WHERE idContacto = '{}'".format(Telefono, Email, idContacto)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
        
        