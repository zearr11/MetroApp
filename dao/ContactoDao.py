from util import ConexionBD


class ContactoBD:
    
    def ObtenerContactoID(self, telefono, correo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaContacto = "SELECT idContacto FROM contacto WHERE Telefono = '{}' AND Email = '{}'".format(telefono, correo)
        cursor.execute(ConsultaContacto)
        objContactoID = cursor.fetchone()
        objContacto = objContactoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objContacto
    
    def InsertTablaContacto(self, telefono, correo): 
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into CONTACTO(Telefono, Email) values ('{}', '{}')".format(telefono, correo)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        
        