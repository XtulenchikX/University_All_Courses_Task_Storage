-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LabWork6
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LabWork6
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LabWork6` DEFAULT CHARACTER SET utf8 ;
USE `LabWork6` ;

-- -----------------------------------------------------
-- Table `LabWork6`.`Manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LabWork6`.`Manufacturer` (
  `Manufacturer_name` VARCHAR(45) NOT NULL,
  `Web-site` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Manufacturer_name`),
  UNIQUE INDEX `Manufacturer_name_UNIQUE` (`Manufacturer_name` ASC) VISIBLE,
  UNIQUE INDEX `Web-site_UNIQUE` (`Web-site` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LabWork6`.`Model`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LabWork6`.`Model` (
  `Model_name` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Disk_size` VARCHAR(45) NOT NULL,
  `Rotation_speed` VARCHAR(45) NOT NULL,
  `Interface_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Model_name`, `Manufacturer`),
  UNIQUE INDEX `model_name_UNIQUE` (`Model_name` ASC) VISIBLE,
  CONSTRAINT `Model_to_manufacturer`
    FOREIGN KEY (`Manufacturer`)
    REFERENCES `LabWork6`.`Manufacturer` (`Manufacturer_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LabWork6`.`Disk`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LabWork6`.`Disk` (
  `Serial_Number` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Date_of_purchase` DATETIME NOT NULL,
  `Date_of_breakdown` DATETIME NULL,
  `Comment` TEXT NULL,
  PRIMARY KEY (`Serial_Number`, `Model`),
  UNIQUE INDEX `Serial_Number_UNIQUE` (`Serial_Number` ASC) VISIBLE,
  INDEX `Disk_to_model_idx` (`Model` ASC) VISIBLE,
  CONSTRAINT `Disk_to_model`
    FOREIGN KEY (`Model`)
    REFERENCES `LabWork6`.`Model` (`Model_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
