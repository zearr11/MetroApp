from util import ConexionBD


class GuiaSalidaBD:
    
    def InsertTablaGuiaSalida(self, Fecha, idMedioPago, idUsuario, idCliente):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        Insert = "insert into guiasalida(Fecha, MedioPago_idMedioPago, Usuario_idUsuario, Cliente_idCliente) values ('{}', '{}', '{}', '{}')".format(Fecha, idMedioPago, idUsuario, idCliente)
        cursor.execute(Insert)
        nbd.conexionBD.commit()
        cursor.close()
        
    def ObtenerGuiaSalidaID(self, Fecha, idMedioPago, idUsuario, idCliente):
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaGuiaSalida = "select idGuiaSalida from guiasalida where Fecha = '{}' and MedioPago_idMedioPago = '{}' and Usuario_idUsuario = '{}' and Cliente_idCliente = '{}'".format(Fecha, idMedioPago, idUsuario, idCliente)
        cursor.execute(ConsultaGuiaSalida)
        objGuiaSalidaID = cursor.fetchone()
        objGuiaSalida = objGuiaSalidaID[0]
        return objGuiaSalida
    
    def ConsultaTablaGuiaSalida(self):#
        nbd = ConexionBD.ConectBaseData()
        cursor = nbd.conexionBD.cursor()
        ConsultaTablaGuiaSalida = "select s.idGuiaSalida, s.Fecha, p_u.Nombres as NombresUsuario, p_u.Apellidos as ApellidosUsuario, p_c.Nombres as NombresCliente, p_c.Apellidos as ApellidosCliente,  o.Telefono, c.Direccion, m.TipoPago from guiasalida s inner join mediopago m on m.idMedioPago = s.MedioPago_idMedioPago inner join usuario u on u.idUsuario = s.Usuario_idUsuario inner join persona p_u on p_u.idPersona = u.Persona_idPersona inner join cliente c on c.idCliente = s.Cliente_idCliente inner join persona p_c on p_c.idPersona = c.Persona_idPersona inner join contacto o on o.idContacto = c.Persona_Contacto_idContacto order by s.idGuiaSalida asc"
        cursor.execute(ConsultaTablaGuiaSalida)
        return cursor.fetchall()