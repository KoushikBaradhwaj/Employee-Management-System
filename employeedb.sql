-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: employee
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `attendance_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `date` date NOT NULL,
  `clock_in` time DEFAULT NULL,
  `clock_out` time DEFAULT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,1,'2023-03-06','09:00:00','17:00:00'),(2,2,'2023-03-06','09:15:00','17:30:00'),(3,3,'2023-03-06','08:45:00','16:45:00'),(4,4,'2023-03-06','10:00:00','18:00:00'),(5,5,'2023-03-06','09:30:00','17:45:00');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `benefits`
--

DROP TABLE IF EXISTS `benefits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `benefits` (
  `benefit_id` int NOT NULL,
  `benefit_name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`benefit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `benefits`
--

LOCK TABLES `benefits` WRITE;
/*!40000 ALTER TABLE `benefits` DISABLE KEYS */;
INSERT INTO `benefits` VALUES (1,'Health Insurance','Comprehensive health coverage.'),(2,'Dental Insurance','Dental care coverage.'),(3,'Vision Insurance','Vision care coverage.'),(4,'Paid Time Off','Paid vacation and sick leave.'),(5,'Retirement Plan','401k retirement savings plan.');
/*!40000 ALTER TABLE `benefits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `dept_id` int NOT NULL,
  `dept_name` varchar(255) NOT NULL,
  `dept_location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Technology','Building A'),(2,'Marketing','Building B'),(3,'Finance','Building C'),(4,'Human Resources','Building D'),(5,'Sales','Building E');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergency_contact`
--

DROP TABLE IF EXISTS `emergency_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emergency_contact` (
  `contact_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `contact_name` varchar(255) NOT NULL,
  `relationship_type` varchar(50) DEFAULT NULL,
  `relationship` varchar(255) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  PRIMARY KEY (`contact_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `emergency_contact_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergency_contact`
--

LOCK TABLES `emergency_contact` WRITE;
/*!40000 ALTER TABLE `emergency_contact` DISABLE KEYS */;
INSERT INTO `emergency_contact` VALUES (1,1,'Mary Doe',NULL,'Spouse','1111111111'),(2,2,'Robert Smith',NULL,'Father','2222222222'),(3,3,'Susan Jones',NULL,'Mother','3333333333'),(4,4,'William Brown',NULL,'Brother','4444444444'),(5,5,'Elizabeth Lee',NULL,'Sister','5555555555');
/*!40000 ALTER TABLE `emergency_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_benefits`
--

DROP TABLE IF EXISTS `emp_benefits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_benefits` (
  `emp_id` int NOT NULL,
  `benefit_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`benefit_id`),
  KEY `benefit_id` (`benefit_id`),
  CONSTRAINT `emp_benefits_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`),
  CONSTRAINT `emp_benefits_ibfk_2` FOREIGN KEY (`benefit_id`) REFERENCES `benefits` (`benefit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_benefits`
--

LOCK TABLES `emp_benefits` WRITE;
/*!40000 ALTER TABLE `emp_benefits` DISABLE KEYS */;
INSERT INTO `emp_benefits` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `emp_benefits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_department`
--

DROP TABLE IF EXISTS `emp_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_department` (
  `emp_id` int NOT NULL,
  `dept_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`dept_id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `emp_department_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`),
  CONSTRAINT `emp_department_ibfk_2` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_department`
--

LOCK TABLES `emp_department` WRITE;
/*!40000 ALTER TABLE `emp_department` DISABLE KEYS */;
INSERT INTO `emp_department` VALUES (1,1),(2,1),(3,2),(4,3),(5,4);
/*!40000 ALTER TABLE `emp_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_project`
--

DROP TABLE IF EXISTS `emp_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_project` (
  `emp_id` int NOT NULL,
  `project_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`project_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `emp_project_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`),
  CONSTRAINT `emp_project_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_project`
--

LOCK TABLES `emp_project` WRITE;
/*!40000 ALTER TABLE `emp_project` DISABLE KEYS */;
INSERT INTO `emp_project` VALUES (1,1),(2,1),(3,2),(4,3),(5,4),(1,101);
/*!40000 ALTER TABLE `emp_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_skills`
--

DROP TABLE IF EXISTS `emp_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_skills` (
  `emp_id` int NOT NULL,
  `skill_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`skill_id`),
  KEY `skill_id` (`skill_id`),
  CONSTRAINT `emp_skills_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`),
  CONSTRAINT `emp_skills_ibfk_2` FOREIGN KEY (`skill_id`) REFERENCES `skills` (`skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_skills`
--

LOCK TABLES `emp_skills` WRITE;
/*!40000 ALTER TABLE `emp_skills` DISABLE KEYS */;
INSERT INTO `emp_skills` VALUES (1,1),(1,2),(2,3),(3,4),(4,5),(1,301);
/*!40000 ALTER TABLE `emp_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_training`
--

DROP TABLE IF EXISTS `emp_training`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_training` (
  `emp_id` int NOT NULL,
  `training_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`training_id`),
  KEY `training_id` (`training_id`),
  CONSTRAINT `emp_training_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`),
  CONSTRAINT `emp_training_ibfk_2` FOREIGN KEY (`training_id`) REFERENCES `training` (`training_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_training`
--

LOCK TABLES `emp_training` WRITE;
/*!40000 ALTER TABLE `emp_training` DISABLE KEYS */;
INSERT INTO `emp_training` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(1,501);
/*!40000 ALTER TABLE `emp_training` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empdata`
--

DROP TABLE IF EXISTS `empdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empdata` (
  `Id` int NOT NULL,
  `Name` varchar(1000) DEFAULT NULL,
  `Emial_Id` varchar(255) DEFAULT NULL,
  `Phone_no` bigint DEFAULT NULL,
  `Address` text,
  `post_id` int DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Emial_Id` (`Emial_Id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `empdata_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `job_role` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empdata`
--

LOCK TABLES `empdata` WRITE;
/*!40000 ALTER TABLE `empdata` DISABLE KEYS */;
INSERT INTO `empdata` VALUES (1,'John Doe','john.doe@example.com',1234567890,'123 Main St, Anytown',NULL),(2,'Jane Smith','jane.smith@example.com',9876543210,'456 Oak Ave, Anytown',NULL),(3,'Peter Jones','peter.jones@example.com',5551234567,'789 Pine St, Anytown',NULL),(4,'Sarah Brown','sarah.brown@example.com',1112223333,'101 Elm St, Anytown',NULL),(5,'David Lee','david.lee@example.com',9998887777,'202 Maple Ave, Anytown',NULL),(6,'SAFA','asdfgh@gmail.com',78996541,'Hyderabad, India',NULL);
/*!40000 ALTER TABLE `empdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_role`
--

DROP TABLE IF EXISTS `job_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_role` (
  `post_id` int NOT NULL AUTO_INCREMENT,
  `post_name` varchar(255) NOT NULL,
  `base_salary` bigint DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_role`
--

LOCK TABLES `job_role` WRITE;
/*!40000 ALTER TABLE `job_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leave_`
--

DROP TABLE IF EXISTS `leave_`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leave_` (
  `leave_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `leave_type` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  PRIMARY KEY (`leave_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `leave__ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leave_`
--

LOCK TABLES `leave_` WRITE;
/*!40000 ALTER TABLE `leave_` DISABLE KEYS */;
INSERT INTO `leave_` VALUES (1,1,'Vacation','2023-05-01','2023-05-05'),(2,2,'Sick Leave','2023-06-10','2023-06-12'),(3,3,'Personal Leave','2023-07-15','2023-07-17'),(4,4,'Maternity Leave','2023-08-01','2023-10-31'),(5,5,'Paternity Leave','2023-09-15','2023-09-29');
/*!40000 ALTER TABLE `leave_` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `performance_review`
--

DROP TABLE IF EXISTS `performance_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance_review` (
  `review_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `review_date` date NOT NULL,
  `comments` text,
  PRIMARY KEY (`review_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `performance_review_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `performance_review`
--

LOCK TABLES `performance_review` WRITE;
/*!40000 ALTER TABLE `performance_review` DISABLE KEYS */;
INSERT INTO `performance_review` VALUES (1,1,'2023-03-01','Excellent performance!'),(2,2,'2023-03-01','Good work, needs improvement in communication.'),(3,3,'2023-03-01','Meets expectations.'),(4,4,'2023-03-01','Exceeded expectations in creativity.'),(5,5,'2023-03-01','Needs to improve time management skills.');
/*!40000 ALTER TABLE `performance_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `project_id` int NOT NULL,
  `project_name` varchar(255) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Project Alpha','2023-01-01','2023-06-30'),(2,'Project Beta','2023-02-15','2023-08-15'),(3,'Project Gamma','2023-03-01','2023-09-30'),(4,'Project Delta','2023-04-15','2023-10-15'),(5,'Project Epsilon','2023-05-01','2023-11-30'),(101,'Employee Portal','2024-01-01','2024-12-31');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `salary_id` int NOT NULL,
  `emp_id` int DEFAULT NULL,
  `salary_amount` decimal(10,2) NOT NULL,
  `payment_date` date NOT NULL,
  PRIMARY KEY (`salary_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (1,1,5000.00,'2023-02-28'),(2,2,6000.00,'2023-02-28'),(3,3,7000.00,'2023-02-28'),(4,4,5500.00,'2023-02-28'),(5,5,6500.00,'2023-02-28'),(6,1,50000.00,'2023-10-05');
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary_history`
--

DROP TABLE IF EXISTS `salary_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_history` (
  `history_id` int NOT NULL AUTO_INCREMENT,
  `emp_id` int DEFAULT NULL,
  `old_salary` decimal(10,2) DEFAULT NULL,
  `new_salary` decimal(10,2) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `update_year` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `salary_history_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdata` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary_history`
--

LOCK TABLES `salary_history` WRITE;
/*!40000 ALTER TABLE `salary_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `salary_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `salaryview`
--

DROP TABLE IF EXISTS `salaryview`;
/*!50001 DROP VIEW IF EXISTS `salaryview`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `salaryview` AS SELECT 
 1 AS `salary_id`,
 1 AS `emp_id`,
 1 AS `salary_amount`,
 1 AS `payment_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `skill_id` int NOT NULL,
  `skill_name` varchar(255) NOT NULL,
  PRIMARY KEY (`skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'Java'),(2,'Python'),(3,'SQL'),(4,'Communication'),(5,'Leadership'),(301,'Cybersecurity');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training`
--

DROP TABLE IF EXISTS `training`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training` (
  `training_id` int NOT NULL,
  `training_name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`training_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training`
--

LOCK TABLES `training` WRITE;
/*!40000 ALTER TABLE `training` DISABLE KEYS */;
INSERT INTO `training` VALUES (1,'Leadership Skills','Develop leadership qualities.'),(2,'Time Management','Improve time management skills.'),(3,'Communication Skills','Enhance communication skills.'),(4,'Technical Skills','Upgrade technical skills.'),(5,'Problem Solving','Improve problem-solving abilities.'),(501,'Network Security Training','Training on securing network infrastructure');
/*!40000 ALTER TABLE `training` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `salaryview`
--

/*!50001 DROP VIEW IF EXISTS `salaryview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `salaryview` AS select `salary`.`salary_id` AS `salary_id`,`salary`.`emp_id` AS `emp_id`,`salary`.`salary_amount` AS `salary_amount`,`salary`.`payment_date` AS `payment_date` from `salary` */;
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

-- Dump completed on 2025-05-31 14:08:08
