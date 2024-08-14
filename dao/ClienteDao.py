from util import ConexionBD


class ClienteBD:
    
    def InsertTablaCliente(self, Direccion, idPersona, idContac, idNumeroDoc, idTipoDoc):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into cliente(Direccion, Persona_idPersona, Persona_Contacto_idContacto, Persona_NumeroDocumento_idNumeroDocumento, Persona_NumeroDocumento_TipoDocumento_idTipoDocumento) values('{}', '{}', '{}', '{}', '{}')".format(Direccion, idPersona, idContac, idNumeroDoc, idTipoDoc)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerNumeroDocumentoCliente(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("SELECT d.NumeroDoc from cliente c inner join numerodocumento d on c.Persona_NumeroDocumento_idNumeroDocumento = d.idNumeroDocumento")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def ObtenerClienteIDXdni(self, idNumeroDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaClienteIDXdni = "SELECT idCliente FROM cliente WHERE Persona_NumeroDocumento_idNumeroDocumento = '{}'".format(idNumeroDocumento)
        cursor.execute(ConsultaClienteIDXdni)
        objClienteIDXdniID = cursor.fetchone()
        objClienteIDXdni = objClienteIDXdniID[0]
        return objClienteIDXdni
    
    def ConsultaTablaCliente(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTablaCliente = "SELECT m.idCliente ,p.Nombres, p.Apellidos, t.TipoDoc, o.NumeroDoc, m.Direccion, s.Telefono, s.Email from cliente m inner join persona p on p.idPersona = m.Persona_idPersona inner join tipodocumento t on t.idTipoDocumento = m.Persona_NumeroDocumento_TipoDocumento_idTipoDocumento inner join numerodocumento o on o.idNumeroDocumento = m.Persona_NumeroDocumento_idNumeroDocumento inner join contacto s on s.idContacto = Persona_Contacto_idContacto"
        cursor.execute(ConsultaTablaCliente)
        return cursor.fetchall()
    
    def ObtenerCliente(self, idCliente):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerCliente = "SELECT m.idCliente ,p.Nombres, p.Apellidos, t.TipoDoc, o.NumeroDoc, m.Direccion, s.Telefono, s.Email from cliente m inner join persona p on p.idPersona = m.Persona_idPersona inner join tipodocumento t on t.idTipoDocumento = m.Persona_NumeroDocumento_TipoDocumento_idTipoDocumento inner join numerodocumento o on o.idNumeroDocumento = m.Persona_NumeroDocumento_idNumeroDocumento inner join contacto s on s.idContacto = Persona_Contacto_idContacto where m.idCliente = '{}'".format(idCliente)
        cursor.execute(ObtenerCliente)
        return cursor.fetchone()
    
    def UpdateCliente(self, Direccion, idPersona, idContacto, idNumeroDocumento, idTipoDocumento, idCliente):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE cliente SET Direccion = '{}', Persona_idPersona = '{}', Persona_Contacto_idContacto = '{}', Persona_NumeroDocumento_idNumeroDocumento = '{}', Persona_NumeroDocumento_TipoDocumento_idTipoDocumento = '{}' where idCliente = '{}'".format(Direccion, idPersona, idContacto, idNumeroDocumento, idTipoDocumento, idCliente)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()