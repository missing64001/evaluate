-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: evaluateg
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'企业用户'),(2,'孵化器用户'),(3,'机构用户');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,25),(2,1,26),(3,1,27),(4,1,28),(5,1,29),(6,1,30),(7,1,31),(8,1,32),(9,1,33),(10,1,34),(11,1,35),(12,1,36),(13,1,37),(14,1,38),(15,1,39),(16,1,40),(17,1,41),(18,1,42),(19,1,43),(20,1,44),(21,1,45),(22,1,49),(23,1,50),(24,1,51),(25,1,52),(26,1,53),(27,1,54),(28,1,55),(29,1,56),(30,1,57),(34,1,58),(35,1,59),(36,1,60),(37,1,61),(38,1,62),(39,1,63),(40,1,64),(41,1,65),(42,1,66),(43,1,67),(44,1,68),(45,1,69),(46,1,70),(47,1,71),(48,1,72),(50,1,73),(51,1,74),(52,1,75),(53,1,76),(54,1,77),(55,1,78),(56,1,79),(57,1,80),(58,1,81),(59,1,82),(60,1,83),(61,1,84),(62,1,85),(63,1,86),(64,1,87),(31,1,88),(32,1,89),(33,1,90),(49,1,92),(65,1,107),(66,2,26),(67,2,29),(68,2,32),(69,2,35),(70,2,38),(71,2,41),(72,2,44),(73,2,47),(74,2,50),(75,2,53),(76,2,56),(78,2,59),(79,2,62),(80,2,65),(81,2,68),(82,2,71),(85,2,74),(86,2,77),(87,2,80),(88,2,83),(89,2,86),(77,2,89),(83,2,91),(84,2,92),(90,2,94),(91,2,95),(92,2,96),(93,2,107),(94,3,26),(95,3,29),(96,3,32),(97,3,35),(98,3,38),(99,3,41),(100,3,44),(101,3,47),(102,3,50),(103,3,53),(104,3,56),(106,3,59),(107,3,62),(108,3,65),(109,3,68),(110,3,71),(111,3,74),(112,3,77),(113,3,80),(114,3,83),(115,3,86),(105,3,89),(116,3,97),(117,3,98),(118,3,99),(119,3,100),(120,3,101),(121,3,102),(122,3,103),(123,3,104),(124,3,105),(125,3,106),(126,3,107),(127,3,108);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 加分项',7,'add_bonus'),(20,'Can change 加分项',7,'change_bonus'),(21,'Can delete 加分项',7,'delete_bonus'),(22,'Can add 减分项',8,'add_subtraction'),(23,'Can change 减分项',8,'change_subtraction'),(24,'Can delete 减分项',8,'delete_subtraction'),(25,'Can add balance',9,'add_balance'),(26,'Can change balance',9,'change_balance'),(27,'Can delete balance',9,'delete_balance'),(28,'Can add cash flow',10,'add_cashflow'),(29,'Can change cash flow',10,'change_cashflow'),(30,'Can delete cash flow',10,'delete_cashflow'),(31,'Can add 一、基本信息',11,'add_companyinfo'),(32,'Can change 一、基本信息',11,'change_companyinfo'),(33,'Can delete 一、基本信息',11,'delete_companyinfo'),(34,'Can add   核心团队(至少三人)',12,'add_coremember'),(35,'Can change   核心团队(至少三人)',12,'change_coremember'),(36,'Can delete   核心团队(至少三人)',12,'delete_coremember'),(37,'Can add 药品批文',13,'add_drugapproval'),(38,'Can change 药品批文',13,'change_drugapproval'),(39,'Can delete 药品批文',13,'delete_drugapproval'),(40,'Can add 教育经历（可增加）',14,'add_educationexperience'),(41,'Can change 教育经历（可增加）',14,'change_educationexperience'),(42,'Can delete 教育经历（可增加）',14,'delete_educationexperience'),(43,'Can add 企业获奖情况',15,'add_enterpriseawards'),(44,'Can change 企业获奖情况',15,'change_enterpriseawards'),(45,'Can delete 企业获奖情况',15,'delete_enterpriseawards'),(46,'Can add 校正评价',16,'add_evaluationofenterprises'),(47,'Can change 校正评价',16,'change_evaluationofenterprises'),(48,'Can delete 校正评价',16,'delete_evaluationofenterprises'),(49,'Can add 二、财务状况',17,'add_financialsituation'),(50,'Can change 二、财务状况',17,'change_financialsituation'),(51,'Can delete 二、财务状况',17,'delete_financialsituation'),(52,'Can add 自主评价',18,'add_independentevaluationofenterprises'),(53,'Can change 自主评价',18,'change_independentevaluationofenterprises'),(54,'Can delete 自主评价',18,'delete_independentevaluationofenterprises'),(55,'Can add 医疗器械注册证',19,'add_mirc'),(56,'Can change 医疗器械注册证',19,'change_mirc'),(57,'Can delete 医疗器械注册证',19,'delete_mirc'),(58,'Can add 专利',20,'add_patent'),(59,'Can change 专利',20,'change_patent'),(60,'Can delete 专利',20,'delete_patent'),(61,'Can add 核心团队个人获奖情况',21,'add_personalawards'),(62,'Can change 核心团队个人获奖情况',21,'change_personalawards'),(63,'Can delete 核心团队个人获奖情况',21,'delete_personalawards'),(64,'Can add 三、产品与市场',22,'add_productsandmarket'),(65,'Can change 三、产品与市场',22,'change_productsandmarket'),(66,'Can delete 三、产品与市场',22,'delete_productsandmarket'),(67,'Can add profit',23,'add_profit'),(68,'Can change profit',23,'change_profit'),(69,'Can delete profit',23,'delete_profit'),(70,'Can add 企业曾经承担或正在承担的科技计划项目',24,'add_project'),(71,'Can change 企业曾经承担或正在承担的科技计划项目',24,'change_project'),(72,'Can delete 企业曾经承担或正在承担的科技计划项目',24,'delete_project'),(73,'Can add 五、服务需求',25,'add_serverrequest'),(74,'Can change 五、服务需求',25,'change_serverrequest'),(75,'Can delete 五、服务需求',25,'delete_serverrequest'),(76,'Can add 主要股东及股权比例（前五名）',26,'add_shareholder'),(77,'Can change 主要股东及股权比例（前五名）',26,'change_shareholder'),(78,'Can delete 主要股东及股权比例（前五名）',26,'delete_shareholder'),(79,'Can add 标准制定情况',27,'add_standardsetting'),(80,'Can change 标准制定情况',27,'change_standardsetting'),(81,'Can delete 标准制定情况',27,'delete_standardsetting'),(82,'Can add 四、技术与研发',28,'add_technologyrd'),(83,'Can change 四、技术与研发',28,'change_technologyrd'),(84,'Can delete 四、技术与研发',28,'delete_technologyrd'),(85,'Can add 工作经历（可增加）',29,'add_workexperience'),(86,'Can change 工作经历（可增加）',29,'change_workexperience'),(87,'Can delete 工作经历（可增加）',29,'delete_workexperience'),(88,'Can add 其他',30,'add_otherm'),(89,'Can change 其他',30,'change_otherm'),(90,'Can delete 其他',30,'delete_otherm'),(91,'Can add 驳回理由',31,'add_rejectreason'),(92,'Can change 驳回理由',31,'change_rejectreason'),(93,'Can delete 驳回理由',31,'delete_rejectreason'),(94,'Can add 孵化器',32,'add_incubator'),(95,'Can change 孵化器',32,'change_incubator'),(96,'Can delete 孵化器',32,'delete_incubator'),(97,'Can add 银行类金融报告',33,'add_bankreport'),(98,'Can change 银行类金融报告',33,'change_bankreport'),(99,'Can delete 银行类金融报告',33,'delete_bankreport'),(100,'Can add 机构',34,'add_institution'),(101,'Can change 机构',34,'change_institution'),(102,'Can delete 机构',34,'delete_institution'),(103,'Can add 投资类金融报告',35,'add_investreport'),(104,'Can change 投资类金融报告',35,'change_investreport'),(105,'Can delete 投资类金融报告',35,'delete_investreport'),(106,'Can add 反馈信息',36,'add_reportback'),(107,'Can change 反馈信息',36,'change_reportback'),(108,'Can delete 反馈信息',36,'delete_reportback');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$dhYZAxYO2A2b$QNru799mu30zKxp2F5K8Gv1UE8T+4kp25DFPF8iLuYM=','2018-11-06 08:26:47.980404',1,'miss','','','',1,1,'2018-11-06 08:25:05.636535'),(2,'pbkdf2_sha256$36000$yoOHiVt6sZyC$aE69LzJcLr1nZt7esBGGEFVqrKj+xstAE50AM6S3fnU=','2018-11-06 08:35:19.775174',0,'fhq','','','xx@qq.com',1,1,'2018-11-06 08:27:26.932983'),(3,'pbkdf2_sha256$36000$he4I3VbvbJvi$Sm7808FYgxnTCoHVTdWPTAJiReo1R/d2sPERyE+pdLs=','2018-11-06 08:36:12.128490',0,'jgtz','','','xx@qq.com',1,1,'2018-11-06 08:27:48.593880'),(4,'pbkdf2_sha256$36000$lcy5KXyKlMxW$aUlM5gQ5mBoVn26z0ASc/6zDb9ZEG/EsWddNVVURBIQ=',NULL,0,'c1','','','xx@qq.com',1,1,'2018-11-06 08:28:52.417253'),(5,'pbkdf2_sha256$36000$P1gEQD2xsjrr$sGCkE/MINT68vfpA/YvjNWHRaWJRTxva2Yt9wnLzwXA=',NULL,0,'c2','','','xx@qq.com',1,1,'2018-11-06 08:39:06.120689'),(6,'pbkdf2_sha256$36000$FP0nmgeDQ4rE$9beN5h1qDEO3gPLBzcb1n62F+Pge8J0mFDL/p76jcc0=',NULL,0,'c3','','','xx@qq.com',1,1,'2018-11-06 08:42:44.999936'),(7,'pbkdf2_sha256$36000$PNtLLuoQh4fM$I6NzOWAfVeXdCMmoIIwovNHHEO54ixX5siBvLX4OgpA=',NULL,0,'c4','','','xx@qq.com',1,1,'2018-11-06 08:43:18.867236'),(8,'pbkdf2_sha256$36000$qDXaSIQFA6Eb$aB5Yb76f6ofg9iaBSuuRZlfs95JeYbLFTEFmcK4dTTI=',NULL,0,'c5','','','xx@qq.com',1,1,'2018-11-06 08:43:54.720678');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,2),(2,3,3),(3,4,1),(4,5,1),(5,6,1),(6,7,1),(7,8,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_balance`
--

DROP TABLE IF EXISTS `company_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_balance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_balance_companyInfo_id_1740a10c_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_balance_companyInfo_id_1740a10c_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_balance`
--

LOCK TABLES `company_balance` WRITE;
/*!40000 ALTER TABLE `company_balance` DISABLE KEYS */;
INSERT INTO `company_balance` VALUES (1,2018,'year',2018,1),(2,2018,'d6',5298.54,1),(3,2018,'e6',1238.49,1),(4,2018,'h6',0,1),(5,2018,'i6',0,1),(6,2018,'d7',0,1),(7,2018,'e7',0,1),(8,2018,'h7',0,1),(9,2018,'i7',0,1),(10,2018,'d8',0,1),(11,2018,'e8',0,1),(12,2018,'h8',0,1),(13,2018,'i8',0,1),(14,2018,'d9',79578,1),(15,2018,'e9',177936.47,1),(16,2018,'h9',5670,1),(17,2018,'i9',32000,1),(18,2018,'d10',0,1),(19,2018,'e10',0,1),(20,2018,'h10',0,1),(21,2018,'i10',43995,1),(22,2018,'d11',0,1),(23,2018,'e11',0,1),(24,2018,'h11',77692,1),(25,2018,'i11',105259.88,1),(26,2018,'d12',0,1),(27,2018,'e12',0,1),(28,2018,'h12',66.92,1),(29,2018,'i12',0,1),(30,2018,'d13',992000,1),(31,2018,'e13',1016000,1),(32,2018,'h13',0,1),(33,2018,'i13',0,1),(34,2018,'d14',0,1),(35,2018,'e14',0,1),(36,2018,'h14',0,1),(37,2018,'i14',0,1),(38,2018,'d15',0,1),(39,2018,'e15',0,1),(40,2018,'h15',34319.88,1),(41,2018,'i15',61548.91,1),(42,2018,'d16',0,1),(43,2018,'e16',0,1),(44,2018,'h16',0,1),(45,2018,'i16',0,1),(46,2018,'h17',0,1),(47,2018,'i17',0,1),(48,2018,'d19',0,1),(49,2018,'e19',0,1),(50,2018,'d20',0,1),(51,2018,'e20',0,1),(52,2018,'h20',0,1),(53,2018,'i20',0,1),(54,2018,'d21',0,1),(55,2018,'e21',0,1),(56,2018,'h21',0,1),(57,2018,'i21',0,1),(58,2018,'d22',0,1),(59,2018,'e22',0,1),(60,2018,'h22',0,1),(61,2018,'i22',0,1),(62,2018,'d23',0,1),(63,2018,'e23',0,1),(64,2018,'h23',0,1),(65,2018,'i23',0,1),(66,2018,'d24',1583.3,1),(67,2018,'e24',21487.3,1),(68,2018,'h24',0,1),(69,2018,'i24',0,1),(70,2018,'d25',369.46,1),(71,2018,'e25',7462.36,1),(72,2018,'h25',0,1),(73,2018,'i25',0,1),(74,2018,'h26',0,1),(75,2018,'i26',0,1),(76,2018,'d27',0,1),(77,2018,'e27',0,1),(78,2018,'d29',0,1),(79,2018,'e29',0,1),(80,2018,'d30',0,1),(81,2018,'e30',0,1),(82,2018,'h30',1000000,1),(83,2018,'i30',1000000,1),(84,2018,'d31',0,1),(85,2018,'e31',0,1),(86,2018,'h31',0,1),(87,2018,'i31',0,1),(88,2018,'d32',0,1),(89,2018,'e32',0,1),(90,2018,'h32',0,1),(91,2018,'i32',0,1),(92,2018,'d33',0,1),(93,2018,'e33',0,1),(94,2018,'h33',0,1),(95,2018,'i33',0,1),(96,2018,'d34',0,1),(97,2018,'e34',0,1),(98,2018,'h34',-39658.42,1),(99,2018,'i34',-33603.89,1),(100,2018,'d35',0,1),(101,2018,'e35',0,1),(102,2018,'d36',0,1),(103,2018,'e36',0,1);
/*!40000 ALTER TABLE `company_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_cashflow`
--

DROP TABLE IF EXISTS `company_cashflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_cashflow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_cashflow_companyInfo_id_84f5fc8e_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_cashflow_companyInfo_id_84f5fc8e_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_cashflow`
--

LOCK TABLES `company_cashflow` WRITE;
/*!40000 ALTER TABLE `company_cashflow` DISABLE KEYS */;
INSERT INTO `company_cashflow` VALUES (1,2018,'year',2018,1),(2,2018,'d8',24965.25,1),(3,2018,'d11',134281.64,1),(4,2018,'d12',119.42,1);
/*!40000 ALTER TABLE `company_cashflow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_companyinfo`
--

DROP TABLE IF EXISTS `company_companyinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_companyinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `registered_capital` int(11) DEFAULT NULL,
  `paid_in_capital` int(11) DEFAULT NULL,
  `major_business` varchar(50) DEFAULT NULL,
  `work_force` int(11) DEFAULT NULL,
  `junior_college_number` int(11) DEFAULT NULL,
  `developer_number` int(11) DEFAULT NULL,
  `is_high_tech_enterprise` tinyint(1) NOT NULL,
  `abouts` longtext,
  `field_1` smallint(6) DEFAULT NULL,
  `field_2` varchar(20) DEFAULT NULL,
  `credit_code` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `business_license_pic` varchar(100) DEFAULT NULL,
  `incubator_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_companyinfo_name_594d044f_uniq` (`name`),
  KEY `company_companyinfo_incubator_id_4ba91699_fk_incubator` (`incubator_id`),
  KEY `company_companyinfo_user_id_e4d0d778` (`user_id`),
  CONSTRAINT `company_companyinfo_incubator_id_4ba91699_fk_incubator` FOREIGN KEY (`incubator_id`) REFERENCES `incubator_incubator` (`id`),
  CONSTRAINT `company_companyinfo_user_id_e4d0d778_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_companyinfo`
--

LOCK TABLES `company_companyinfo` WRITE;
/*!40000 ALTER TABLE `company_companyinfo` DISABLE KEYS */;
INSERT INTO `company_companyinfo` VALUES (1,'中创恩（天津）科技有限公司','2014-11-06',2000000,1000000,'电子信息技术',14,8,3,1,'电子信息技术',1,'电子信息技术','91120116MA06H0558E','18722631889','static/upload/company/bg9.png',1,4,10),(2,'天津津松伟业科技有限公司',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,'91120116MA06U3485M','15022666265','static/upload/company/bg9_OrSf0u3.png',1,5,0),(3,'康之源（天津）科技发展有限公司',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,'91120116MA05JXJU10','13920384338','static/upload/company/bg9_P17ChjH.png',1,6,0),(4,'卡博瑞（天津）智能科技有限责任公司',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,'91120116351564414W','18522877619','static/upload/company/bg9_DsvS0PT.png',1,7,0),(5,'天津卓越信通科技有限公司',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,'91120116MA05K4NU30','13681032839','static/upload/company/bg9_xbMzpqs.png',1,8,0);
/*!40000 ALTER TABLE `company_companyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_coremember`
--

DROP TABLE IF EXISTS `company_coremember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_coremember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `gender` smallint(6) DEFAULT NULL,
  `age` smallint(6) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `is_study_abroad` tinyint(1) NOT NULL,
  `entrepreneurial_times` smallint(6) DEFAULT NULL,
  `experience` varchar(500) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_coremember_companyInfo_id_c881a2da_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_coremember_companyInfo_id_c881a2da_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_coremember`
--

LOCK TABLES `company_coremember` WRITE;
/*!40000 ALTER TABLE `company_coremember` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_coremember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_drugapproval`
--

DROP TABLE IF EXISTS `company_drugapproval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_drugapproval` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `new_drug` varchar(50) DEFAULT NULL,
  `c_drug` varchar(50) DEFAULT NULL,
  `num` varchar(50) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_drugapproval_companyInfo_id_e33a90e9_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_drugapproval_companyInfo_id_e33a90e9_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_drugapproval`
--

LOCK TABLES `company_drugapproval` WRITE;
/*!40000 ALTER TABLE `company_drugapproval` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_drugapproval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_educationexperience`
--

DROP TABLE IF EXISTS `company_educationexperience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_educationexperience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `education` varchar(50) DEFAULT NULL,
  `university` varchar(50) DEFAULT NULL,
  `major` varchar(50) DEFAULT NULL,
  `core_member_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_educationexp_core_member_id_ae620ffa_fk_company_c` (`core_member_id`),
  CONSTRAINT `company_educationexp_core_member_id_ae620ffa_fk_company_c` FOREIGN KEY (`core_member_id`) REFERENCES `company_coremember` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_educationexperience`
--

LOCK TABLES `company_educationexperience` WRITE;
/*!40000 ALTER TABLE `company_educationexperience` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_educationexperience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_enterpriseawards`
--

DROP TABLE IF EXISTS `company_enterpriseawards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_enterpriseawards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` varchar(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_enterpriseaw_companyInfo_id_5f1670fa_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_enterpriseaw_companyInfo_id_5f1670fa_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_enterpriseawards`
--

LOCK TABLES `company_enterpriseawards` WRITE;
/*!40000 ALTER TABLE `company_enterpriseawards` DISABLE KEYS */;
INSERT INTO `company_enterpriseawards` VALUES (1,'市级','某某奖','2015-11-06',1);
/*!40000 ALTER TABLE `company_enterpriseawards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_evaluationofenterprises`
--

DROP TABLE IF EXISTS `company_evaluationofenterprises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_evaluationofenterprises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `external_environment` smallint(6) DEFAULT NULL,
  `products_and_market` smallint(6) DEFAULT NULL,
  `technology_R_D` smallint(6) DEFAULT NULL,
  `team` smallint(6) DEFAULT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_evaluationof_companyInfo_id_446e2046_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_evaluationofenterprises`
--

LOCK TABLES `company_evaluationofenterprises` WRITE;
/*!40000 ALTER TABLE `company_evaluationofenterprises` DISABLE KEYS */;
INSERT INTO `company_evaluationofenterprises` VALUES (1,10,10,10,10,'2018-11-06 08:35:48.559762',1);
/*!40000 ALTER TABLE `company_evaluationofenterprises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_financialsituation`
--

DROP TABLE IF EXISTS `company_financialsituation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_financialsituation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `income` int(11) DEFAULT NULL,
  `profit` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `r_d_cost` int(11) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_financialsit_companyInfo_id_222ea973_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_financialsit_companyInfo_id_222ea973_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_financialsituation`
--

LOCK TABLES `company_financialsituation` WRITE;
/*!40000 ALTER TABLE `company_financialsituation` DISABLE KEYS */;
INSERT INTO `company_financialsituation` VALUES (1,2018,1000000,100000,3000000,500000,1);
/*!40000 ALTER TABLE `company_financialsituation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_independentevaluationofenterprises`
--

DROP TABLE IF EXISTS `company_independentevaluationofenterprises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_independentevaluationofenterprises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `external_environment` smallint(6) DEFAULT NULL,
  `products_and_market` smallint(6) DEFAULT NULL,
  `technology_R_D` smallint(6) DEFAULT NULL,
  `team` smallint(6) DEFAULT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_independente_companyInfo_id_c8cbcd0e_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_independentevaluationofenterprises`
--

LOCK TABLES `company_independentevaluationofenterprises` WRITE;
/*!40000 ALTER TABLE `company_independentevaluationofenterprises` DISABLE KEYS */;
INSERT INTO `company_independentevaluationofenterprises` VALUES (1,8,4,6,7,'2018-11-06 08:34:39.879296',1);
/*!40000 ALTER TABLE `company_independentevaluationofenterprises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_mirc`
--

DROP TABLE IF EXISTS `company_mirc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_mirc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `num` varchar(50) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_mirc_companyInfo_id_b23cd250_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `company_mirc_companyInfo_id_b23cd250_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_mirc`
--

LOCK TABLES `company_mirc` WRITE;
/*!40000 ALTER TABLE `company_mirc` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_mirc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_otherm`
--

DROP TABLE IF EXISTS `company_otherm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_otherm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x1` smallint(6) DEFAULT NULL,
  `technical_source` smallint(6) DEFAULT NULL,
  `SOAT` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_otherm_companyInfo_id_53c8b1b9_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_otherm`
--

LOCK TABLES `company_otherm` WRITE;
/*!40000 ALTER TABLE `company_otherm` DISABLE KEYS */;
INSERT INTO `company_otherm` VALUES (1,1,2,3,1);
/*!40000 ALTER TABLE `company_otherm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_patent`
--

DROP TABLE IF EXISTS `company_patent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_patent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `_type` varchar(50) DEFAULT NULL,
  `num` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_patent_companyInfo_id_ae9bc17c_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `company_patent_companyInfo_id_ae9bc17c_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_patent`
--

LOCK TABLES `company_patent` WRITE;
/*!40000 ALTER TABLE `company_patent` DISABLE KEYS */;
INSERT INTO `company_patent` VALUES (1,'某某专利','科技','xxxx11111','2018-11-06',1);
/*!40000 ALTER TABLE `company_patent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_personalawards`
--

DROP TABLE IF EXISTS `company_personalawards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_personalawards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `level_title` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_personalawar_companyInfo_id_d63b1736_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_personalawar_companyInfo_id_d63b1736_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_personalawards`
--

LOCK TABLES `company_personalawards` WRITE;
/*!40000 ALTER TABLE `company_personalawards` DISABLE KEYS */;
INSERT INTO `company_personalawards` VALUES (1,'李某某','市级','2015-11-06',1);
/*!40000 ALTER TABLE `company_personalawards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_productsandmarket`
--

DROP TABLE IF EXISTS `company_productsandmarket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_productsandmarket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product` longtext,
  `model` longtext,
  `analysis_forecast` longtext,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_productsandm_companyInfo_id_f940e9f4_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_productsandmarket`
--

LOCK TABLES `company_productsandmarket` WRITE;
/*!40000 ALTER TABLE `company_productsandmarket` DISABLE KEYS */;
INSERT INTO `company_productsandmarket` VALUES (1,'电子信息技术','电子信息技术','电子信息技术',1);
/*!40000 ALTER TABLE `company_productsandmarket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_profit`
--

DROP TABLE IF EXISTS `company_profit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_profit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_profit_companyInfo_id_528daf88_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `company_profit_companyInfo_id_528daf88_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_profit`
--

LOCK TABLES `company_profit` WRITE;
/*!40000 ALTER TABLE `company_profit` DISABLE KEYS */;
INSERT INTO `company_profit` VALUES (1,2018,'year',2018,1),(2,2018,'c7',0,1),(3,2018,'c8',0,1),(4,2018,'c11',0,1),(5,2018,'c12',0,1),(6,2018,'c13',0,1),(7,2018,'c14',287075.72,1),(8,2018,'c15',0,1),(9,2018,'c16',0,1),(10,2018,'c17',0,1),(11,2018,'c18',0,1),(12,2018,'c19',0,1),(13,2018,'c20',-1.76,1),(14,2018,'c21',0,1),(15,2018,'c22',0,1),(16,2018,'c24',8994.04,1),(17,2018,'c25',0,1),(18,2018,'c26',0,1),(19,2018,'c27',0,1),(20,2018,'c29',0,1);
/*!40000 ALTER TABLE `company_profit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_project`
--

DROP TABLE IF EXISTS `company_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_type` varchar(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  `conclusion` longtext,
  `finished_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_project_companyInfo_id_235f7a33_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_project_companyInfo_id_235f7a33_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_project`
--

LOCK TABLES `company_project` WRITE;
/*!40000 ALTER TABLE `company_project` DISABLE KEYS */;
INSERT INTO `company_project` VALUES (1,'省级','某某工程','2017-11-06',1,'完成','2018-11-06');
/*!40000 ALTER TABLE `company_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_rejectreason`
--

DROP TABLE IF EXISTS `company_rejectreason`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_rejectreason` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext,
  `is_alive` tinyint(1) NOT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_rejectreason_companyInfo_id_c4ac0844_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_rejectreason_companyInfo_id_c4ac0844_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_rejectreason`
--

LOCK TABLES `company_rejectreason` WRITE;
/*!40000 ALTER TABLE `company_rejectreason` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_rejectreason` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_serverrequest`
--

DROP TABLE IF EXISTS `company_serverrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_serverrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `duration` smallint(6) DEFAULT NULL,
  `ratio` double DEFAULT NULL,
  `interest_rate` double DEFAULT NULL,
  `plan` longtext,
  `small_loan` smallint(6) DEFAULT NULL,
  `share_model` smallint(6) DEFAULT NULL,
  `request` longtext,
  `companyInfo_id` int(11) NOT NULL,
  `otherrequest` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_serverreques_companyInfo_id_bbcdc638_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_serverrequest`
--

LOCK TABLES `company_serverrequest` WRITE;
/*!40000 ALTER TABLE `company_serverrequest` DISABLE KEYS */;
INSERT INTO `company_serverrequest` VALUES (1,1000,365,25,10,'无',NULL,NULL,'',1,'');
/*!40000 ALTER TABLE `company_serverrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_shareholder`
--

DROP TABLE IF EXISTS `company_shareholder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_shareholder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `share_ratio` double DEFAULT NULL,
  `form_of_contribution` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_shareholder_companyInfo_id_29b72b99_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_shareholder_companyInfo_id_29b72b99_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_shareholder`
--

LOCK TABLES `company_shareholder` WRITE;
/*!40000 ALTER TABLE `company_shareholder` DISABLE KEYS */;
INSERT INTO `company_shareholder` VALUES (1,'王某某',10,1,1),(2,'李某某',10,2,1);
/*!40000 ALTER TABLE `company_shareholder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_standardsetting`
--

DROP TABLE IF EXISTS `company_standardsetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_standardsetting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `level` varchar(10) DEFAULT NULL,
  `num` varchar(50) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_standardsett_companyInfo_id_a73978b0_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_standardsett_companyInfo_id_a73978b0_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_standardsetting`
--

LOCK TABLES `company_standardsetting` WRITE;
/*!40000 ALTER TABLE `company_standardsetting` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_standardsetting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_technologyrd`
--

DROP TABLE IF EXISTS `company_technologyrd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_technologyrd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` longtext,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_technologyrd_companyInfo_id_18ee93e7_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_technologyrd`
--

LOCK TABLES `company_technologyrd` WRITE;
/*!40000 ALTER TABLE `company_technologyrd` DISABLE KEYS */;
INSERT INTO `company_technologyrd` VALUES (1,'电子信息技术',1);
/*!40000 ALTER TABLE `company_technologyrd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_workexperience`
--

DROP TABLE IF EXISTS `company_workexperience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_workexperience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(50) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `date_s` date DEFAULT NULL,
  `date_e` date DEFAULT NULL,
  `core_member_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_workexperien_core_member_id_a3194aa2_fk_company_c` (`core_member_id`),
  CONSTRAINT `company_workexperien_core_member_id_a3194aa2_fk_company_c` FOREIGN KEY (`core_member_id`) REFERENCES `company_coremember` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_workexperience`
--

LOCK TABLES `company_workexperience` WRITE;
/*!40000 ALTER TABLE `company_workexperience` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_workexperience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-06 08:29:57.102324','1','中创恩（天津）科技有限公司',2,'[{\"changed\": {\"fields\": [\"create_date\", \"registered_capital\", \"paid_in_capital\", \"major_business\", \"work_force\", \"junior_college_number\", \"developer_number\", \"is_high_tech_enterprise\", \"abouts\", \"field_1\", \"field_2\"]}}, {\"added\": {\"name\": \"\\u4e3b\\u8981\\u80a1\\u4e1c\\u53ca\\u80a1\\u6743\\u6bd4\\u4f8b\\uff08\\u524d\\u4e94\\u540d\\uff09\", \"object\": \"Shareholder object\"}}, {\"added\": {\"name\": \"\\u4e3b\\u8981\\u80a1\\u4e1c\\u53ca\\u80a1\\u6743\\u6bd4\\u4f8b\\uff08\\u524d\\u4e94\\u540d\\uff09\", \"object\": \"Shareholder object\"}}]',11,4),(2,'2018-11-06 08:33:48.002849','1','中创恩（天津）科技有限公司',2,'[{\"added\": {\"name\": \"\\u4f01\\u4e1a\\u83b7\\u5956\\u60c5\\u51b5\", \"object\": \"EnterpriseAwards object\"}}, {\"added\": {\"name\": \"\\u6838\\u5fc3\\u56e2\\u961f\\u4e2a\\u4eba\\u83b7\\u5956\\u60c5\\u51b5\", \"object\": \"PersonalAwards object\"}}, {\"added\": {\"name\": \"\\u4f01\\u4e1a\\u66fe\\u7ecf\\u627f\\u62c5\\u6216\\u6b63\\u5728\\u627f\\u62c5\\u7684\\u79d1\\u6280\\u8ba1\\u5212\\u9879\\u76ee\", \"object\": \"Project object\"}}, {\"added\": {\"name\": \"\\u4e13\\u5229\", \"object\": \"Patent object\"}}, {\"added\": {\"name\": \"\\u5176\\u4ed6\", \"object\": \"Otherm object\"}}, {\"added\": {\"name\": \"\\u4e8c\\u3001\\u8d22\\u52a1\\u72b6\\u51b5\", \"object\": \"FinancialSituation object\"}}, {\"added\": {\"name\": \"\\u4e09\\u3001\\u4ea7\\u54c1\\u4e0e\\u5e02\\u573a\", \"object\": \"ProductsAndMarket object\"}}, {\"added\": {\"name\": \"\\u56db\\u3001\\u6280\\u672f\\u4e0e\\u7814\\u53d1\", \"object\": \"TechnologyRD object\"}}, {\"added\": {\"name\": \"\\u4e94\\u3001\\u670d\\u52a1\\u9700\\u6c42\", \"object\": \"ServerRequest object\"}}]',11,4),(3,'2018-11-06 08:34:39.883422','1','自主评价',1,'[{\"added\": {}}]',18,4),(4,'2018-11-06 08:35:48.560739','1','校正评价',2,'[{\"changed\": {\"fields\": [\"external_environment\", \"products_and_market\", \"technology_R_D\", \"team\"]}}]',16,2),(5,'2018-11-06 08:36:44.354186','1','中创恩（天津）科技有限公司',1,'[{\"added\": {}}]',7,1),(6,'2018-11-06 08:36:56.320946','1','2018-11-06 16:36:56',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',35,1),(7,'2018-11-06 08:37:44.813368','1','中创恩（天津）科技有限公司 2018-11-06 16:36:56 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',36,3),(8,'2018-11-06 08:38:00.488460','1','中创恩（天津）科技有限公司 2018-11-06 16:36:56 反馈信息',2,'[{\"changed\": {\"fields\": [\"iscompanyview\"]}}]',36,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'company','balance'),(10,'company','cashflow'),(11,'company','companyinfo'),(12,'company','coremember'),(13,'company','drugapproval'),(14,'company','educationexperience'),(15,'company','enterpriseawards'),(16,'company','evaluationofenterprises'),(17,'company','financialsituation'),(18,'company','independentevaluationofenterprises'),(19,'company','mirc'),(30,'company','otherm'),(20,'company','patent'),(21,'company','personalawards'),(22,'company','productsandmarket'),(23,'company','profit'),(24,'company','project'),(31,'company','rejectreason'),(25,'company','serverrequest'),(26,'company','shareholder'),(27,'company','standardsetting'),(28,'company','technologyrd'),(29,'company','workexperience'),(5,'contenttypes','contenttype'),(32,'incubator','incubator'),(7,'index','bonus'),(8,'index','subtraction'),(33,'institution','bankreport'),(34,'institution','institution'),(35,'institution','investreport'),(36,'institution','reportback'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-06 08:09:07.057297'),(2,'auth','0001_initial','2018-11-06 08:09:07.577301'),(3,'admin','0001_initial','2018-11-06 08:09:07.696180'),(4,'admin','0002_logentry_remove_auto_add','2018-11-06 08:09:07.718158'),(5,'contenttypes','0002_remove_content_type_name','2018-11-06 08:09:07.801689'),(6,'auth','0002_alter_permission_name_max_length','2018-11-06 08:09:07.851361'),(7,'auth','0003_alter_user_email_max_length','2018-11-06 08:09:07.904744'),(8,'auth','0004_alter_user_username_opts','2018-11-06 08:09:07.928103'),(9,'auth','0005_alter_user_last_login_null','2018-11-06 08:09:07.973337'),(10,'auth','0006_require_contenttypes_0002','2018-11-06 08:09:07.978046'),(11,'auth','0007_alter_validators_add_error_messages','2018-11-06 08:09:07.993538'),(12,'auth','0008_alter_user_username_max_length','2018-11-06 08:09:08.096899'),(13,'incubator','0001_initial','2018-11-06 08:09:08.177699'),(14,'company','0001_initial','2018-11-06 08:09:10.116900'),(15,'company','0002_auto_20181106_1548','2018-11-06 08:09:12.453532'),(16,'incubator','0002_auto_20181106_1548','2018-11-06 08:09:12.545726'),(17,'index','0001_initial','2018-11-06 08:09:12.709925'),(18,'institution','0001_initial','2018-11-06 08:09:12.970047'),(19,'institution','0002_auto_20181106_1548','2018-11-06 08:09:14.750078'),(20,'sessions','0001_initial','2018-11-06 08:09:14.794628');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0e861sygoboy9ybofyhdiimrdxlo35wb','ZGM3NGEzZGQ0MmM3OWE4NDRlNjdjNTQ3YjUyY2RjYWUxYjgxNDZjZTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5Yjg2MTkwYWU2N2U0M2NiY2MwMjRmMmRkOGRjMmFlN2Q0ODgwMmM3In0=','2018-11-20 08:36:12.133769'),('efilrki10nckriv0bhpg9cl5284mwuo0','NjExYWNkYTQ3YmM4NDA5NzVjNDU1YTNiMjY5NmZjNmMyNTM1N2I0Yzp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhOTJjNmJkMTBhMGNjMzM5Y2I4ZjA4NTkyMjQ1YWUwZmUyZjBiMzY1In0=','2018-11-20 08:43:54.854765'),('o4y5epbm0lgomujdcqcrt0al43jrfmu8','MmRiZjU1ZTcwNjIwMGU0MTRkN2FlYThhZjg1OTdjN2FmYTM1NzlkZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxODU0NTVhOTY0OTBlNGNmNDYxMTk2YmU4ZjEyNDUxYjlmYjkwODE5In0=','2018-11-20 08:26:47.985676');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incubator_incubator`
--

DROP TABLE IF EXISTS `incubator_incubator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `incubator_incubator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `credit_code` varchar(50) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `incubator_incubator_name_ed12c7a4_uniq` (`name`),
  CONSTRAINT `incubator_incubator_user_id_bf7d94d1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incubator_incubator`
--

LOCK TABLES `incubator_incubator` WRITE;
/*!40000 ALTER TABLE `incubator_incubator` DISABLE KEYS */;
INSERT INTO `incubator_incubator` VALUES (1,'默认孵化器','123',NULL,2);
/*!40000 ALTER TABLE `incubator_incubator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_bonus`
--

DROP TABLE IF EXISTS `index_bonus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_bonus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item` smallint(6) NOT NULL,
  `note` longtext NOT NULL,
  `value` smallint(6) NOT NULL,
  `companyInfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_bonus_companyInfo_id_06a1f375_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `index_bonus_companyInfo_id_06a1f375_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_bonus`
--

LOCK TABLES `index_bonus` WRITE;
/*!40000 ALTER TABLE `index_bonus` DISABLE KEYS */;
INSERT INTO `index_bonus` VALUES (1,3,'优秀',5,1);
/*!40000 ALTER TABLE `index_bonus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_subtraction`
--

DROP TABLE IF EXISTS `index_subtraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_subtraction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item` smallint(6) DEFAULT NULL,
  `note` longtext,
  `value` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_subtraction_companyInfo_id_23ff605a_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `index_subtraction_companyInfo_id_23ff605a_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_subtraction`
--

LOCK TABLES `index_subtraction` WRITE;
/*!40000 ALTER TABLE `index_subtraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `index_subtraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_bankreport`
--

DROP TABLE IF EXISTS `institution_bankreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_bankreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `i1` smallint(6),
  `i2` smallint(6),
  `i3` smallint(6),
  `i4` smallint(6),
  `i5` tinyint(1) NOT NULL,
  `i6` tinyint(1) NOT NULL,
  `i7` tinyint(1) NOT NULL,
  `i8` tinyint(1) NOT NULL,
  `i9` tinyint(1) NOT NULL,
  `i10` tinyint(1) NOT NULL,
  `i11` tinyint(1) NOT NULL,
  `i12` tinyint(1) NOT NULL,
  `i13` tinyint(1) NOT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `companyInfo_id` int(11) NOT NULL,
  `i14` tinyint(1) NOT NULL,
  `i15` tinyint(1) NOT NULL,
  `i16` tinyint(1) NOT NULL,
  `i17` tinyint(1) NOT NULL,
  `i18` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `institution_bankrepo_companyInfo_id_f19fe783_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `institution_bankrepo_companyInfo_id_f19fe783_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_bankreport`
--

LOCK TABLES `institution_bankreport` WRITE;
/*!40000 ALTER TABLE `institution_bankreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `institution_bankreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_bankreport_institution`
--

DROP TABLE IF EXISTS `institution_bankreport_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_bankreport_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bankreport_id` int(11) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `institution_bankreport_i_bankreport_id_institutio_57c0f417_uniq` (`bankreport_id`,`institution_id`),
  KEY `institution_bankrepo_institution_id_f6ae4cd0_fk_instituti` (`institution_id`),
  CONSTRAINT `institution_bankrepo_bankreport_id_b4c1209b_fk_instituti` FOREIGN KEY (`bankreport_id`) REFERENCES `institution_bankreport` (`id`),
  CONSTRAINT `institution_bankrepo_institution_id_f6ae4cd0_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_bankreport_institution`
--

LOCK TABLES `institution_bankreport_institution` WRITE;
/*!40000 ALTER TABLE `institution_bankreport_institution` DISABLE KEYS */;
/*!40000 ALTER TABLE `institution_bankreport_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_institution`
--

DROP TABLE IF EXISTS `institution_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `institution_institution_name_56c61d5e_uniq` (`name`),
  CONSTRAINT `institution_institution_user_id_114f795c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_institution`
--

LOCK TABLES `institution_institution` WRITE;
/*!40000 ALTER TABLE `institution_institution` DISABLE KEYS */;
INSERT INTO `institution_institution` VALUES (1,1,'投资机构','123',3);
/*!40000 ALTER TABLE `institution_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_investreport`
--

DROP TABLE IF EXISTS `institution_investreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_investreport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `i5` tinyint(1) NOT NULL,
  `i6` tinyint(1) NOT NULL,
  `i7` tinyint(1) NOT NULL,
  `i8` tinyint(1) NOT NULL,
  `i9` tinyint(1) NOT NULL,
  `i10` tinyint(1) NOT NULL,
  `i11` tinyint(1) NOT NULL,
  `i12` tinyint(1) NOT NULL,
  `i13` tinyint(1) NOT NULL,
  `i14` tinyint(1) NOT NULL,
  `i15` tinyint(1) NOT NULL,
  `i16` tinyint(1) NOT NULL,
  `i17` tinyint(1) NOT NULL,
  `i18` tinyint(1) NOT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `companyInfo_id` int(11) NOT NULL,
  `i1` smallint(6),
  `i2` smallint(6),
  `i3` smallint(6),
  `i4` smallint(6),
  PRIMARY KEY (`id`),
  KEY `institution_investre_companyInfo_id_f0e8ce27_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `institution_investre_companyInfo_id_f0e8ce27_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_investreport`
--

LOCK TABLES `institution_investreport` WRITE;
/*!40000 ALTER TABLE `institution_investreport` DISABLE KEYS */;
INSERT INTO `institution_investreport` VALUES (1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,'2018-11-06 08:36:56.316885',1,10,10,10,10);
/*!40000 ALTER TABLE `institution_investreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_investreport_institution`
--

DROP TABLE IF EXISTS `institution_investreport_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_investreport_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `investreport_id` int(11) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `institution_investreport_investreport_id_institut_f9221963_uniq` (`investreport_id`,`institution_id`),
  KEY `institution_investre_institution_id_c006bdac_fk_instituti` (`institution_id`),
  CONSTRAINT `institution_investre_institution_id_c006bdac_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`),
  CONSTRAINT `institution_investre_investreport_id_0dfd221b_fk_instituti` FOREIGN KEY (`investreport_id`) REFERENCES `institution_investreport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_investreport_institution`
--

LOCK TABLES `institution_investreport_institution` WRITE;
/*!40000 ALTER TABLE `institution_investreport_institution` DISABLE KEYS */;
INSERT INTO `institution_investreport_institution` VALUES (1,1,1);
/*!40000 ALTER TABLE `institution_investreport_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_reportback`
--

DROP TABLE IF EXISTS `institution_reportback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institution_reportback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `will` smallint(6) DEFAULT NULL,
  `type` smallint(6) DEFAULT NULL,
  `note` longtext,
  `iscompanyview` smallint(6) NOT NULL,
  `isinstitutionview` smallint(6) NOT NULL,
  `bankreport_id` int(11) DEFAULT NULL,
  `institution_id` int(11) DEFAULT NULL,
  `investreport_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `institution_reportba_bankreport_id_170c33df_fk_instituti` (`bankreport_id`),
  KEY `institution_reportba_institution_id_aebc6cf1_fk_instituti` (`institution_id`),
  KEY `institution_reportba_investreport_id_03a548cf_fk_instituti` (`investreport_id`),
  CONSTRAINT `institution_reportba_bankreport_id_170c33df_fk_instituti` FOREIGN KEY (`bankreport_id`) REFERENCES `institution_bankreport` (`id`),
  CONSTRAINT `institution_reportba_institution_id_aebc6cf1_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`),
  CONSTRAINT `institution_reportba_investreport_id_03a548cf_fk_instituti` FOREIGN KEY (`investreport_id`) REFERENCES `institution_investreport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_reportback`
--

LOCK TABLES `institution_reportback` WRITE;
/*!40000 ALTER TABLE `institution_reportback` DISABLE KEYS */;
INSERT INTO `institution_reportback` VALUES (1,1,1,'和企业沟通',2,1,NULL,1,1);
/*!40000 ALTER TABLE `institution_reportback` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-06  8:49:42
