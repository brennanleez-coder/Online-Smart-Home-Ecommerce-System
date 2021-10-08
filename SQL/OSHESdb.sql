CREATE DATABASE IF NOT EXISTS OSHES;
use OSHES;

CREATE TABLE `OSHES`.`Customer` (
	`customerID` VARCHAR(100) NOT NULL,

	`fName` VARCHAR(255) NOT NULL,
	`lName` VARCHAR(255) NOT NULL,

	`gender` VARCHAR(10) NOT NULL,
	`emailAddress` VARCHAR(255) NOT NULL,
	`address` VARCHAR(255) NOT NULL,
	`phoneNumber` VARCHAR(50) NOT NULL,
	`password` VARCHAR(255) NOT NULL);
	
	CREATE TABLE `OSHES`.`Administrator` (
	`administratorID` VARCHAR(100) NOT NULL,

	`fName` VARCHAR(255) NOT NULL,
	`lName` VARCHAR(255) NOT NULL,

	`gender` VARCHAR(10) NOT NULL,
	`phoneNumber` VARCHAR(50) NOT NULL,
	`password` VARCHAR(255) NOT NULL);
    /*PRIMARY KEY (`adminstratorID`));*/

