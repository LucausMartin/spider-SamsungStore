/*
SQLyog Ultimate v11.25 (64 bit)
MySQL - 5.7.19 : Database - spider
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`spider` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `spider`;

/*Table structure for table `kind` */

DROP TABLE IF EXISTS `kind`;

CREATE TABLE `kind` (
  `id` int(11) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `url` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `kind` */

/*Table structure for table `phone` */

DROP TABLE IF EXISTS `phone`;

CREATE TABLE `phone` (
  `id` int(32) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `price` int(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `phone` */

/*Table structure for table `smart_home` */

DROP TABLE IF EXISTS `smart_home`;

CREATE TABLE `smart_home` (
  `id` int(32) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `price` int(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `smart_home` */

/*Table structure for table `storage` */

DROP TABLE IF EXISTS `storage`;

CREATE TABLE `storage` (
  `id` int(32) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `price` int(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `storage` */

/*Table structure for table `tv` */

DROP TABLE IF EXISTS `tv`;

CREATE TABLE `tv` (
  `id` int(32) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `price` int(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `tv` */

/*Table structure for table `wearable` */

DROP TABLE IF EXISTS `wearable`;

CREATE TABLE `wearable` (
  `id` int(32) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `price` int(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `wearable` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
