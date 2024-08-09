from util import ConexionBD

class RegUserDB:
    
    def DataCargo(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoCargo FROM cargo")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]
    
    def DataPermisos(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoPermiso FROM permisos")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]
    
    def DataDocumentos(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT TipoDoc FROM documento")
        rows = cursor.fetchall()
        cursor.close()
        nbd.CloseConexion()
        return [row[0] for row in rows]

    def ObtenerDocumentoID(self, tipoDOC):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaDOC = "SELECT idDocumento FROM documento WHERE TipoDoc = '{}'".format(tipoDOC)
        cursor.execute(ConsultaDOC)
        objDocumentoID = cursor.fetchone()
        objDocumento = objDocumentoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objDocumento

    def ObtenerCargoID(self, cargo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaCargo = "SELECT idCargo FROM cargo WHERE TipoCargo = '{}'".format(cargo)
        cursor.execute(ConsultaCargo)
        objCargoID = cursor.fetchone()
        objCargo = objCargoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objCargo
        
    def ObtenerPermisoID(self, permiso):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPermiso = "SELECT idPermisos FROM permisos WHERE TipoPermiso = '{}'".format(permiso)
        cursor.execute(ConsultaPermiso)
        objPermisoID = cursor.fetchone()
        objPermiso = objPermisoID[0]
        cursor.close()
        nbd.CloseConexion()
        return objPermiso
    
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
    
    def ObtenerPersonaID(self, Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaPersona = "SELECT idPersona FROM persona WHERE Nombres = '{}' AND Apellidos = '{}' AND NumeroDocumento = '{}' AND Documento_idDocumento = '{}' AND Contacto_idContacto = '{}'".format(Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto)
        cursor.execute(ConsultaPersona)
        objPersonaID = cursor.fetchone()
        objPersona = objPersonaID[0]
        cursor.close()
        nbd.CloseConexion()
        return objPersona
    
    def InsertTablaContacto(self, telefono, correo): 
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into CONTACTO(Telefono, Email) values ('{}', '{}')".format(telefono, correo)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        
    def InsertTablaPersona(self, Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into persona(Nombres, Apellidos, NumeroDocumento, Documento_idDocumento, Contacto_idContacto) values('{}', '{}', '{}', '{}', '{}')".format(Nombres, Apellidos, NumeroDocumento, idDocumento, idContacto)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        
    def InsertTablaUser(self, NameUser, Contrasenia, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into usuario(NombUser, Password, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos) values('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(NameUser, Contrasenia, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto, Cargo_idCargo, Permisos_idPermisos)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()
        
    def InsertTablaCliente(self, Direccion, idPersona, idDoc, idContac):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into cliente(Direccion, Persona_idPersona, Persona_Documento_idDocumento, Persona_Contacto_idContacto) values('{}', '{}', '{}', '{}')".format(Direccion, idPersona, idDoc, idContac)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        nbd.CloseConexion()