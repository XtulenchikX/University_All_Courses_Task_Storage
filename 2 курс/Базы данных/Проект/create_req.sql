-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 ;
USE `project` ;

-- -----------------------------------------------------
-- Table `project`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`students` (
  `id_students` VARCHAR(4) NOT NULL,
  `fio` VARCHAR(45) NOT NULL,
  `date_of_birth` DATE NOT NULL CHECK (YEAR(`date_of_birth`) <= 2017),
  `age` INT NULL,
  `sex` VARCHAR(1) NULL,
  `documents` VARCHAR(20) NOT NULL,
  `document_code` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`id_students`),
  UNIQUE INDEX `idstudents_UNIQUE` (`id_students` ASC) VISIBLE,
  UNIQUE INDEX `fio_UNIQUE` (`fio` ASC) VISIBLE,
  UNIQUE INDEX `document_code_UNIQUE` (`document_code` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`parent`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`parent` (
  `fio` VARCHAR(45) NOT NULL,
  `students_id` VARCHAR(4) NOT NULL,
  `phone_number` VARCHAR(12) NOT NULL,
  `email` VARCHAR(40) NULL,
  PRIMARY KEY (`fio`, `students_id`),
  INDEX `parent_to_student_idx` (`students_id` ASC) VISIBLE,
  CONSTRAINT `parent_to_student`
    FOREIGN KEY (`students_id`)
    REFERENCES `project`.`students` (`id_students`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`employees` (
  `id_employees` VARCHAR(4) NOT NULL,
  `fio` VARCHAR(45) NOT NULL,
  `age` INT NULL,
  `date_of_birth` DATE NOT NULL,
  `sex` VARCHAR(45) NULL,
  `document` VARCHAR(30) NOT NULL,
  `document_code` VARCHAR(11) NOT NULL,
  `position` VARCHAR(30) NOT NULL,
  `email` VARCHAR(40) NOT NULL,
  `work_experience (months)` INT NULL,
  `personal_achievements` TEXT NULL,
  PRIMARY KEY (`id_employees`),
  UNIQUE INDEX `id_employees_UNIQUE` (`id_employees` ASC) VISIBLE,
  UNIQUE INDEX `fio_UNIQUE` (`fio` ASC) VISIBLE,
  UNIQUE INDEX `document_code_UNIQUE` (`document_code` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`departments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`departments` (
  `id_departments` VARCHAR(3) NOT NULL,
  `name` VARCHAR(30) NOT NULL,
  `head` VARCHAR(45) NOT NULL,
  `age_restrictions` VARCHAR(15) NOT NULL,
  `description` TEXT NOT NULL,
  PRIMARY KEY (`id_departments`),
  UNIQUE INDEX `id_departments_UNIQUE` (`id_departments` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`classes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`classes` (
  `id_classes` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `departments_id` VARCHAR(3) NOT NULL,
  `employees_id` VARCHAR(4) NOT NULL,
  `classroom` INT NOT NULL,
  `days` VARCHAR(20) NOT NULL,
  `time` VARCHAR(30) NOT NULL,
  `inventory` VARCHAR(45) NULL,
  `recommended_age` VARCHAR(10) NULL,
  `description` TEXT NOT NULL,
  PRIMARY KEY (`id_classes`, `employees_id`, `departments_id`),
  UNIQUE INDEX `id_classes_UNIQUE` (`id_classes` ASC) VISIBLE,
  INDEX `classes_to_dep_idx` (`departments_id` ASC) VISIBLE,
  INDEX `classes_to_emp_idx` (`employees_id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  CONSTRAINT `classes_to_dep`
    FOREIGN KEY (`departments_id`)
    REFERENCES `project`.`departments` (`id_departments`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `classes_to_emp`
    FOREIGN KEY (`employees_id`)
    REFERENCES `project`.`employees` (`id_employees`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`workload`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`workload` (
  `id_workload` INT NOT NULL AUTO_INCREMENT,
  `students_id` VARCHAR(4) NOT NULL,
  `departments_id` VARCHAR(3) NOT NULL,
  `classes_id` VARCHAR(3) NOT NULL,
  `employees_id` VARCHAR(4) NOT NULL,
  `selected days` VARCHAR(20) NOT NULL,
  `teacher's_commentary` TEXT NULL,
  PRIMARY KEY (`id_workload`, `students_id`, `departments_id`, `classes_id`, `employees_id`),
  UNIQUE INDEX `id_student's_plan_UNIQUE` (`id_workload` ASC) VISIBLE,
  INDEX `st_p_to_student_idx` (`students_id` ASC) VISIBLE,
  INDEX `st_p_to_department_idx` (`departments_id` ASC) VISIBLE,
  INDEX `st_p_to_classes_idx` (`classes_id` ASC) VISIBLE,
  INDEX `st_p_to_employee_idx` (`employees_id` ASC) VISIBLE,
  CONSTRAINT `st_p_to_student`
    FOREIGN KEY (`students_id`)
    REFERENCES `project`.`students` (`id_students`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `st_p_to_department`
    FOREIGN KEY (`departments_id`)
    REFERENCES `project`.`departments` (`id_departments`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `st_p_to_classes`
    FOREIGN KEY (`classes_id`)
    REFERENCES `project`.`classes` (`id_classes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `st_p_to_employee`
    FOREIGN KEY (`employees_id`)
    REFERENCES `project`.`employees` (`id_employees`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`events` (
  `id_events` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `place` VARCHAR(45) NOT NULL,
  `date_time` DATETIME NOT NULL,
  `employees_ev_org_id` VARCHAR(4) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id_events`, `employees_ev_org_id`),
  UNIQUE INDEX `idevents_UNIQUE` (`id_events` ASC) VISIBLE,
  INDEX `event_to_employee_idx` (`employees_ev_org_id` ASC) VISIBLE,
  CONSTRAINT `event_to_employee`
    FOREIGN KEY (`employees_ev_org_id`)
    REFERENCES `project`.`employees` (`id_employees`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`users` (
  `Login` VARCHAR(20) NOT NULL,
  `Password` VARCHAR(45) NOT NULL CHECK (`Password` LIKE '________%'),
  `students_id` VARCHAR(4) NULL,
  `employees_id` VARCHAR(4) NULL,
  PRIMARY KEY (`Login`),
  UNIQUE INDEX `Login_UNIQUE` (`Login` ASC) VISIBLE,
  INDEX `users_to_employees_idx` (`employees_id` ASC) VISIBLE,
  UNIQUE INDEX `students_id_UNIQUE` (`students_id` ASC) VISIBLE,
  UNIQUE INDEX `employees_id_UNIQUE` (`employees_id` ASC) VISIBLE,
  CONSTRAINT `users_to_students`
    FOREIGN KEY (`students_id`)
    REFERENCES `project`.`students` (`id_students`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `users_to_employees`
    FOREIGN KEY (`employees_id`)
    REFERENCES `project`.`employees` (`id_employees`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
