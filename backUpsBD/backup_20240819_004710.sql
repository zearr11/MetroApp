-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo` (
  `idCargo` int NOT NULL AUTO_INCREMENT,
  `TipoCargo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES (1,'Seleccione'),(2,'Cajero'),(3,'Auxiliar de Compras'),(4,'Auxiliar de Almacen'),(5,'Jefe de Ventas'),(6,'Jefe de Compras'),(7,'Jefe de Almacen'),(8,'Administrador General');
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `idCategoria` int NOT NULL AUTO_INCREMENT,
  `TipoCategoria` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Seleccione'),(2,'Frutas y Verduras'),(3,'Carnes y Pescados'),(4,'Lácteos y Derivados'),(5,'Panadería y Pastelería'),(6,'Bebidas Alcohólicas'),(7,'Bebidas no Alcohólicas'),(8,'Congelados'),(9,'Abarrotes'),(10,'Limpieza y Cuidado del Hogar'),(11,'Higiene Personal'),(12,'Productos para Bebés'),(13,'Mascotas'),(14,'Juguetería'),(15,'Textiles y Ropa'),(16,'Papelería y Oficina'),(17,'Tecnologia y Electronica');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `Direccion` varchar(100) DEFAULT NULL,
  `Persona_idPersona` int NOT NULL,
  `Persona_Contacto_idContacto` int NOT NULL,
  `Persona_NumeroDocumento_idNumeroDocumento` int NOT NULL,
  `Persona_NumeroDocumento_TipoDocumento_idTipoDocumento` int NOT NULL,
  PRIMARY KEY (`idCliente`,`Persona_idPersona`,`Persona_Contacto_idContacto`,`Persona_NumeroDocumento_idNumeroDocumento`,`Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`),
  KEY `fk_Cliente_Persona1_idx` (`Persona_idPersona`,`Persona_Contacto_idContacto`,`Persona_NumeroDocumento_idNumeroDocumento`,`Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`),
  CONSTRAINT `fk_Cliente_Persona1` FOREIGN KEY (`Persona_idPersona`, `Persona_Contacto_idContacto`, `Persona_NumeroDocumento_idNumeroDocumento`, `Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`) REFERENCES `persona` (`idPersona`, `Contacto_idContacto`, `NumeroDocumento_idNumeroDocumento`, `NumeroDocumento_TipoDocumento_idTipoDocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Calle Falsa 123',6000,1,1,2),(2,'Avenida Siempre Viva 742',6001,2,2,2),(3,'Boulevard del Río 456',6002,3,3,2),(4,'Plaza Mayor 789',6003,4,4,2),(5,'Calle del Sol 321',6004,5,5,2),(6,'Avenida Libertad 654',6005,6,6,2),(7,'Calle de la Luna 987',6006,7,7,2),(8,'Avenida de la Paz 135',6007,8,8,2),(9,'Calle del Mar 246',6008,9,9,2),(10,'Avenida de la Esperanza 369',6009,10,10,2),(11,'Calle del Viento 482',6010,11,11,3),(12,'Avenida del Progreso 593',6011,12,12,3),(13,'Calle del Bosque 604',6012,13,13,3),(14,'Plaza del Mercado 715',6013,14,14,3),(15,'Avenida del Valle 826',6014,15,15,3),(16,'Calle de la Alegría 937',6015,16,16,3),(17,'Avenida del Parque 048',6016,17,17,3),(18,'Calle del Río 159',6017,18,18,3),(19,'Plaza del Sol 270',6018,19,19,3),(20,'Calle de la Montaña 381',6019,20,20,3);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `idCompra` int NOT NULL AUTO_INCREMENT,
  `Fecha` date DEFAULT NULL,
  `Estado` varchar(45) DEFAULT NULL,
  `Usuario_idUsuario` int NOT NULL,
  `DocumentodeVenta_idDocumentodeVenta` int NOT NULL,
  `Proveedor_idProveedor` int NOT NULL,
  PRIMARY KEY (`idCompra`,`Usuario_idUsuario`,`DocumentodeVenta_idDocumentodeVenta`,`Proveedor_idProveedor`),
  KEY `fk_Compra_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Compra_DocumentodeVenta1_idx` (`DocumentodeVenta_idDocumentodeVenta`),
  KEY `fk_Compra_Proveedor1_idx` (`Proveedor_idProveedor`),
  CONSTRAINT `fk_Compra_DocumentodeVenta1` FOREIGN KEY (`DocumentodeVenta_idDocumentodeVenta`) REFERENCES `documentodeventa` (`idDocumentodeVenta`),
  CONSTRAINT `fk_Compra_Proveedor1` FOREIGN KEY (`Proveedor_idProveedor`) REFERENCES `proveedor` (`idProveedor`),
  CONSTRAINT `fk_Compra_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4006 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (4000,'2024-08-17','Atendido',2000,3,3004),(4001,'2024-08-17','Atendido',2000,5,3016),(4002,'2024-08-17','Atendido',2000,6,3002),(4003,'2024-08-18','Atendido',2000,9,3003),(4004,'2024-08-18','Atendido',2000,10,3017),(4005,'2024-08-18','Atendido',2000,11,3004);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacto`
--

DROP TABLE IF EXISTS `contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto` (
  `idContacto` int NOT NULL AUTO_INCREMENT,
  `Telefono` int DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idContacto`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacto`
--

LOCK TABLES `contacto` WRITE;
/*!40000 ALTER TABLE `contacto` DISABLE KEYS */;
INSERT INTO `contacto` VALUES (1,912345678,'nova912_a@gmail.com'),(2,923456789,'quark923x@hotmail.com'),(3,934567890,'lynx934.yz@gmail.com'),(4,945678901,'delta945z@hotmail.com'),(5,956789012,'zeta956_q@gmail.com'),(6,967890123,'vortex967mx@hotmail.com'),(7,978901234,'sigma978_abc@gmail.com'),(8,989012345,'echo989yz@hotmail.com'),(9,990123456,'pulsar990p1@gmail.com'),(10,901234567,'zenith901_x@hotmail.com'),(11,912345679,'omega912_m2@gmail.com'),(12,923456780,'nebula923wy@hotmail.com'),(13,934567891,'aether934_jk@gmail.com'),(14,945678902,'spectrum945lm@hotmail.com'),(15,956789013,'phoenix956_vz@gmail.com'),(16,967890124,'quantum967xp@hotmail.com'),(17,978901235,'lambda978_r3@gmail.com'),(18,989012346,'krypton989lk@hotmail.com'),(19,990123457,'vertex990_45@gmail.com'),(20,901234568,'aurora901_nm@hotmail.com'),(21,5123456,'contacto@lechegloria.com.pe'),(22,5234567,'ventas@cevicheriaelancla.com.pe'),(23,5345678,'info@panaderiasanantonio.com.pe'),(24,5456789,'atencion@inkacola.com.pe'),(25,5567890,'consultas@refrescoscusquena.com.pe'),(26,5678901,'ventas@congeladoslima.com.pe'),(27,5789012,'contacto@distribuidorapalacios.com.pe'),(28,5890123,'soporte@limpiezaperu.com.pe'),(29,5901234,'servicio@higieneybelleza.com.pe'),(30,5012345,'info@babycareperu.com.pe'),(31,5123456,'ventas@mascotasyfamiliaperu.com.pe'),(32,5234567,'contacto@juguetesydiversion.com.pe'),(33,5345678,'ventas@textileslamoderna.com.pe'),(34,5456789,'atencion@papeleriarapida.com.pe'),(35,5567890,'soporte@electrodomesticoshiper.com.pe'),(36,5678901,'info@articulosdeoficinalima.com.pe'),(37,5789012,'ventas@modayestilo.com.pe'),(38,5890123,'contacto@frutasdelvalle.com.pe'),(39,999087167,'correo23@gmail.com'),(40,988327122,'jk11anto@hotmail.com'),(41,988237622,'contaccIdat2@hotmail.com'),(42,988347216,'mkmlst23@gmail.com'),(43,988237611,'cokkks8882@hotmail.com'),(44,988236701,'ssdllskiw82@hotmail.com');
/*!40000 ALTER TABLE `contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallecompra`
--

DROP TABLE IF EXISTS `detallecompra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallecompra` (
  `idDetalleCompra` int NOT NULL AUTO_INCREMENT,
  `CantidadProdCompr` varchar(45) DEFAULT NULL,
  `TotalXProd` varchar(45) DEFAULT NULL,
  `Producto_idProducto` int NOT NULL,
  `Compra_idCompra` int NOT NULL,
  PRIMARY KEY (`idDetalleCompra`,`Producto_idProducto`,`Compra_idCompra`),
  KEY `fk_DetalleCompra_Producto1_idx` (`Producto_idProducto`),
  KEY `fk_DetalleCompra_Compra1_idx` (`Compra_idCompra`),
  CONSTRAINT `fk_DetalleCompra_Compra1` FOREIGN KEY (`Compra_idCompra`) REFERENCES `compra` (`idCompra`),
  CONSTRAINT `fk_DetalleCompra_Producto1` FOREIGN KEY (`Producto_idProducto`) REFERENCES `producto` (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallecompra`
--

LOCK TABLES `detallecompra` WRITE;
/*!40000 ALTER TABLE `detallecompra` DISABLE KEYS */;
INSERT INTO `detallecompra` VALUES (1,'1','6.0',5004,4000),(2,'23','80.5',5007,4001),(3,'2','40.0',5017,4001),(4,'9','36.0',5023,4001),(5,'23','96.6',5002,4002),(6,'12','60.0',5003,4002),(7,'2','12.0',5004,4003),(8,'2','8.0',5023,4004),(9,'2','3.0',5000,4004),(10,'3','9000.0',5015,4004),(11,'5','900.0',5013,4004),(12,'6','21.0',5007,4004),(13,'1','0.8',5016,4004),(14,'2','5.0',5021,4005),(15,'11','1210.0',5020,4005);
/*!40000 ALTER TABLE `detallecompra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalleventa`
--

DROP TABLE IF EXISTS `detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalleventa` (
  `idDetalleVenta` int NOT NULL AUTO_INCREMENT,
  `CantidadProd` varchar(45) DEFAULT NULL,
  `Total` varchar(45) DEFAULT NULL,
  `Producto_idProducto` int NOT NULL,
  `Venta_idVenta` int NOT NULL,
  PRIMARY KEY (`idDetalleVenta`,`Producto_idProducto`,`Venta_idVenta`),
  KEY `fk_DetalleVenta_Producto1_idx` (`Producto_idProducto`),
  KEY `fk_DetalleVenta_Venta1_idx` (`Venta_idVenta`),
  CONSTRAINT `fk_DetalleVenta_Producto1` FOREIGN KEY (`Producto_idProducto`) REFERENCES `producto` (`idProducto`),
  CONSTRAINT `fk_DetalleVenta_Venta1` FOREIGN KEY (`Venta_idVenta`) REFERENCES `venta` (`idVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
INSERT INTO `detalleventa` VALUES (1,'23','34.5',5005,7000),(2,'1','5.0',5003,7001),(3,'2','16.0',5022,7001),(4,'23','115.0',5003,7002),(5,'2','36.0',5006,7002),(6,'2','16.0',5022,7003),(7,'25','300.0',5001,7004),(8,'23','3450.0',5012,7004);
/*!40000 ALTER TABLE `detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentodeventa`
--

DROP TABLE IF EXISTS `documentodeventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentodeventa` (
  `idDocumentodeVenta` int NOT NULL AUTO_INCREMENT,
  `NumeroDocumentoVenta` varchar(45) DEFAULT NULL,
  `SubTotal` varchar(45) DEFAULT NULL,
  `IGV` varchar(45) DEFAULT NULL,
  `TotalCancelado` varchar(45) DEFAULT NULL,
  `TipoDocVenta_idTipoDocVenta` int NOT NULL,
  PRIMARY KEY (`idDocumentodeVenta`,`TipoDocVenta_idTipoDocVenta`),
  KEY `fk_DocumentodeVenta_TipoDocVenta1_idx` (`TipoDocVenta_idTipoDocVenta`),
  CONSTRAINT `fk_DocumentodeVenta_TipoDocVenta1` FOREIGN KEY (`TipoDocVenta_idTipoDocVenta`) REFERENCES `tipodocventa` (`idTipoDocVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentodeventa`
--

LOCK TABLES `documentodeventa` WRITE;
/*!40000 ALTER TABLE `documentodeventa` DISABLE KEYS */;
INSERT INTO `documentodeventa` VALUES (1,'5263112019','1','1','1',3),(2,'5263112020','28.29','6.21','34.5',2),(3,'5263112021','4.92','1.08','6.0',3),(4,'5263112022','17.22','3.78','21.0',2),(5,'5263112023','128.33','28.169999999999998','156.5',3),(6,'5263112024','128.412','28.188','156.6',3),(7,'5263112025','123.82','27.18','151.0',2),(8,'5263112026','13.120000000000001','2.88','16.0',2),(9,'5263112027','9.84','2.16','12.0',3),(10,'5263112028','8144.896','1787.9039999999998','9932.8',3),(11,'5263112029','996.3','218.7','1215.0',3),(12,'5263112030','3075.0','675.0','3750.0',3);
/*!40000 ALTER TABLE `documentodeventa` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_insert_NumeroDocumentoVenta` BEFORE INSERT ON `documentodeventa` FOR EACH ROW BEGIN
   -- Obtener el valor máximo actual de NumeroDocumentoVenta y sumarle 1
   SET NEW.NumeroDocumentoVenta = (
       SELECT IFNULL(MAX(CAST(NumeroDocumentoVenta AS UNSIGNED)) + 1, 1)
       FROM documentodeventa
   );
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado` (
  `idEstado` int NOT NULL AUTO_INCREMENT,
  `Estado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idEstado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (1,'Seleccione'),(2,'Disponible'),(3,'No Disponible'),(4,'Descontinuado');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guiaentrada`
--

DROP TABLE IF EXISTS `guiaentrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guiaentrada` (
  `idGuiaEntrada` int NOT NULL AUTO_INCREMENT,
  `FechaRecepcion` date DEFAULT NULL,
  `Recepcion` varchar(45) DEFAULT NULL,
  `DetalleCompra_idDetalleCompra` int NOT NULL,
  `DetalleCompra_Producto_idProducto` int NOT NULL,
  `DetalleCompra_Compra_idCompra` int NOT NULL,
  PRIMARY KEY (`idGuiaEntrada`,`DetalleCompra_idDetalleCompra`,`DetalleCompra_Producto_idProducto`,`DetalleCompra_Compra_idCompra`),
  KEY `fk_GuiaEntrada_DetalleCompra1_idx` (`DetalleCompra_idDetalleCompra`,`DetalleCompra_Producto_idProducto`,`DetalleCompra_Compra_idCompra`),
  CONSTRAINT `fk_GuiaEntrada_DetalleCompra1` FOREIGN KEY (`DetalleCompra_idDetalleCompra`, `DetalleCompra_Producto_idProducto`, `DetalleCompra_Compra_idCompra`) REFERENCES `detallecompra` (`idDetalleCompra`, `Producto_idProducto`, `Compra_idCompra`)
) ENGINE=InnoDB AUTO_INCREMENT=8015 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guiaentrada`
--

LOCK TABLES `guiaentrada` WRITE;
/*!40000 ALTER TABLE `guiaentrada` DISABLE KEYS */;
INSERT INTO `guiaentrada` VALUES (8000,'2024-08-17','Si',1,5004,4000),(8001,'2024-08-17','Si',2,5007,4001),(8002,'2024-08-17','No',3,5017,4001),(8003,'2024-08-17','Si',4,5023,4001),(8004,'2024-08-17','Si',5,5002,4002),(8005,'2024-08-17','Si',6,5003,4002),(8006,'2024-08-18','Si',14,5021,4005),(8007,'2024-08-18','Si',15,5020,4005),(8008,'2024-08-18','Si',7,5004,4003),(8009,'2024-08-18','Si',8,5023,4004),(8010,'2024-08-18','No',9,5000,4004),(8011,'2024-08-18','Si',10,5015,4004),(8012,'2024-08-18','Si',11,5013,4004),(8013,'2024-08-18','Si',12,5007,4004),(8014,'2024-08-18','Si',13,5016,4004);
/*!40000 ALTER TABLE `guiaentrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guiasalida`
--

DROP TABLE IF EXISTS `guiasalida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guiasalida` (
  `idGuiaSalida` int NOT NULL AUTO_INCREMENT,
  `Fecha` date DEFAULT NULL,
  `MedioPago_idMedioPago` int NOT NULL,
  `Usuario_idUsuario` int NOT NULL,
  `Cliente_idCliente` int NOT NULL,
  PRIMARY KEY (`idGuiaSalida`,`MedioPago_idMedioPago`,`Usuario_idUsuario`,`Cliente_idCliente`),
  KEY `fk_GuiaSalida_MedioPago1_idx` (`MedioPago_idMedioPago`),
  KEY `fk_GuiaSalida_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_GuiaSalida_Cliente1_idx` (`Cliente_idCliente`),
  CONSTRAINT `fk_GuiaSalida_Cliente1` FOREIGN KEY (`Cliente_idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `fk_GuiaSalida_MedioPago1` FOREIGN KEY (`MedioPago_idMedioPago`) REFERENCES `mediopago` (`idMedioPago`),
  CONSTRAINT `fk_GuiaSalida_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=8004 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guiasalida`
--

LOCK TABLES `guiasalida` WRITE;
/*!40000 ALTER TABLE `guiasalida` DISABLE KEYS */;
INSERT INTO `guiasalida` VALUES (8000,'2024-08-17',4,2000,9),(8001,'2024-08-18',2,2000,4),(8002,'2024-08-18',4,2000,18),(8003,'2024-08-18',4,2000,6);
/*!40000 ALTER TABLE `guiasalida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logusers`
--

DROP TABLE IF EXISTS `logusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logusers` (
  `idLogUsers` int NOT NULL AUTO_INCREMENT,
  `Usuario_idUsuario` int NOT NULL,
  PRIMARY KEY (`idLogUsers`,`Usuario_idUsuario`),
  KEY `fk_LogUsers_Usuario1_idx` (`Usuario_idUsuario`),
  CONSTRAINT `fk_LogUsers_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logusers`
--

LOCK TABLES `logusers` WRITE;
/*!40000 ALTER TABLE `logusers` DISABLE KEYS */;
INSERT INTO `logusers` VALUES (1,2000),(2,2000),(3,2000),(4,2000),(5,2000),(6,2000),(7,2000),(8,2000),(9,2000),(10,2000),(11,2000),(12,2000),(13,2000),(14,2000),(15,2000),(16,2000),(17,2000),(19,2000),(20,2000),(21,2000),(22,2000),(23,2000),(24,2000),(25,2000),(26,2000),(27,2000),(28,2000),(29,2000),(30,2000),(31,2000),(32,2000),(33,2000),(34,2000),(35,2000),(36,2000),(37,2000),(42,2000),(43,2000),(44,2000),(45,2000),(46,2000),(47,2000),(48,2000),(49,2000),(50,2000),(51,2000),(52,2000),(53,2000),(54,2000),(55,2000),(56,2000),(57,2000),(58,2000),(59,2000),(60,2000),(61,2000),(62,2000),(18,2001),(40,2002),(41,2003),(38,2004),(39,2005);
/*!40000 ALTER TABLE `logusers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medidaventa`
--

DROP TABLE IF EXISTS `medidaventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medidaventa` (
  `idMedidaVenta` int NOT NULL AUTO_INCREMENT,
  `MedidaVenta` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idMedidaVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medidaventa`
--

LOCK TABLES `medidaventa` WRITE;
/*!40000 ALTER TABLE `medidaventa` DISABLE KEYS */;
INSERT INTO `medidaventa` VALUES (1,'Seleccione'),(2,'Unidad'),(3,'Kilogramos');
/*!40000 ALTER TABLE `medidaventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mediopago`
--

DROP TABLE IF EXISTS `mediopago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mediopago` (
  `idMedioPago` int NOT NULL AUTO_INCREMENT,
  `TipoPago` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idMedioPago`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mediopago`
--

LOCK TABLES `mediopago` WRITE;
/*!40000 ALTER TABLE `mediopago` DISABLE KEYS */;
INSERT INTO `mediopago` VALUES (1,'Seleccione'),(2,'Efectivo'),(3,'Débito'),(4,'Crédito'),(5,'Pago Móvil');
/*!40000 ALTER TABLE `mediopago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `numerodocumento`
--

DROP TABLE IF EXISTS `numerodocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `numerodocumento` (
  `idNumeroDocumento` int NOT NULL AUTO_INCREMENT,
  `NumeroDoc` varchar(45) DEFAULT NULL,
  `TipoDocumento_idTipoDocumento` int NOT NULL,
  PRIMARY KEY (`idNumeroDocumento`,`TipoDocumento_idTipoDocumento`),
  KEY `fk_NumeroDocumento_TipoDocumento1_idx` (`TipoDocumento_idTipoDocumento`),
  CONSTRAINT `fk_NumeroDocumento_TipoDocumento1` FOREIGN KEY (`TipoDocumento_idTipoDocumento`) REFERENCES `tipodocumento` (`idTipoDocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `numerodocumento`
--

LOCK TABLES `numerodocumento` WRITE;
/*!40000 ALTER TABLE `numerodocumento` DISABLE KEYS */;
INSERT INTO `numerodocumento` VALUES (1,'15469872',2),(2,'23654789',2),(3,'37895124',2),(4,'48963275',2),(5,'59748316',2),(6,'64829537',2),(7,'75948126',2),(8,'86937415',2),(9,'97462038',2),(10,'08123645',2),(11,'100345678',3),(12,'210456789',3),(13,'321567890',3),(14,'432678901',3),(15,'543789012',3),(16,'654890123',3),(17,'765901234',3),(18,'876012345',3),(19,'987123456',3),(20,'098234567',3),(21,'11111111',2),(22,'87626723',2),(23,'74936722',2),(24,'87459338',2),(25,'74846732',2),(26,'78347323',2);
/*!40000 ALTER TABLE `numerodocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisos`
--

DROP TABLE IF EXISTS `permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisos` (
  `idPermisos` int NOT NULL AUTO_INCREMENT,
  `TipoPermiso` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPermisos`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisos`
--

LOCK TABLES `permisos` WRITE;
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
INSERT INTO `permisos` VALUES (1,'Seleccione'),(2,'Usuario Estandar'),(3,'Admin');
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `idPersona` int NOT NULL AUTO_INCREMENT,
  `Nombres` varchar(45) DEFAULT NULL,
  `Apellidos` varchar(45) DEFAULT NULL,
  `Contacto_idContacto` int NOT NULL,
  `NumeroDocumento_idNumeroDocumento` int NOT NULL,
  `NumeroDocumento_TipoDocumento_idTipoDocumento` int NOT NULL,
  PRIMARY KEY (`idPersona`,`Contacto_idContacto`,`NumeroDocumento_idNumeroDocumento`,`NumeroDocumento_TipoDocumento_idTipoDocumento`),
  KEY `fk_Persona_Contacto1_idx` (`Contacto_idContacto`),
  KEY `fk_Persona_NumeroDocumento1_idx` (`NumeroDocumento_idNumeroDocumento`,`NumeroDocumento_TipoDocumento_idTipoDocumento`),
  CONSTRAINT `fk_Persona_Contacto1` FOREIGN KEY (`Contacto_idContacto`) REFERENCES `contacto` (`idContacto`),
  CONSTRAINT `fk_Persona_NumeroDocumento1` FOREIGN KEY (`NumeroDocumento_idNumeroDocumento`, `NumeroDocumento_TipoDocumento_idTipoDocumento`) REFERENCES `numerodocumento` (`idNumeroDocumento`, `TipoDocumento_idTipoDocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=6026 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (6000,'Juan','Pérez Rodríguez',1,1,2),(6001,'Ana','Gómez Martínez',2,2,2),(6002,'Luis','Martínez Vargas',3,3,2),(6003,'María','López García',4,4,2),(6004,'Pedro','Ramírez Soto',5,5,2),(6005,'Laura','Fernández Ramirez',6,6,2),(6006,'Carlos','García Romero',7,7,2),(6007,'Elena','Sánchez Herrera',8,8,2),(6008,'Jorge','Vázquez López',9,9,2),(6009,'Sofía','Mendoza Díaz',10,10,2),(6010,'Andrés','Jiménez Paredes',11,11,3),(6011,'Valeria','Suárez Morales',12,12,3),(6012,'Ricardo','Guerrero Gómez',13,13,3),(6013,'Gabriela','Ríos González',14,14,3),(6014,'Felipe','Hernández Pérez',15,15,3),(6015,'Cristina','Paredes Ramírez',16,16,3),(6016,'Oscar','Cordero Silva',17,17,3),(6017,'Camila','Cano Torres',18,18,3),(6018,'Javier','Arriaga Vargas',19,19,3),(6019,'Natalia','Arias Mendoza',20,20,3),(6020,'Cesar','Gamarra Rivera',39,21,2),(6021,'Jose Antonio','Lopez Ramirez',40,22,2),(6022,'Jhou','Lozano',41,23,2),(6023,'Miguel','Felix',42,24,2),(6024,'Cristhian','Castellanos',43,25,2),(6025,'Roy','Ayala',44,26,2);
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `idProducto` int NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(45) DEFAULT NULL,
  `Marca` varchar(45) DEFAULT NULL,
  `Cantidad` varchar(45) DEFAULT NULL,
  `Precio` varchar(45) DEFAULT NULL,
  `MedidaVenta_idMedidaVenta` int NOT NULL,
  `Estado_idEstado` int NOT NULL,
  `Categoria_idCategoria` int NOT NULL,
  PRIMARY KEY (`idProducto`,`MedidaVenta_idMedidaVenta`,`Estado_idEstado`,`Categoria_idCategoria`),
  KEY `fk_Producto_MedidaVenta1_idx` (`MedidaVenta_idMedidaVenta`),
  KEY `fk_Producto_Estado1_idx` (`Estado_idEstado`),
  KEY `fk_Producto_Categoria1_idx` (`Categoria_idCategoria`),
  CONSTRAINT `fk_Producto_Categoria1` FOREIGN KEY (`Categoria_idCategoria`) REFERENCES `categoria` (`idCategoria`),
  CONSTRAINT `fk_Producto_Estado1` FOREIGN KEY (`Estado_idEstado`) REFERENCES `estado` (`idEstado`),
  CONSTRAINT `fk_Producto_MedidaVenta1` FOREIGN KEY (`MedidaVenta_idMedidaVenta`) REFERENCES `medidaventa` (`idMedidaVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=5025 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (5000,'Manzana Roja','Del Monte','100','1.50',2,2,2),(5001,'Pollo Entero','San Fernando','25','12.00',3,2,3),(5002,'Leche Entera','Gloria','222','4.20',2,2,4),(5003,'Pan Integral','Bimbo','66','5.00',2,2,5),(5004,'Cerveza Rubia','Cusqueña','153','6.00',2,2,6),(5005,'Agua Mineral','San Mateo','275','1.50',2,2,7),(5006,'Helado de Vainilla','D\'Onofrio','58','18.00',3,2,8),(5007,'Arroz Extra','Costeño','129','3.50',3,2,9),(5008,'Detergente en Polvo','Ace','50','12.00',3,2,10),(5009,'Shampoo','Sedal','120','12.50',2,2,11),(5010,'Pañales','Pampers','80','48.00',2,2,12),(5011,'Alimento para Perros','Pedigree','100','120.00',3,2,13),(5012,'Muñeca Barbie','Mattel','7','150.00',2,2,14),(5013,'Sábanas Matrimoniales','Cannon','45','180.00',2,2,15),(5014,'Cuaderno A4','Norma','200','8.00',2,2,16),(5015,'Laptop','HP','13','3000.00',2,2,17),(5016,'Plátano','Chiquita','151','0.80',2,2,2),(5017,'Pescado Fresco','Alicorp','40','20.00',3,2,3),(5018,'Yogurt Natural','Laive','70','6.50',2,2,4),(5019,'Galletas Integrales','Nestlé','90','3.50',2,2,5),(5020,'Whisky','Johnnie Walker','59','110.00',2,2,6),(5021,'Gaseosa','Coca Cola','202','2.50',2,2,7),(5022,'Verduras Congeladas','D\'Onofrio','23','8.00',3,2,8),(5023,'Fideos','Don Vittorio','108','4.00',2,2,9),(5024,'Papel Higiénico','Suave','34','1.00',2,2,10);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `idProveedor` int NOT NULL AUTO_INCREMENT,
  `RazonSocial` varchar(100) DEFAULT NULL,
  `RUC` varchar(12) DEFAULT NULL,
  `Direccion` varchar(100) DEFAULT NULL,
  `Contacto_idContacto` int NOT NULL,
  `Categoria_idCategoria` int NOT NULL,
  PRIMARY KEY (`idProveedor`,`Contacto_idContacto`,`Categoria_idCategoria`),
  KEY `fk_Proveedor_Contacto1_idx` (`Contacto_idContacto`),
  KEY `fk_Proveedor_Categoria1_idx` (`Categoria_idCategoria`),
  CONSTRAINT `fk_Proveedor_Categoria1` FOREIGN KEY (`Categoria_idCategoria`) REFERENCES `categoria` (`idCategoria`),
  CONSTRAINT `fk_Proveedor_Contacto1` FOREIGN KEY (`Contacto_idContacto`) REFERENCES `contacto` (`idContacto`)
) ENGINE=InnoDB AUTO_INCREMENT=3018 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (3000,'Leche Gloria SA','20123456789','Av. La Victoria 123, La Victoria',21,4),(3001,'Cevichería El Ancla','20234567890','Jr. Puno 234, Miraflores',22,3),(3002,'Panadería San Antonio','20345678901','Av. Tacna 345, Lima Cercado',23,5),(3003,'Inka Cola SAC','20456789012','Av. Javier Prado 456, San Isidro',24,6),(3004,'Refrescos Cusqueña SRL','20567890123','Av. Arequipa 567, Lince',25,7),(3005,'Congelados Lima SAC','20678901234','Av. Industrial 678, Callao',26,8),(3006,'Distribuidora Palacios SRL','20789012345','Jr. Callao 789, Breña',27,9),(3007,'Limpieza Perú SAC','20890123456','Av. El Sol 890, San Juan de Miraflores',28,10),(3008,'Higiene y Belleza BELLEZA SRL','20901234567','Av. Brasil 901, Jesús María',29,11),(3009,'Babycare Perú SAC','20012345678','Jr. Huancavelica 012, La Molina',30,12),(3010,'Mascotas y Familia SRL','20123456789','Av. Santa Anita 123, Santa Anita',31,13),(3011,'Juguetes y Diversión SRL','20234567890','Jr. Áncash 234, San Borja',32,14),(3012,'Textiles La Moderna SA','20345678901','Av. Alfonso Ugarte 345, El Agustino',33,15),(3013,'Papelería Rápida SAC','20456789012','Jr. Huancayo 456, San Miguel',34,16),(3014,'Electrodomésticos Hiper SRL','20567890123','Av. Nicolás Arriola 567, La Victoria',35,17),(3015,'Artículos de Oficina Perú SAC','20678901234','Jr. Moquegua 678, San Luis',36,16),(3016,'Moda y Estilo SRL','20789012345','Av. Javier Prado Este 789, San Borja',37,15),(3017,'Frutas del Valle SA','20890123456','Jr. Los Frutales 890, Surco',38,2);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportedesalida`
--

DROP TABLE IF EXISTS `reportedesalida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reportedesalida` (
  `idReporteDeSalida` int NOT NULL AUTO_INCREMENT,
  `GuiaSalida_idGuiaSalida` int NOT NULL,
  `Producto_idProducto` int NOT NULL,
  `CantidadProd` varchar(45) DEFAULT NULL,
  `TotalXproduct` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idReporteDeSalida`,`GuiaSalida_idGuiaSalida`,`Producto_idProducto`),
  KEY `fk_ReporteDeSalida_GuiaSalida1_idx` (`GuiaSalida_idGuiaSalida`),
  KEY `fk_ReporteDeSalida_Producto1_idx` (`Producto_idProducto`),
  CONSTRAINT `fk_ReporteDeSalida_GuiaSalida1` FOREIGN KEY (`GuiaSalida_idGuiaSalida`) REFERENCES `guiasalida` (`idGuiaSalida`),
  CONSTRAINT `fk_ReporteDeSalida_Producto1` FOREIGN KEY (`Producto_idProducto`) REFERENCES `producto` (`idProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportedesalida`
--

LOCK TABLES `reportedesalida` WRITE;
/*!40000 ALTER TABLE `reportedesalida` DISABLE KEYS */;
INSERT INTO `reportedesalida` VALUES (1,8000,5005,'2','3.0'),(2,8000,5020,'2','220.0'),(3,8001,5003,'2','10.0'),(4,8001,5022,'23','184.0'),(5,8001,5024,'2','2.0'),(6,8002,5002,'1','4.2'),(7,8003,5023,'23','92.0'),(8,8003,5024,'2','2.0');
/*!40000 ALTER TABLE `reportedesalida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipodocumento`
--

DROP TABLE IF EXISTS `tipodocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipodocumento` (
  `idTipoDocumento` int NOT NULL AUTO_INCREMENT,
  `TipoDoc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idTipoDocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipodocumento`
--

LOCK TABLES `tipodocumento` WRITE;
/*!40000 ALTER TABLE `tipodocumento` DISABLE KEYS */;
INSERT INTO `tipodocumento` VALUES (1,'Seleccione'),(2,'DNI'),(3,'CE');
/*!40000 ALTER TABLE `tipodocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipodocventa`
--

DROP TABLE IF EXISTS `tipodocventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipodocventa` (
  `idTipoDocVenta` int NOT NULL AUTO_INCREMENT,
  `TipoDocVenta` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idTipoDocVenta`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipodocventa`
--

LOCK TABLES `tipodocventa` WRITE;
/*!40000 ALTER TABLE `tipodocventa` DISABLE KEYS */;
INSERT INTO `tipodocventa` VALUES (1,'Seleccione'),(2,'Boleta'),(3,'Factura');
/*!40000 ALTER TABLE `tipodocventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `NombUser` varchar(8) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `Cargo_idCargo` int NOT NULL,
  `Permisos_idPermisos` int NOT NULL,
  `Persona_idPersona` int NOT NULL,
  `Persona_Contacto_idContacto` int NOT NULL,
  `Persona_NumeroDocumento_idNumeroDocumento` int NOT NULL,
  `Persona_NumeroDocumento_TipoDocumento_idTipoDocumento` int NOT NULL,
  PRIMARY KEY (`idUsuario`,`Cargo_idCargo`,`Permisos_idPermisos`,`Persona_idPersona`,`Persona_Contacto_idContacto`,`Persona_NumeroDocumento_idNumeroDocumento`,`Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`),
  KEY `fk_Usuario_Cargo1_idx` (`Cargo_idCargo`),
  KEY `fk_Usuario_Permisos1_idx` (`Permisos_idPermisos`),
  KEY `fk_Usuario_Persona1_idx` (`Persona_idPersona`,`Persona_Contacto_idContacto`,`Persona_NumeroDocumento_idNumeroDocumento`,`Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`),
  CONSTRAINT `fk_Usuario_Cargo1` FOREIGN KEY (`Cargo_idCargo`) REFERENCES `cargo` (`idCargo`),
  CONSTRAINT `fk_Usuario_Permisos1` FOREIGN KEY (`Permisos_idPermisos`) REFERENCES `permisos` (`idPermisos`),
  CONSTRAINT `fk_Usuario_Persona1` FOREIGN KEY (`Persona_idPersona`, `Persona_Contacto_idContacto`, `Persona_NumeroDocumento_idNumeroDocumento`, `Persona_NumeroDocumento_TipoDocumento_idTipoDocumento`) REFERENCES `persona` (`idPersona`, `Contacto_idContacto`, `NumeroDocumento_idNumeroDocumento`, `NumeroDocumento_TipoDocumento_idTipoDocumento`)
) ENGINE=InnoDB AUTO_INCREMENT=2006 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (2000,'admin11','clave123@',3,3,6020,39,21,2),(2001,'josnio2','nuevopass@233',2,2,6021,40,22,2),(2002,'jouu2','idat992@',8,3,6022,41,23,2),(2003,'mig92','idat993@',8,3,6023,42,24,2),(2004,'cast99','idat994@',8,3,6024,43,25,2),(2005,'ayal4','idat995@',8,3,6025,44,26,2);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `idVenta` int NOT NULL AUTO_INCREMENT,
  `Fecha` date DEFAULT NULL,
  `MedioPago_idMedioPago` int NOT NULL,
  `Usuario_idUsuario` int NOT NULL,
  `Cliente_idCliente` int NOT NULL,
  `DocumentodeVenta_idDocumentodeVenta` int NOT NULL,
  PRIMARY KEY (`idVenta`,`MedioPago_idMedioPago`,`Usuario_idUsuario`,`Cliente_idCliente`,`DocumentodeVenta_idDocumentodeVenta`),
  KEY `fk_Venta_MedioPago1_idx` (`MedioPago_idMedioPago`),
  KEY `fk_Venta_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Venta_Cliente1_idx` (`Cliente_idCliente`),
  KEY `fk_Venta_DocumentodeVenta1_idx` (`DocumentodeVenta_idDocumentodeVenta`),
  CONSTRAINT `fk_Venta_Cliente1` FOREIGN KEY (`Cliente_idCliente`) REFERENCES `cliente` (`idCliente`),
  CONSTRAINT `fk_Venta_DocumentodeVenta1` FOREIGN KEY (`DocumentodeVenta_idDocumentodeVenta`) REFERENCES `documentodeventa` (`idDocumentodeVenta`),
  CONSTRAINT `fk_Venta_MedioPago1` FOREIGN KEY (`MedioPago_idMedioPago`) REFERENCES `mediopago` (`idMedioPago`),
  CONSTRAINT `fk_Venta_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7005 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (7000,'2024-08-17',3,2000,8,2),(7001,'2024-08-17',5,2000,3,4),(7002,'2024-08-18',2,2001,20,7),(7003,'2024-08-18',5,2000,7,8),(7004,'2024-08-18',2,2000,7,12);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-19  0:47:10
