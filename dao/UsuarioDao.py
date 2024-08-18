from util import ConexionBD


class UsuarioBD:
    
    def ObtenerUsuarioID(self, NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaUsuario = "SELECT idUsuario FROM usuario WHERE NombUser = '{}' AND Password = '{}' AND Cargo_idCargo = '{}' AND Permisos_idPermisos = '{}' AND Persona_idPersona = '{}' AND Persona_Contacto_idContacto = '{}' AND Persona_NumeroDocumento_idNumeroDocumento = '{}' AND Persona_NumeroDocumento_TipoDocumento_idTipoDocumento = '{}'".format(NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento)
        cursor.execute(ConsultaUsuario)
        objUsuarioID = cursor.fetchone()
        objUsuario = objUsuarioID[0]
        return objUsuario
    
    def ConsultaTablaUsuario(self):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTablaUsuario = "SELECT c.idUsuario, c.NombUser, c.Password, p.Nombres, p.Apellidos, f.TipoDoc, i.NumeroDoc, t.Telefono, t.Email, k.TipoCargo, m.TipoPermiso FROM usuario c INNER JOIN persona p ON c.Persona_idPersona = p.idPersona INNER JOIN tipodocumento f ON c.Persona_NumeroDocumento_TipoDocumento_idTipoDocumento = f.idTipoDocumento INNER JOIN numerodocumento i ON c.Persona_NumeroDocumento_idNumeroDocumento = i.idNumeroDocumento INNER JOIN contacto t ON c.Persona_Contacto_idContacto = t.idContacto INNER JOIN cargo k ON c.Cargo_idCargo = k.idCargo INNER JOIN permisos m ON c.Permisos_idPermisos = m.idPermisos"
        cursor.execute(ConsultaTablaUsuario)
        return cursor.fetchall()
    
    def ObtenerUsuario(self, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerUsuario = "SELECT c.idUsuario, c.NombUser, c.Password, p.Nombres, p.Apellidos, f.TipoDoc, i.NumeroDoc, t.Telefono, t.Email, k.TipoCargo, m.TipoPermiso FROM usuario c INNER JOIN persona p ON c.Persona_idPersona = p.idPersona INNER JOIN tipodocumento f ON c.Persona_NumeroDocumento_TipoDocumento_idTipoDocumento = f.idTipoDocumento INNER JOIN numerodocumento i ON c.Persona_NumeroDocumento_idNumeroDocumento = i.idNumeroDocumento INNER JOIN contacto t ON c.Persona_Contacto_idContacto = t.idContacto INNER JOIN cargo k ON c.Cargo_idCargo = k.idCargo INNER JOIN permisos m ON c.Permisos_idPermisos = m.idPermisos where c.idUsuario = '{}'".format(idUsuario)
        cursor.execute(ObtenerUsuario)
        return cursor.fetchone()
        
    def InsertTablaUser(self, NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into usuario(NombUser, Password, Cargo_idCargo, Permisos_idPermisos, Persona_idPersona, Persona_Contacto_idContacto, Persona_NumeroDocumento_idNumeroDocumento, Persona_NumeroDocumento_TipoDocumento_idTipoDocumento) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(NombUser, Password, idCargo, idPermisos, idPersona, idContacto, idNumeroDocumento, idTipoDocumento)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def UpdateUsuario(self, NombUser, Password, idCargo, idPermisos, idUsuario):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        query = "UPDATE usuario SET NombUser = '{}', Password ='{}', Cargo_idCargo = '{}', Permisos_idPermisos = '{}' WHERE idUsuario = '{}'".format(NombUser, Password, idCargo, idPermisos, idUsuario)
        cursor.execute(query)
        nbd.conexionBD.commit()
        cursor.close()
        
    def AllDataNombreDeUsuarios(self, idCargo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        cursor.execute("select concat(p.Nombres,' ',p.Apellidos) from usuario u inner join persona p on p.idPersona = u.Persona_idPersona where u.Cargo_idCargo = '{}'".format(idCargo))
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def UbicadorDeUsuarioXNombreYApellido(self, NombYApelli, idCargo):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ObtenerUsuarioID = "select u.idUsuario from usuario u inner join persona p on u.Persona_idPersona = p.idPersona where concat(p.Nombres,' ',p.Apellidos) = '{}' and u.Cargo_idCargo = '{}'".format(NombYApelli, idCargo)
        cursor.execute(ObtenerUsuarioID)
        objUsuarioID = cursor.fetchone()
        objUsuario = objUsuarioID[0]
        return objUsuario
        
        
        