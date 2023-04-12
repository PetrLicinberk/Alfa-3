/*
Projekt: Alfa 3 – Databázový projekt, obchod
Autor: Petr Licinberk
Email: licinberk@spsejecna.cz
Datum vypracování: 3. 2. 2023
Škola: Střední průmyslová škola elektrotechnická Ječná
Jedná se o školní project
*/

CREATE DATABASE  IF NOT EXISTS `shop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `shop`;
-- MariaDB dump 10.19  Distrib 10.4.27-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: shop
-- ------------------------------------------------------
-- Server version	10.4.27-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Potraviny'),(2,'Napoje'),(3,'Elektronika'),(6,'Nabytek'),(7,'kancelarske potreb');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(32) NOT NULL,
  `last_name` varchar(32) NOT NULL,
  `email` varchar(64) NOT NULL,
  `city` varchar(64) NOT NULL,
  `street` varchar(64) NOT NULL,
  `postal_code` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Dan','Zeleny','danzeleny@gmail.com','Praha','Jecna 40','10034'),(2,'Lukas','Modry','modry@gmail.com','Brno','Lomena 134','56783'),(3,'Jiri','Strom','jstrom@gmail.com','Ostrava','Nadrazni 6','28934'),(4,'Petr','Novak','novak@gmail.com','Brno','U Potoka 163','56103'),(7,'Matej','Novak\'','mnovak@seznam.cz','Praha','Nova402','12389'),(8,'Michal','Pomaly','pomaly@gmail.com','Brno','Stara 45','3216');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `order_date` datetime NOT NULL,
  `payment` enum('kreditni karta','hotovost') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_customer_id` (`customer_id`),
  CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
INSERT INTO `order_details` VALUES (1,1,'2022-06-24 13:05:34','kreditni karta'),(2,3,'2022-06-24 14:37:02','kreditni karta'),(3,2,'2022-06-24 16:55:44','hotovost'),(4,1,'2022-06-25 08:25:14','kreditni karta'),(5,4,'2022-06-25 10:01:59','hotovost'),(6,2,'2022-06-25 11:09:41','kreditni karta'),(7,4,'2022-06-25 15:38:19','kreditni karta'),(8,3,'2022-06-26 07:42:04','hotovost'),(10,1,'2023-02-03 13:58:45','kreditni karta'),(11,1,'2023-02-03 13:34:34','kreditni karta'),(13,1,'2023-02-03 13:58:45','kreditni karta'),(14,1,'2023-02-03 16:56:20','hotovost'),(17,7,'2023-01-27 14:06:35','hotovost');
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_id` (`product_id`),
  KEY `fk_order_id` (`order_id`),
  CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_details` (`id`),
  CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `positive_amount` CHECK (`amount` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
INSERT INTO `order_item` VALUES (1,3,1,3),(2,6,1,5),(3,1,2,2),(4,2,2,1),(5,8,2,4),(6,4,3,7),(7,3,4,2),(8,9,4,1),(9,10,4,1),(10,2,4,6),(11,7,5,1),(12,3,5,2),(13,4,6,3),(14,1,7,1),(15,8,7,5),(16,9,8,2),(17,10,8,1),(18,7,8,1),(19,12,13,2),(20,11,13,1),(21,8,13,3),(25,9,17,3),(26,6,14,12);
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!50001 DROP VIEW IF EXISTS `order_items`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `order_items` AS SELECT
 1 AS `id`,
  1 AS `first_name`,
  1 AS `last_name`,
  1 AS `order_date`,
  1 AS `payment`,
  1 AS `item_id`,
  1 AS `name`,
  1 AS `price`,
  1 AS `amount` */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `in_stock` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category_id` (`category_id`),
  CONSTRAINT `fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `positive_price` CHECK (`price` > 0)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,'Chleba',14.90,1),(2,3,'Baterie',4.90,1),(3,2,'Voda',9.90,1),(4,2,'Caj',19.90,0),(5,1,'Mrkev',4.90,0),(6,1,'Jablko',3.90,1),(7,3,'Graficka karta',14990.00,0),(8,2,'Kava',24.90,1),(9,1,'Pomeranc',6.90,1),(10,3,'Procesor',9990.00,0),(11,6,'Stul',1399.90,1),(12,6,'Kreslo',1590.90,1),(13,2,'Energeticky napoj',39.90,0);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `products_out_of_stock`
--

DROP TABLE IF EXISTS `products_out_of_stock`;
/*!50001 DROP VIEW IF EXISTS `products_out_of_stock`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `products_out_of_stock` AS SELECT
 1 AS `id`,
  1 AS `category_id`,
  1 AS `name`,
  1 AS `price`,
  1 AS `in_stock` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `total_sales`
--

DROP TABLE IF EXISTS `total_sales`;
/*!50001 DROP VIEW IF EXISTS `total_sales`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `total_sales` AS SELECT
 1 AS `name`,
  1 AS `total_sales` */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `order_items`
--

/*!50001 DROP VIEW IF EXISTS `order_items`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `order_items` AS select `d`.`id` AS `id`,`c`.`first_name` AS `first_name`,`c`.`last_name` AS `last_name`,`d`.`order_date` AS `order_date`,`d`.`payment` AS `payment`,`i`.`id` AS `item_id`,`p`.`name` AS `name`,`p`.`price` AS `price`,`i`.`amount` AS `amount` from (((`order_details` `d` join `order_item` `i` on(`i`.`order_id` = `d`.`id`)) join `product` `p` on(`i`.`product_id` = `p`.`id`)) join `customer` `c` on(`d`.`customer_id` = `c`.`id`)) order by `d`.`id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `products_out_of_stock`
--

/*!50001 DROP VIEW IF EXISTS `products_out_of_stock`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `products_out_of_stock` AS select `p`.`id` AS `id`,`p`.`category_id` AS `category_id`,`p`.`name` AS `name`,`p`.`price` AS `price`,`p`.`in_stock` AS `in_stock` from `product` `p` where `p`.`in_stock` = 0 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `total_sales`
--

/*!50001 DROP VIEW IF EXISTS `total_sales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `total_sales` AS select `p`.`name` AS `name`,ifnull(sum(`i`.`amount` * `p`.`price`),0) AS `total_sales` from (`product` `p` left join `order_item` `i` on(`i`.`product_id` = `p`.`id`)) group by `p`.`name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-03 21:33:14
