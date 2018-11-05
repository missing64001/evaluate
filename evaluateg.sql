-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: evaluateg
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,25),(2,1,26),(3,1,27),(4,1,28),(5,1,29),(6,1,30),(7,1,31),(8,1,32),(9,1,33),(10,1,34),(11,1,35),(12,1,36),(13,1,37),(14,1,38),(15,1,39),(16,1,40),(17,1,41),(18,1,42),(19,1,43),(20,1,44),(21,1,45),(22,1,46),(23,1,47),(24,1,48),(25,1,49),(26,1,50),(27,1,51),(28,1,52),(29,1,53),(30,1,54),(31,1,55),(32,1,56),(33,1,57),(34,1,58),(35,1,59),(36,1,60),(37,1,61),(38,1,62),(39,1,63),(40,1,64),(41,1,65),(42,1,66),(43,1,67),(44,1,68),(45,1,69),(46,1,70),(47,1,71),(48,1,72),(49,1,73),(50,1,74),(51,1,75),(52,1,76),(53,1,77),(54,1,78),(55,1,79),(56,1,80),(57,1,81),(58,1,82),(59,1,83),(60,1,84),(61,1,85),(62,1,86),(63,1,87),(123,1,101),(74,2,26),(76,2,29),(77,2,32),(78,2,35),(79,2,38),(80,2,41),(81,2,44),(82,2,47),(83,2,50),(84,2,53),(85,2,56),(86,2,59),(87,2,62),(64,2,65),(65,2,68),(66,2,71),(67,2,74),(68,2,77),(69,2,80),(70,2,83),(71,2,86),(72,2,88),(73,2,89),(75,2,90),(122,2,101),(96,3,26),(99,3,29),(102,3,32),(105,3,35),(108,3,38),(110,3,41),(111,3,44),(112,3,47),(113,3,50),(114,3,53),(115,3,56),(116,3,59),(117,3,62),(88,3,65),(118,3,68),(90,3,71),(91,3,74),(92,3,77),(93,3,80),(94,3,83),(95,3,86),(97,3,91),(98,3,92),(100,3,93),(101,3,94),(103,3,95),(104,3,96),(106,3,97),(107,3,98),(109,3,99),(119,3,100),(120,3,101),(121,3,102);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 加分项',7,'add_bonus'),(20,'Can change 加分项',7,'change_bonus'),(21,'Can delete 加分项',7,'delete_bonus'),(22,'Can add 减分项',8,'add_subtraction'),(23,'Can change 减分项',8,'change_subtraction'),(24,'Can delete 减分项',8,'delete_subtraction'),(25,'Can add 企业获奖情况',9,'add_enterpriseawards'),(26,'Can change 企业获奖情况',9,'change_enterpriseawards'),(27,'Can delete 企业获奖情况',9,'delete_enterpriseawards'),(28,'Can add 主要股东及股权比例（前五名）',10,'add_shareholder'),(29,'Can change 主要股东及股权比例（前五名）',10,'change_shareholder'),(30,'Can delete 主要股东及股权比例（前五名）',10,'delete_shareholder'),(31,'Can add 企业曾经承担或正在承担的科技计划项目',11,'add_project'),(32,'Can change 企业曾经承担或正在承担的科技计划项目',11,'change_project'),(33,'Can delete 企业曾经承担或正在承担的科技计划项目',11,'delete_project'),(34,'Can add 二、财务状况',12,'add_financialsituation'),(35,'Can change 二、财务状况',12,'change_financialsituation'),(36,'Can delete 二、财务状况',12,'delete_financialsituation'),(37,'Can add balance',13,'add_balance'),(38,'Can change balance',13,'change_balance'),(39,'Can delete balance',13,'delete_balance'),(40,'Can add profit',14,'add_profit'),(41,'Can change profit',14,'change_profit'),(42,'Can delete profit',14,'delete_profit'),(43,'Can add 四、技术与研发',15,'add_technologyrd'),(44,'Can change 四、技术与研发',15,'change_technologyrd'),(45,'Can delete 四、技术与研发',15,'delete_technologyrd'),(46,'Can add 标准制定情况',16,'add_standardsetting'),(47,'Can change 标准制定情况',16,'change_standardsetting'),(48,'Can delete 标准制定情况',16,'delete_standardsetting'),(49,'Can add 自主评价',17,'add_independentevaluationofenterprises'),(50,'Can change 自主评价',17,'change_independentevaluationofenterprises'),(51,'Can delete 自主评价',17,'delete_independentevaluationofenterprises'),(52,'Can add 教育经历（可增加）',18,'add_educationexperience'),(53,'Can change 教育经历（可增加）',18,'change_educationexperience'),(54,'Can delete 教育经历（可增加）',18,'delete_educationexperience'),(55,'Can add 校正评价',19,'add_evaluationofenterprises'),(56,'Can change 校正评价',19,'change_evaluationofenterprises'),(57,'Can delete 校正评价',19,'delete_evaluationofenterprises'),(58,'Can add 工作经历（可增加）',20,'add_workexperience'),(59,'Can change 工作经历（可增加）',20,'change_workexperience'),(60,'Can delete 工作经历（可增加）',20,'delete_workexperience'),(61,'Can add 专利',21,'add_patent'),(62,'Can change 专利',21,'change_patent'),(63,'Can delete 专利',21,'delete_patent'),(64,'Can add 医疗器械注册证',22,'add_mirc'),(65,'Can change 医疗器械注册证',22,'change_mirc'),(66,'Can delete 医疗器械注册证',22,'delete_mirc'),(67,'Can add 一、基本信息',23,'add_companyinfo'),(68,'Can change 一、基本信息',23,'change_companyinfo'),(69,'Can delete 一、基本信息',23,'delete_companyinfo'),(70,'Can add 核心团队个人获奖情况',24,'add_personalawards'),(71,'Can change 核心团队个人获奖情况',24,'change_personalawards'),(72,'Can delete 核心团队个人获奖情况',24,'delete_personalawards'),(73,'Can add 药品批文',25,'add_drugapproval'),(74,'Can change 药品批文',25,'change_drugapproval'),(75,'Can delete 药品批文',25,'delete_drugapproval'),(76,'Can add 三、产品与市场',26,'add_productsandmarket'),(77,'Can change 三、产品与市场',26,'change_productsandmarket'),(78,'Can delete 三、产品与市场',26,'delete_productsandmarket'),(79,'Can add cash flow',27,'add_cashflow'),(80,'Can change cash flow',27,'change_cashflow'),(81,'Can delete cash flow',27,'delete_cashflow'),(82,'Can add   核心团队(至少三人)',28,'add_coremember'),(83,'Can change   核心团队(至少三人)',28,'change_coremember'),(84,'Can delete   核心团队(至少三人)',28,'delete_coremember'),(85,'Can add 五、服务需求',29,'add_serverrequest'),(86,'Can change 五、服务需求',29,'change_serverrequest'),(87,'Can delete 五、服务需求',29,'delete_serverrequest'),(88,'Can add 孵化器',30,'add_incubator'),(89,'Can change 孵化器',30,'change_incubator'),(90,'Can delete 孵化器',30,'delete_incubator'),(91,'Can add 机构',31,'add_institution'),(92,'Can change 机构',31,'change_institution'),(93,'Can delete 机构',31,'delete_institution'),(94,'Can add 投资类金融报告',32,'add_investreport'),(95,'Can change 投资类金融报告',32,'change_investreport'),(96,'Can delete 投资类金融报告',32,'delete_investreport'),(97,'Can add 银行类金融报告',33,'add_bankreport'),(98,'Can change 银行类金融报告',33,'change_bankreport'),(99,'Can delete 银行类金融报告',33,'delete_bankreport'),(100,'Can add report back',34,'add_reportback'),(101,'Can change report back',34,'change_reportback'),(102,'Can delete report back',34,'delete_reportback');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$Csl1siaRooo8$JMt3WhEO+PFsQHwIsXlmOoI2BiuD2E1lHDXW75tmiDQ=','2018-10-19 07:41:55.435956',1,'miss','','','1@qq.com',1,1,'2018-10-17 03:36:54.509298'),(2,'pbkdf2_sha256$36000$PwDIl7Oum49F$kOtzajp6IkqD/bH8tcsYQ8Xy1fgQ0Yx3OwNM5zZQ4kw=','2018-10-17 03:56:38.312949',0,'fhq','','','xx@qq.com',0,1,'2018-10-17 03:56:37.994957'),(3,'pbkdf2_sha256$36000$hpIkAftL7xXC$/ekUTS1gSkhnHGnefxf7rXsh2qximaGnYTZrZLszX5Y=','2018-10-19 05:53:29.198750',0,'fhqz','','','xx@qq.com',1,1,'2018-10-17 03:59:16.886954'),(4,'pbkdf2_sha256$36000$tjEvtU9hzQoA$eH2If+k6LLF2frRaueyJQ74FKRxUbdB+WygBZaugfmQ=',NULL,0,'c1','','','xx@qq.com',1,1,'2018-10-17 04:00:19.728162'),(5,'pbkdf2_sha256$36000$3LKChlARLW7l$Lkq/qp9zcRD0nvKJW7V87CRBEithzOfXK9g/IoPI9dE=',NULL,0,'c2','','','xx@qq.com',1,1,'2018-10-17 04:02:13.170739'),(6,'pbkdf2_sha256$36000$JhbiuZYmEZXU$C7tcCR4xwbROjgdn7w9Na6iRY7LuMtRITaO6Oflp0yA=',NULL,0,'c3','','','xx@qq.com',1,1,'2018-10-17 04:03:00.328144'),(7,'pbkdf2_sha256$36000$sZU3ZUgrxlrk$loNsUT+/pUwkYrDkG9ewW67n5a6htvLS8LzU+0OgXJs=',NULL,0,'c4','','','xx@qq.com',1,1,'2018-10-17 04:05:20.841379'),(8,'pbkdf2_sha256$36000$OURA2hqEb3Ks$71vZODI4ADiSsud97KXQZ4hhJQV8hcUK2BYyhJp2ClQ=',NULL,0,'c5','','','xx@qq.com',1,1,'2018-10-17 05:12:16.708892'),(9,'pbkdf2_sha256$36000$2iGuKTirkV3y$YwbL3QROoQgNkGAELpVzzG1i7GByij1m2ahclDZ2EUQ=',NULL,0,'jg1','','','xx@qq.com',1,1,'2018-10-18 02:20:46.325034'),(10,'pbkdf2_sha256$36000$thW0AEyyZrP7$2FPn9E2x3kavoIMpfE/WVEmcnPETcyaYljZVZ17nlq0=',NULL,0,'jg2','','','xx@qq.com',1,1,'2018-10-18 02:22:40.853597'),(11,'pbkdf2_sha256$36000$2Rxat1dhsYfK$JOTGFtHE1fSb8jbBmWEusmdBK7IN5BuJGFxFEWqs+rA=',NULL,0,'jg3','','','xx@qq.com',1,1,'2018-10-18 02:25:20.193594'),(12,'pbkdf2_sha256$36000$ofSnLsTSBDBt$fFQxUH3j2CgHiTH+Eq2y0KlYgko781zsCCnvAfHENT0=',NULL,0,'jg4','','','xx@qq.com',1,1,'2018-10-18 02:26:00.114085'),(13,'pbkdf2_sha256$36000$4yyWZI6RcJXQ$60rXWijhhNTAI/eLlTWRLWUn98p0KVcb5/nCVqE1KAA=',NULL,0,'jg5','','','xx@qq.com',1,1,'2018-10-18 02:26:10.341964'),(14,'pbkdf2_sha256$36000$Wvvnmw9ZNOiw$/UKog94FU49Cuv9637xVJiu2/bof4lrqrZ7JlDWt0oc=',NULL,0,'jgg1','','','xx@qq.com',1,1,'2018-10-18 02:31:20.498058'),(15,'pbkdf2_sha256$36000$7ECThgBWsOrD$5mleMfTd2ZC7DlZUi90TgSJoj0NjIJC/SdrxBzI9gp8=',NULL,0,'jgg2','','','xx@qq.com',1,1,'2018-10-18 02:32:36.110108'),(16,'pbkdf2_sha256$36000$E1mtgrKrmPWQ$C+qDIGdFwtpWZ2usC1ej4AkANID/Vf10W08VRpBsu54=',NULL,0,'jgg3','','','xx@qq.com',1,1,'2018-10-18 02:32:47.255966'),(17,'pbkdf2_sha256$36000$qognblc2J6Rk$jCZngc5ZQm+BdcYrfvwZYPsMQUetfNTfj9tLXyYKN+U=','2018-10-19 00:57:05.041324',0,'jgg4','','','xx@qq.com',1,1,'2018-10-18 02:33:02.128779'),(18,'pbkdf2_sha256$36000$DF4KhxugWASP$OJL3VcpemvW4lOe/hKOsTsd2hp9o/Mx8qkqFwVXfeL4=','2018-10-19 05:57:03.349058',0,'jgtz1','','','xx@qq.com',1,1,'2018-10-19 03:37:58.765968'),(19,'pbkdf2_sha256$36000$2aZiivRRtAdd$VHLEH1P0owkkOGkPMD8CP0viVpZflgC9t31aA45nUZ4=',NULL,0,'admin','','','xx@qq.com',1,1,'2018-10-19 04:08:23.802019'),(20,'pbkdf2_sha256$36000$iZImhuPTjOot$hh60TJ07BtwITQuxaklo2X0u1Y3TFrM38fm5zwGMIig=',NULL,0,'cc1','','','xx@qq.com',1,1,'2018-10-19 05:39:31.027285'),(21,'pbkdf2_sha256$36000$8Qex0ZuLvG8j$dxbLBe4e/+rIDDvcshF2q2fIBtaclkf2wOe0c5Seo2g=',NULL,0,'fhqz1','','','xx@qq.com',1,1,'2018-10-19 05:53:05.339051');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,3,2),(2,4,1),(3,5,1),(4,6,1),(5,7,1),(6,8,1),(7,9,3),(8,10,3),(9,11,3),(10,12,3),(11,13,3),(12,14,3),(13,15,3),(14,16,3),(15,17,3),(16,18,3),(17,19,1),(18,20,1),(19,21,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_balance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_balance_companyInfo_id_1740a10c_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_balance_companyInfo_id_1740a10c_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=207 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_balance`
--

LOCK TABLES `company_balance` WRITE;
/*!40000 ALTER TABLE `company_balance` DISABLE KEYS */;
INSERT INTO `company_balance` VALUES (1,2018,'h22',0,5),(2,2018,'i24',0,5),(3,2018,'h9',5670,5),(4,2018,'e22',0,5),(5,2018,'d11',0,5),(6,2018,'h33',0,5),(7,2018,'d16',0,5),(8,2018,'e23',0,5),(9,2018,'e25',7462.36,5),(10,2018,'i34',-33603.89,5),(11,2018,'i15',61548.91,5),(12,2018,'d14',0,5),(13,2018,'h11',77692,5),(14,2018,'h34',-39658.42,5),(15,2018,'e35',0,5),(16,2018,'i26',0,5),(17,2018,'i30',1000000,5),(18,2018,'i9',32000,5),(19,2018,'h15',34319.88,5),(20,2018,'i14',0,5),(21,2018,'h8',0,5),(22,2018,'d22',0,5),(23,2018,'e31',0,5),(24,2018,'h30',1000000,5),(25,2018,'e7',0,5),(26,2018,'i17',0,5),(27,2018,'d12',0,5),(28,2018,'i11',105259.88,5),(29,2018,'d10',0,5),(30,2018,'e8',0,5),(31,2018,'e16',0,5),(32,2018,'i7',0,5),(33,2018,'i8',0,5),(34,2018,'d6',5298.54,5),(35,2018,'e6',1238.49,5),(36,2018,'e20',0,5),(37,2018,'d9',79578,5),(38,2018,'e13',1016000,5),(39,2018,'d31',0,5),(40,2018,'i16',0,5),(41,2018,'e36',0,5),(42,2018,'d27',0,5),(43,2018,'h23',0,5),(44,2018,'d23',0,5),(45,2018,'h21',0,5),(46,2018,'i12',0,5),(47,2018,'h7',0,5),(48,2018,'h25',0,5),(49,2018,'i32',0,5),(50,2018,'h26',0,5),(51,2018,'e14',0,5),(52,2018,'d33',0,5),(53,2018,'d20',0,5),(54,2018,'h6',0,5),(55,2018,'e21',0,5),(56,2018,'i31',0,5),(57,2018,'e34',0,5),(58,2018,'h10',0,5),(59,2018,'e11',0,5),(60,2018,'d7',0,5),(61,2018,'e27',0,5),(62,2018,'e19',0,5),(63,2018,'d13',992000,5),(64,2018,'i21',0,5),(65,2018,'d34',0,5),(66,2018,'e12',0,5),(67,2018,'d15',0,5),(68,2018,'d8',0,5),(69,2018,'i20',0,5),(70,2018,'h32',0,5),(71,2018,'h31',0,5),(72,2018,'e9',177936.47,5),(73,2018,'i13',0,5),(74,2018,'d29',0,5),(75,2018,'e24',21487.3,5),(76,2018,'h12',66.92,5),(77,2018,'h17',0,5),(78,2018,'e10',0,5),(79,2018,'d32',0,5),(80,2018,'i10',43995,5),(81,2018,'h20',0,5),(82,2018,'i25',0,5),(83,2018,'d19',0,5),(84,2018,'h14',0,5),(85,2018,'i33',0,5),(86,2018,'d36',0,5),(87,2018,'d35',0,5),(88,2018,'h16',0,5),(89,2018,'h13',0,5),(90,2018,'year',2018,5),(91,2018,'e33',0,5),(92,2018,'d21',0,5),(93,2018,'e29',0,5),(94,2018,'i22',0,5),(95,2018,'d30',0,5),(96,2018,'e32',0,5),(97,2018,'i6',0,5),(98,2018,'d24',1583.3,5),(99,2018,'h24',0,5),(100,2018,'e30',0,5),(101,2018,'e15',0,5),(102,2018,'i23',0,5),(103,2018,'d25',369.46,5),(104,2018,'i25',0,6),(105,2018,'i31',0,6),(106,2018,'e25',7462.36,6),(107,2018,'d23',0,6),(108,2018,'d33',0,6),(109,2018,'i7',0,6),(110,2018,'d30',0,6),(111,2018,'i8',0,6),(112,2018,'d32',0,6),(113,2018,'e14',0,6),(114,2018,'h23',0,6),(115,2018,'h11',77692,6),(116,2018,'d8',0,6),(117,2018,'i11',105259.88,6),(118,2018,'e24',21487.3,6),(119,2018,'h25',0,6),(120,2018,'d15',0,6),(121,2018,'i33',0,6),(122,2018,'d9',79578,6),(123,2018,'e23',0,6),(124,2018,'i6',0,6),(125,2018,'i32',0,6),(126,2018,'e35',0,6),(127,2018,'i9',32000,6),(128,2018,'e27',0,6),(129,2018,'i17',0,6),(130,2018,'h13',0,6),(131,2018,'e22',0,6),(132,2018,'e12',0,6),(133,2018,'h31',0,6),(134,2018,'e20',0,6),(135,2018,'d34',0,6),(136,2018,'e9',177936.47,6),(137,2018,'i22',0,6),(138,2018,'h30',1000000,6),(139,2018,'e29',0,6),(140,2018,'i23',0,6),(141,2018,'h6',0,6),(142,2018,'h14',0,6),(143,2018,'h12',66.92,6),(144,2018,'d29',0,6),(145,2018,'e19',0,6),(146,2018,'h7',0,6),(147,2018,'h33',0,6),(148,2018,'e34',0,6),(149,2018,'d24',1583.3,6),(150,2018,'i20',0,6),(151,2018,'h10',0,6),(152,2018,'e21',0,6),(153,2018,'e16',0,6),(154,2018,'h15',34319.88,6),(155,2018,'e32',0,6),(156,2018,'d36',0,6),(157,2018,'d6',5298.54,6),(158,2018,'h24',0,6),(159,2018,'e13',1016000,6),(160,2018,'i34',-33603.89,6),(161,2018,'h26',0,6),(162,2018,'h21',0,6),(163,2018,'h8',0,6),(164,2018,'d22',0,6),(165,2018,'h20',0,6),(166,2018,'d31',0,6),(167,2018,'e6',1238.49,6),(168,2018,'e11',0,6),(169,2018,'d19',0,6),(170,2018,'i26',0,6),(171,2018,'i12',0,6),(172,2018,'i14',0,6),(173,2018,'d12',0,6),(174,2018,'h32',0,6),(175,2018,'d13',992000,6),(176,2018,'e30',0,6),(177,2018,'h22',0,6),(178,2018,'d14',0,6),(179,2018,'d27',0,6),(180,2018,'d10',0,6),(181,2018,'d21',0,6),(182,2018,'year',2018,6),(183,2018,'e8',0,6),(184,2018,'e7',0,6),(185,2018,'e10',0,6),(186,2018,'e33',0,6),(187,2018,'d16',0,6),(188,2018,'h34',-39658.42,6),(189,2018,'i15',61548.91,6),(190,2018,'d25',369.46,6),(191,2018,'i24',0,6),(192,2018,'d20',0,6),(193,2018,'e31',0,6),(194,2018,'i16',0,6),(195,2018,'e36',0,6),(196,2018,'d11',0,6),(197,2018,'i10',43995,6),(198,2018,'i21',0,6),(199,2018,'h16',0,6),(200,2018,'h9',5670,6),(201,2018,'i30',1000000,6),(202,2018,'d35',0,6),(203,2018,'i13',0,6),(204,2018,'e15',0,6),(205,2018,'d7',0,6),(206,2018,'h17',0,6);
/*!40000 ALTER TABLE `company_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_cashflow`
--

DROP TABLE IF EXISTS `company_cashflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_cashflow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_cashflow_companyInfo_id_84f5fc8e_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_cashflow_companyInfo_id_84f5fc8e_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_cashflow`
--

LOCK TABLES `company_cashflow` WRITE;
/*!40000 ALTER TABLE `company_cashflow` DISABLE KEYS */;
INSERT INTO `company_cashflow` VALUES (1,2018,'g13',1,5),(2,2018,'g37',1,5),(3,2018,'d24',1,5),(4,2018,'g17',1,5),(5,2018,'d18',1,5),(6,2018,'d19',11,5),(7,2018,'g27',1,5),(8,2018,'d12',1,5),(9,2018,'d11',1,5),(10,2018,'g7',1,5),(11,2018,'d7',1,5),(12,2018,'year',2018,5),(13,2018,'d20',1,5),(14,2018,'d13',1,5),(15,2018,'g10',1,5),(16,2018,'g29',1,5),(17,2018,'d8',1,5),(18,2018,'g28',1,5),(19,2018,'g36',1,5),(20,2018,'g14',1,5),(21,2018,'g15',1,5),(22,2018,'g9',1,5),(23,2018,'d12',119.42,6),(24,2018,'d11',134281.64,6),(25,2018,'d8',24965.25,6),(26,2018,'d13',154565,6),(27,2018,'year',2018,6);
/*!40000 ALTER TABLE `company_cashflow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_companyinfo`
--

DROP TABLE IF EXISTS `company_companyinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
  `abouts` varchar(500) DEFAULT NULL,
  `field_1` smallint(6) DEFAULT NULL,
  `field_2` varchar(20) DEFAULT NULL,
  `x1` smallint(6) DEFAULT NULL,
  `technical_source` smallint(6) DEFAULT NULL,
  `SOAT` smallint(6) DEFAULT NULL,
  `credit_code` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `business_license_pic` varchar(100) DEFAULT NULL,
  `incubator_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `company_companyinfo_incubator_id_4ba91699_fk_incubator` (`incubator_id`),
  CONSTRAINT `company_companyinfo_incubator_id_4ba91699_fk_incubator` FOREIGN KEY (`incubator_id`) REFERENCES `incubator_incubator` (`id`),
  CONSTRAINT `company_companyinfo_user_id_e4d0d778_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_companyinfo`
--

LOCK TABLES `company_companyinfo` WRITE;
/*!40000 ALTER TABLE `company_companyinfo` DISABLE KEYS */;
INSERT INTO `company_companyinfo` VALUES (1,'c1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_qPo1Jdw.jpg',1,4),(2,'c2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_MT8ToIT.jpg',1,5),(3,'c3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_EhxMQxs.jpg',1,6),(4,'c4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_NSiPcHE.jpg',1,7),(5,'c5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_6Z1JjKd.jpg',1,8),(6,'111','2018-10-19',13132,12132,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'111',13945846584,'static/upload/company/banner-1.png',1,19),(7,'cc1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'123',123,'static/upload/company/1_M4zmV7A.jpg',1,20);
/*!40000 ALTER TABLE `company_companyinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_coremember`
--

DROP TABLE IF EXISTS `company_coremember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_educationexperience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `education` varchar(50) DEFAULT NULL,
  `university` varchar(50) DEFAULT NULL,
  `major` varchar(50) DEFAULT NULL,
  `core_member_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_educationexp_core_member_id_ae620ffa_fk_company_c` (`core_member_id`),
  CONSTRAINT `company_educationexp_core_member_id_ae620ffa_fk_company_c` FOREIGN KEY (`core_member_id`) REFERENCES `company_coremember` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_enterpriseawards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` varchar(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_enterpriseaw_companyInfo_id_5f1670fa_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_enterpriseaw_companyInfo_id_5f1670fa_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_enterpriseawards`
--

LOCK TABLES `company_enterpriseawards` WRITE;
/*!40000 ALTER TABLE `company_enterpriseawards` DISABLE KEYS */;
INSERT INTO `company_enterpriseawards` VALUES (1,'1','1','2018-10-18',5);
/*!40000 ALTER TABLE `company_enterpriseawards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_evaluationofenterprises`
--

DROP TABLE IF EXISTS `company_evaluationofenterprises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_evaluationofenterprises`
--

LOCK TABLES `company_evaluationofenterprises` WRITE;
/*!40000 ALTER TABLE `company_evaluationofenterprises` DISABLE KEYS */;
INSERT INTO `company_evaluationofenterprises` VALUES (1,5,3,8,9,'2018-10-17 05:59:31.706252',5),(2,6,5,8,10,'2018-10-19 04:13:26.758211',6),(3,NULL,NULL,NULL,NULL,'2018-10-19 05:55:09.889485',7);
/*!40000 ALTER TABLE `company_evaluationofenterprises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_financialsituation`
--

DROP TABLE IF EXISTS `company_financialsituation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_financialsituation`
--

LOCK TABLES `company_financialsituation` WRITE;
/*!40000 ALTER TABLE `company_financialsituation` DISABLE KEYS */;
INSERT INTO `company_financialsituation` VALUES (1,2018,222,22,222,222,5),(2,2017,22,22,22,22,5),(3,NULL,NULL,NULL,NULL,NULL,6),(4,NULL,NULL,NULL,NULL,NULL,7);
/*!40000 ALTER TABLE `company_financialsituation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_independentevaluationofenterprises`
--

DROP TABLE IF EXISTS `company_independentevaluationofenterprises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_independentevaluationofenterprises`
--

LOCK TABLES `company_independentevaluationofenterprises` WRITE;
/*!40000 ALTER TABLE `company_independentevaluationofenterprises` DISABLE KEYS */;
INSERT INTO `company_independentevaluationofenterprises` VALUES (1,2,4,4,6,'2018-10-17 05:58:33.122991',5),(2,7,6,10,10,'2018-10-19 04:10:13.766635',6),(3,1,1,1,1,'2018-10-19 05:46:24.170095',7);
/*!40000 ALTER TABLE `company_independentevaluationofenterprises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_mirc`
--

DROP TABLE IF EXISTS `company_mirc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_mirc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `num` varchar(50) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_mirc_companyInfo_id_b23cd250_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `company_mirc_companyInfo_id_b23cd250_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_mirc`
--

LOCK TABLES `company_mirc` WRITE;
/*!40000 ALTER TABLE `company_mirc` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_mirc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_patent`
--

DROP TABLE IF EXISTS `company_patent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_patent`
--

LOCK TABLES `company_patent` WRITE;
/*!40000 ALTER TABLE `company_patent` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_patent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_personalawards`
--

DROP TABLE IF EXISTS `company_personalawards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_personalawards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `level_title` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_personalawar_companyInfo_id_d63b1736_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_personalawar_companyInfo_id_d63b1736_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_personalawards`
--

LOCK TABLES `company_personalawards` WRITE;
/*!40000 ALTER TABLE `company_personalawards` DISABLE KEYS */;
INSERT INTO `company_personalawards` VALUES (1,'1','1','2018-10-18',5);
/*!40000 ALTER TABLE `company_personalawards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_productsandmarket`
--

DROP TABLE IF EXISTS `company_productsandmarket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_productsandmarket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product` varchar(500) DEFAULT NULL,
  `model` varchar(500) DEFAULT NULL,
  `analysis_forecast` varchar(500) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_productsandm_companyInfo_id_f940e9f4_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_productsandmarket`
--

LOCK TABLES `company_productsandmarket` WRITE;
/*!40000 ALTER TABLE `company_productsandmarket` DISABLE KEYS */;
INSERT INTO `company_productsandmarket` VALUES (1,NULL,NULL,NULL,5),(2,NULL,NULL,NULL,6),(3,NULL,NULL,NULL,7);
/*!40000 ALTER TABLE `company_productsandmarket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_profit`
--

DROP TABLE IF EXISTS `company_profit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_profit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` smallint(6) DEFAULT NULL,
  `name` varchar(4) NOT NULL,
  `value` double NOT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_profit_companyInfo_id_528daf88_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `company_profit_companyInfo_id_528daf88_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_profit`
--

LOCK TABLES `company_profit` WRITE;
/*!40000 ALTER TABLE `company_profit` DISABLE KEYS */;
INSERT INTO `company_profit` VALUES (1,2018,'c21',1111,5),(2,2018,'c22',15,5),(3,2018,'c26',18,5),(4,2018,'c8',2,5),(5,2018,'c27',19,5),(6,2018,'c17',9,5),(7,2018,'c15',7,5),(8,2018,'c11',3,5),(9,2018,'year',2018,5),(10,2018,'c19',12,5),(11,2018,'c24',16,5),(12,2018,'c20',13,5),(13,2018,'c14',6,5),(14,2018,'c7',1,5),(15,2018,'c18',11,5),(16,2018,'c29',20,5),(17,2018,'c12',4,5),(18,2018,'c13',5,5),(19,2018,'c25',17,5),(20,2018,'c16',8,5),(21,2018,'c7',284134.45,6),(22,2018,'c16',55092.9,6),(23,2018,'c15',287075.72,6),(24,2018,'c24',8994.04,6),(25,2018,'c17',-1.76,6),(26,2018,'c18',12.76,6),(27,2018,'year',2018,6);
/*!40000 ALTER TABLE `company_profit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_project`
--

DROP TABLE IF EXISTS `company_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `_type` varchar(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `finished_date_and_conclusion` varchar(50) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_project_companyInfo_id_235f7a33_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_project_companyInfo_id_235f7a33_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_project`
--

LOCK TABLES `company_project` WRITE;
/*!40000 ALTER TABLE `company_project` DISABLE KEYS */;
INSERT INTO `company_project` VALUES (1,'1','1','2018-10-18','1',5);
/*!40000 ALTER TABLE `company_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_serverrequest`
--

DROP TABLE IF EXISTS `company_serverrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_serverrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `duration` smallint(6) DEFAULT NULL,
  `ratio` double DEFAULT NULL,
  `interest_rate` double DEFAULT NULL,
  `plan` varchar(500) DEFAULT NULL,
  `small_loan` smallint(6) DEFAULT NULL,
  `share_model` smallint(6) DEFAULT NULL,
  `request` varchar(20) DEFAULT NULL,
  `companyInfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_serverreques_companyInfo_id_bbcdc638_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_serverrequest`
--

LOCK TABLES `company_serverrequest` WRITE;
/*!40000 ALTER TABLE `company_serverrequest` DISABLE KEYS */;
INSERT INTO `company_serverrequest` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,5),(2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,6),(3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,7);
/*!40000 ALTER TABLE `company_serverrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_shareholder`
--

DROP TABLE IF EXISTS `company_shareholder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_shareholder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `share_ratio` double DEFAULT NULL,
  `form_of_contribution` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `company_shareholder_companyInfo_id_29b72b99_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `company_shareholder_companyInfo_id_29b72b99_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_shareholder`
--

LOCK TABLES `company_shareholder` WRITE;
/*!40000 ALTER TABLE `company_shareholder` DISABLE KEYS */;
INSERT INTO `company_shareholder` VALUES (1,'1',2,3,5);
/*!40000 ALTER TABLE `company_shareholder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_standardsetting`
--

DROP TABLE IF EXISTS `company_standardsetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `company_technologyrd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(500) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `companyInfo_id` (`companyInfo_id`),
  CONSTRAINT `company_technologyrd_companyInfo_id_18ee93e7_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_technologyrd`
--

LOCK TABLES `company_technologyrd` WRITE;
/*!40000 ALTER TABLE `company_technologyrd` DISABLE KEYS */;
INSERT INTO `company_technologyrd` VALUES (1,NULL,5),(2,NULL,6),(3,NULL,7);
/*!40000 ALTER TABLE `company_technologyrd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_workexperience`
--

DROP TABLE IF EXISTS `company_workexperience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-10-17 03:57:39.285183','1','企业用户',1,'[{\"added\": {}}]',3,1),(2,'2018-10-17 03:58:21.360653','2','孵化器用户',1,'[{\"added\": {}}]',3,1),(3,'2018-10-17 03:58:51.410273','3','机构用户',1,'[{\"added\": {}}]',3,1),(4,'2018-10-17 05:57:56.783446','5','c5',2,'[{\"added\": {\"object\": \"FinancialSituation object\", \"name\": \"\\u4e8c\\u3001\\u8d22\\u52a1\\u72b6\\u51b5\"}}, {\"changed\": {\"fields\": [\"year\", \"income\", \"profit\", \"total\", \"r_d_cost\"], \"object\": \"FinancialSituation object\", \"name\": \"\\u4e8c\\u3001\\u8d22\\u52a1\\u72b6\\u51b5\"}}]',23,8),(5,'2018-10-17 05:58:33.136995','1','自主评价',1,'[{\"added\": {}}]',17,8),(6,'2018-10-17 05:59:31.719258','1','校正评价',2,'[{\"changed\": {\"fields\": [\"external_environment\", \"products_and_market\", \"technology_R_D\", \"team\"]}}]',19,3),(7,'2018-10-18 02:04:08.680575','10','2018-10-17 14:54:26',3,'',33,1),(8,'2018-10-18 02:33:27.607459','2','2018-10-18 10:33:27',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',33,1),(9,'2018-10-18 02:39:41.414760','2','2018-10-18 10:39:41',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',33,1),(10,'2018-10-18 03:31:18.619825','1','2018-10-18 11:31:18',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(11,'2018-10-18 06:26:29.497750','3','机构用户',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(12,'2018-10-18 06:27:09.851243','3','机构用户',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(13,'2018-10-18 06:29:50.448230','5','c5',2,'[{\"added\": {\"object\": \"Shareholder object\", \"name\": \"\\u4e3b\\u8981\\u80a1\\u4e1c\\u53ca\\u80a1\\u6743\\u6bd4\\u4f8b\\uff08\\u524d\\u4e94\\u540d\\uff09\"}}, {\"added\": {\"object\": \"EnterpriseAwards object\", \"name\": \"\\u4f01\\u4e1a\\u83b7\\u5956\\u60c5\\u51b5\"}}, {\"added\": {\"object\": \"PersonalAwards object\", \"name\": \"\\u6838\\u5fc3\\u56e2\\u961f\\u4e2a\\u4eba\\u83b7\\u5956\\u60c5\\u51b5\"}}, {\"added\": {\"object\": \"Project object\", \"name\": \"\\u4f01\\u4e1a\\u66fe\\u7ecf\\u627f\\u62c5\\u6216\\u6b63\\u5728\\u627f\\u62c5\\u7684\\u79d1\\u6280\\u8ba1\\u5212\\u9879\\u76ee\"}}]',23,8),(14,'2018-10-18 07:41:26.248222','3','jgg4',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',31,1),(15,'2018-10-18 09:40:50.823684','3','机构用户',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(16,'2018-10-18 09:41:35.929118','2','孵化器用户',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(17,'2018-10-18 09:41:46.329985','1','企业用户',2,'[{\"changed\": {\"fields\": [\"permissions\"]}}]',3,1),(18,'2018-10-19 01:25:12.836107','2','ReportBack object',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,17),(19,'2018-10-19 01:30:26.391165','3','c5 2018-10-18 11:31:18 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,17),(20,'2018-10-19 01:42:16.920233','3','c5 2018-10-18 11:31:18 反馈信息',2,'[{\"changed\": {\"fields\": [\"iscompanyview\"]}}]',34,1),(21,'2018-10-19 01:45:10.636055','3','c5 2018-10-18 11:31:18 反馈信息',2,'[{\"changed\": {\"fields\": [\"isinstitutionview\"]}}]',34,1),(22,'2018-10-19 02:59:42.814826','4','2018-10-19 10:59:42',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(23,'2018-10-19 03:04:16.615383','5','2018-10-19 11:04:16',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(24,'2018-10-19 03:04:39.262098','13','2018-10-19 11:04:39',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',33,1),(25,'2018-10-19 03:05:07.498743','6','2018-10-19 11:05:07',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(26,'2018-10-19 03:05:32.164436','6','2018-10-19 11:05:32',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(27,'2018-10-19 03:38:15.663751','7','2018-10-19 11:38:15',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(28,'2018-10-19 03:39:03.294157','4','c5 2018-10-19 11:38:15 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,18),(29,'2018-10-19 04:05:35.767133','1','c1',1,'[{\"added\": {}}]',7,1),(30,'2018-10-19 04:05:52.197925','1','c2',1,'[{\"added\": {}}]',8,1),(31,'2018-10-19 04:10:13.792638','2','自主评价',1,'[{\"added\": {}}]',17,19),(32,'2018-10-19 04:11:38.558576','6','111',2,'[{\"changed\": {\"fields\": [\"create_date\", \"registered_capital\", \"paid_in_capital\"]}}]',23,19),(33,'2018-10-19 04:13:26.772209','2','校正评价',2,'[{\"changed\": {\"fields\": [\"external_environment\", \"products_and_market\", \"technology_R_D\", \"team\"]}}]',19,3),(34,'2018-10-19 04:14:08.640683','10','2018-10-19 12:14:08',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',32,1),(35,'2018-10-19 04:15:40.484530','5','111 2018-10-19 12:14:08 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,18),(36,'2018-10-19 04:16:21.476019','6','111 2018-10-19 12:14:08 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,18),(37,'2018-10-19 04:16:42.880743','6','111 2018-10-19 12:14:08 反馈信息',2,'[{\"changed\": {\"fields\": [\"isinstitutionview\"]}}]',34,1),(38,'2018-10-19 05:42:58.370686','7','cc1',2,'[]',23,20),(39,'2018-10-19 05:43:06.595577','7','cc1',2,'[]',23,20),(40,'2018-10-19 05:46:24.183093','3','自主评价',1,'[{\"added\": {}}]',17,20),(41,'2018-10-19 05:57:49.702481','7','c5 2018-10-19 11:38:15 反馈信息',2,'[{\"changed\": {\"fields\": [\"institution\"]}}]',34,18);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(13,'company','balance'),(27,'company','cashflow'),(23,'company','companyinfo'),(28,'company','coremember'),(25,'company','drugapproval'),(18,'company','educationexperience'),(9,'company','enterpriseawards'),(19,'company','evaluationofenterprises'),(12,'company','financialsituation'),(17,'company','independentevaluationofenterprises'),(22,'company','mirc'),(21,'company','patent'),(24,'company','personalawards'),(26,'company','productsandmarket'),(14,'company','profit'),(11,'company','project'),(29,'company','serverrequest'),(10,'company','shareholder'),(16,'company','standardsetting'),(15,'company','technologyrd'),(20,'company','workexperience'),(5,'contenttypes','contenttype'),(30,'incubator','incubator'),(7,'index','bonus'),(8,'index','subtraction'),(33,'institution','bankreport'),(31,'institution','institution'),(32,'institution','investreport'),(34,'institution','reportback'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-17 03:26:54.533842'),(2,'auth','0001_initial','2018-10-17 03:27:13.317603'),(3,'admin','0001_initial','2018-10-17 03:27:16.382574'),(4,'admin','0002_logentry_remove_auto_add','2018-10-17 03:27:16.491570'),(5,'contenttypes','0002_remove_content_type_name','2018-10-17 03:27:18.814536'),(6,'auth','0002_alter_permission_name_max_length','2018-10-17 03:27:20.363516'),(7,'auth','0003_alter_user_email_max_length','2018-10-17 03:27:20.749509'),(8,'auth','0004_alter_user_username_opts','2018-10-17 03:27:20.827510'),(9,'auth','0005_alter_user_last_login_null','2018-10-17 03:27:22.341489'),(10,'auth','0006_require_contenttypes_0002','2018-10-17 03:27:22.399489'),(11,'auth','0007_alter_validators_add_error_messages','2018-10-17 03:27:22.518495'),(12,'auth','0008_alter_user_username_max_length','2018-10-17 03:27:26.501438'),(13,'incubator','0001_initial','2018-10-17 03:27:31.791371'),(14,'company','0001_initial','2018-10-17 03:28:25.725692'),(15,'index','0001_initial','2018-10-17 03:28:29.302649'),(16,'sessions','0001_initial','2018-10-17 03:28:29.996637'),(17,'institution','0001_initial','2018-10-17 03:29:00.767259'),(18,'company','0002_auto_20181017_1311','2018-10-17 05:11:55.774158'),(19,'institution','0002_institutions','2018-10-17 05:11:57.954127'),(20,'institution','0003_auto_20181017_1135','2018-10-17 05:12:02.222073'),(21,'institution','0004_auto_20181017_1417','2018-10-17 06:17:33.478651'),(22,'institution','0005_auto_20181017_1421','2018-10-17 06:22:21.196036'),(23,'institution','0006_investreport_institution','2018-10-18 02:16:27.729291'),(24,'institution','0007_auto_20181018_1027','2018-10-18 02:27:43.096790'),(25,'institution','0008_reportback','2018-10-18 09:28:16.048171'),(26,'institution','0009_auto_20181019_0924','2018-10-19 01:24:31.765621');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('049662lf56mwt8hu7rnew6jkvrpqxqwc','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-11-01 02:22:41.100588'),('3e5utv0zqr1yit9hqd7cv5o8hc4lgd0i','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-10-31 04:03:00.564142'),('44rervxghmbvan6m5jzcugyh8yv8dbxi','MzNhY2M2NTE0MDZmOGI3MTVhYjkwN2JkMzEzNzhhYTE5MTQ4MDgyZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjM2NjZjNGRhZGY4ZGUzOWRmOTc3MDczNmE4MzhlMzI2MjNmMzk2MmUiLCJfYXV0aF91c2VyX2lkIjoiMTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2018-11-01 02:33:02.663772'),('8lfjp7e8ibl5o52e419dtlb4r9hgtngc','ZjUyMzA1NzdjOGIwNDQwMDJiMGM0ZGU5ZmFlYWJhZmI0YTU0MjI3MDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWI3YmVhYmI4M2Q1OTMxZGIzNjIxZTMxZjU0MjUwYTRmNGZmZjc3ZiIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2018-10-31 05:12:18.650871'),('ctjjyzm6bllgpovw5ynauruie439w5h3','YWVlMGFmNGZiZmZkNzBiNzI0MzI3ODM2MDE2YWJkY2ZmMmFlZTA0NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhlNzE1ZWQ4ZjUyYjZiYzhjMjM1MDhjNzM3MThhNWU4ZTljZmUyZmYiLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-11-02 01:43:05.342624'),('d8t9cu63ez4drtzuc6vwijq9jshzpw7j','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-10-31 04:02:13.384734'),('dyghqx9ao217vveksuq7nvjlfxxvq2fa','M2NlNjg4OGFlOTUxYWFiOTVhYzJiYmFkZTVkZDMyOWI5OGQ4Mjk4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjIyMTA3Mjg1MDc3Mjk4MDA0MmM2MGZmNjRmMjJiZDVjZDI5OTUyMjciLCJfYXV0aF91c2VyX2lkIjoiMTgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2018-11-02 05:57:03.427056'),('h1zwpyb52qvjk3pm9yo3pf80s6pc4rrm','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-10-31 04:00:20.036160'),('jpwibcang8aj37tbtsjv5jbitf39lj45','YWVlMGFmNGZiZmZkNzBiNzI0MzI3ODM2MDE2YWJkY2ZmMmFlZTA0NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjhlNzE1ZWQ4ZjUyYjZiYzhjMjM1MDhjNzM3MThhNWU4ZTljZmUyZmYiLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-10-31 03:59:17.631946'),('o40hookmhiptpkh42vo83hphvqtgoip1','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-11-01 02:20:46.579028'),('rr79ayczxpid8ui3t9jkz58ybbpuheea','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-10-31 03:56:38.267948'),('xkx4g2jq4hd0eqb3q4n602183j96yxl5','MTc4NDdjMzFjZmExZjI2YjVkODg1ZTk4ZDFiMzZkYjQzMWE5ZjI3ODp7fQ==','2018-10-31 04:05:21.150374'),('ye7yuuohx1jzz84k306moyyveydhfpuh','YThkM2NjM2ViZTIyOWQwODVkMjJhMDQ1OTM4ZTI2YjI2ODgwN2RmMjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiOGU3MTVlZDhmNTJiNmJjOGMyMzUwOGM3MzcxOGE1ZThlOWNmZTJmZiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-11-02 04:17:20.057280');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incubator_incubator`
--

DROP TABLE IF EXISTS `incubator_incubator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `incubator_incubator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `credit_code` varchar(50) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `incubator_incubator_user_id_bf7d94d1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incubator_incubator`
--

LOCK TABLES `incubator_incubator` WRITE;
/*!40000 ALTER TABLE `incubator_incubator` DISABLE KEYS */;
INSERT INTO `incubator_incubator` VALUES (1,'fhqz',123,NULL,3),(2,'123',123,NULL,11),(3,'123',123,NULL,12),(4,'123',123,NULL,13),(5,'fhqz1',123,NULL,21);
/*!40000 ALTER TABLE `incubator_incubator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_bonus`
--

DROP TABLE IF EXISTS `index_bonus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `index_bonus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item` smallint(6) NOT NULL,
  `note` longtext NOT NULL,
  `value` smallint(6) NOT NULL,
  `companyInfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_bonus_companyInfo_id_06a1f375_fk_company_companyinfo_id` (`companyInfo_id`),
  CONSTRAINT `index_bonus_companyInfo_id_06a1f375_fk_company_companyinfo_id` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_bonus`
--

LOCK TABLES `index_bonus` WRITE;
/*!40000 ALTER TABLE `index_bonus` DISABLE KEYS */;
INSERT INTO `index_bonus` VALUES (1,1,'111',111,1);
/*!40000 ALTER TABLE `index_bonus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_subtraction`
--

DROP TABLE IF EXISTS `index_subtraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `index_subtraction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item` smallint(6) DEFAULT NULL,
  `note` longtext,
  `value` smallint(6) DEFAULT NULL,
  `companyInfo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_subtraction_companyInfo_id_23ff605a_fk_company_c` (`companyInfo_id`),
  CONSTRAINT `index_subtraction_companyInfo_id_23ff605a_fk_company_c` FOREIGN KEY (`companyInfo_id`) REFERENCES `company_companyinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_subtraction`
--

LOCK TABLES `index_subtraction` WRITE;
/*!40000 ALTER TABLE `index_subtraction` DISABLE KEYS */;
INSERT INTO `index_subtraction` VALUES (1,2,'111',1,2);
/*!40000 ALTER TABLE `index_subtraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_bankreport`
--

DROP TABLE IF EXISTS `institution_bankreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_bankreport`
--

LOCK TABLES `institution_bankreport` WRITE;
/*!40000 ALTER TABLE `institution_bankreport` DISABLE KEYS */;
INSERT INTO `institution_bankreport` VALUES (1,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:22:31.727903',5,1,0,0,0,1),(2,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-18 02:39:41.394763',5,1,0,0,0,1),(3,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:28:17.404557',5,1,0,0,0,1),(4,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:30:18.201039',5,1,0,0,0,1),(5,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:52:52.648010',5,1,0,0,0,1),(6,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:53:11.986769',5,1,0,0,0,1),(7,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:53:23.136628',5,1,0,0,0,1),(8,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:53:34.464485',5,1,0,0,0,1),(9,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:53:38.689439',5,1,0,0,0,1),(11,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:54:44.108610',5,1,0,0,0,1),(12,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-17 06:55:26.409084',5,1,0,0,0,1),(13,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-19 03:04:39.220100',5,0,0,1,0,1),(14,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-19 03:54:18.470646',5,0,0,1,0,1),(15,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-19 03:54:42.686341',5,0,0,1,0,1),(16,5,3,8,9,0,0,0,0,0,1,0,0,0,'2018-10-19 06:06:12.785157',5,0,0,1,0,1);
/*!40000 ALTER TABLE `institution_bankreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_bankreport_institution`
--

DROP TABLE IF EXISTS `institution_bankreport_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `institution_bankreport_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bankreport_id` int(11) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `institution_bankreport_i_bankreport_id_institutio_57c0f417_uniq` (`bankreport_id`,`institution_id`),
  KEY `institution_bankrepo_institution_id_f6ae4cd0_fk_instituti` (`institution_id`),
  CONSTRAINT `institution_bankrepo_bankreport_id_b4c1209b_fk_instituti` FOREIGN KEY (`bankreport_id`) REFERENCES `institution_bankreport` (`id`),
  CONSTRAINT `institution_bankrepo_institution_id_f6ae4cd0_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_bankreport_institution`
--

LOCK TABLES `institution_bankreport_institution` WRITE;
/*!40000 ALTER TABLE `institution_bankreport_institution` DISABLE KEYS */;
INSERT INTO `institution_bankreport_institution` VALUES (3,2,3),(4,13,3);
/*!40000 ALTER TABLE `institution_bankreport_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_institution`
--

DROP TABLE IF EXISTS `institution_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `institution_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `institution_institution_user_id_114f795c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_institution`
--

LOCK TABLES `institution_institution` WRITE;
/*!40000 ALTER TABLE `institution_institution` DISABLE KEYS */;
INSERT INTO `institution_institution` VALUES (1,2,'123',123,15),(2,1,'123',123,16),(3,2,'jgg4',123,17),(4,1,'jgtz1',123,18);
/*!40000 ALTER TABLE `institution_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_investreport`
--

DROP TABLE IF EXISTS `institution_investreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_investreport`
--

LOCK TABLES `institution_investreport` WRITE;
/*!40000 ALTER TABLE `institution_investreport` DISABLE KEYS */;
INSERT INTO `institution_investreport` VALUES (1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,'2018-10-18 03:31:18.577826',5,5,3,8,9),(2,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-18 01:42:30.474894',5,5,3,8,9),(3,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 02:56:57.876899',5,5,3,8,9),(4,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 02:59:42.764827',5,5,3,8,9),(5,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 03:04:16.588387',5,5,3,8,9),(6,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 03:05:32.125437',5,5,3,8,9),(7,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 03:38:15.627756',5,5,3,8,9),(8,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 03:44:34.330988',5,5,3,8,9),(9,0,0,0,0,0,1,0,0,0,0,0,1,0,1,'2018-10-19 03:54:27.537537',5,5,3,8,9),(10,0,0,0,0,0,0,0,0,1,0,0,1,0,0,'2018-10-19 04:14:08.596686',6,6,5,8,10);
/*!40000 ALTER TABLE `institution_investreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_investreport_institution`
--

DROP TABLE IF EXISTS `institution_investreport_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `institution_investreport_institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `investreport_id` int(11) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `institution_investreport_investreport_id_institut_f9221963_uniq` (`investreport_id`,`institution_id`),
  KEY `institution_investre_institution_id_c006bdac_fk_instituti` (`institution_id`),
  CONSTRAINT `institution_investre_institution_id_c006bdac_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`),
  CONSTRAINT `institution_investre_investreport_id_0dfd221b_fk_instituti` FOREIGN KEY (`investreport_id`) REFERENCES `institution_investreport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_investreport_institution`
--

LOCK TABLES `institution_investreport_institution` WRITE;
/*!40000 ALTER TABLE `institution_investreport_institution` DISABLE KEYS */;
INSERT INTO `institution_investreport_institution` VALUES (1,1,1),(2,1,2),(3,1,3),(4,4,3),(5,5,3),(7,6,1),(8,7,4),(9,10,4);
/*!40000 ALTER TABLE `institution_investreport_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution_reportback`
--

DROP TABLE IF EXISTS `institution_reportback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `institution_reportback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `will` smallint(6) DEFAULT NULL,
  `type` smallint(6) DEFAULT NULL,
  `note` longtext,
  `iscompanyview` smallint(6) NOT NULL,
  `isinstitutionview` smallint(6) NOT NULL,
  `bankreport_id` int(11) DEFAULT NULL,
  `investreport_id` int(11) DEFAULT NULL,
  `institution_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `institution_reportback_bankreport_id_170c33df` (`bankreport_id`),
  KEY `institution_reportback_investreport_id_03a548cf` (`investreport_id`),
  KEY `institution_reportba_institution_id_aebc6cf1_fk_instituti` (`institution_id`),
  CONSTRAINT `institution_reportba_bankreport_id_170c33df_fk_instituti` FOREIGN KEY (`bankreport_id`) REFERENCES `institution_bankreport` (`id`),
  CONSTRAINT `institution_reportba_institution_id_aebc6cf1_fk_instituti` FOREIGN KEY (`institution_id`) REFERENCES `institution_institution` (`id`),
  CONSTRAINT `institution_reportba_investreport_id_03a548cf_fk_instituti` FOREIGN KEY (`investreport_id`) REFERENCES `institution_investreport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution_reportback`
--

LOCK TABLES `institution_reportback` WRITE;
/*!40000 ALTER TABLE `institution_reportback` DISABLE KEYS */;
INSERT INTO `institution_reportback` VALUES (1,1,2,'而德国',1,1,NULL,1,3),(2,1,2,'而德国',1,1,NULL,1,3),(3,1,2,'12344',2,2,NULL,1,3),(4,1,2,'fffff',1,1,NULL,7,4),(5,1,1,'111',1,1,NULL,10,4),(6,1,1,'111',1,2,NULL,10,4),(7,1,2,'123',1,1,NULL,7,4);
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

-- Dump completed on 2018-10-20 10:18:22
