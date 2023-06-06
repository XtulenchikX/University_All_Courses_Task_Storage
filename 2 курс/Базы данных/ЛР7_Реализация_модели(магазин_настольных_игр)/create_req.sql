-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LR7_Games
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LR7_Games
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LR7_Games` DEFAULT CHARACTER SET utf8 ;
USE `LR7_Games` ;

-- -----------------------------------------------------
-- Table `LR7_Games`.`Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LR7_Games`.`Game` (
  `title` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `min_players` INT NOT NULL,
  `max_players` INT NOT NULL,
  `min_age` INT NULL,
  PRIMARY KEY (`title`, `manufacturer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LR7_Games`.`Clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LR7_Games`.`Clients` (
  `id_client` VARCHAR(5) NOT NULL,
  `surname` VARCHAR(25) NULL,
  `name` VARCHAR(25) NOT NULL,
  `date_of_birth` DATE NULL,
  `phone_number` VARCHAR(20) NULL,
  `mail` VARCHAR(50) NOT NULL,
  `address` VARCHAR(100) NULL,
  PRIMARY KEY (`id_client`),
  UNIQUE INDEX `id_client_UNIQUE` (`id_client` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LR7_Games`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LR7_Games`.`Employees` (
  `service_number` VARCHAR(3) NOT NULL,
  `surname` VARCHAR(25) NOT NULL,
  `name` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`service_number`),
  UNIQUE INDEX `service_number_UNIQUE` (`service_number` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LR7_Games`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LR7_Games`.`Orders` (
  `number` INT NOT NULL AUTO_INCREMENT,
  `method_of_obtaining` VARCHAR(10) NOT NULL,
  `created` DATETIME NOT NULL,
  `client` VARCHAR(5) NOT NULL,
  `employee` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`number`, `client`, `employee`),
  UNIQUE INDEX `number_UNIQUE` (`number` ASC) VISIBLE,
  INDEX `order_to_client_idx` (`client` ASC) VISIBLE,
  INDEX `order_to_emp_idx` (`employee` ASC) VISIBLE,
  CONSTRAINT `order_to_client`
    FOREIGN KEY (`client`)
    REFERENCES `LR7_Games`.`Clients` (`id_client`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `order_to_emp`
    FOREIGN KEY (`employee`)
    REFERENCES `LR7_Games`.`Employees` (`service_number`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LR7_Games`.`Filling`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LR7_Games`.`Filling` (
  `order_number` INT NOT NULL,
  `game_title` VARCHAR(45) NOT NULL,
  `game_manufacturer` VARCHAR(45) NOT NULL,
  `amount` INT NOT NULL,
  PRIMARY KEY (`order_number`, `game_title`, `game_manufacturer`),
  INDEX `filling_to_game_idx` (`game_title` ASC, `game_manufacturer` ASC) VISIBLE,
  CONSTRAINT `filling_to_order`
    FOREIGN KEY (`order_number`)
    REFERENCES `LR7_Games`.`Orders` (`number`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `filling_to_game`
    FOREIGN KEY (`game_title` , `game_manufacturer`)
    REFERENCES `LR7_Games`.`Game` (`title` , `manufacturer`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
