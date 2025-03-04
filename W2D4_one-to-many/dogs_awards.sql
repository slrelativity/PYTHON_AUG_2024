-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dogs_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dogs_db` ;

-- -----------------------------------------------------
-- Schema dogs_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dogs_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `dogs_db` ;

-- -----------------------------------------------------
-- Table `dogs_db`.`dogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dogs_db`.`dogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `age` INT NULL DEFAULT NULL,
  `breed` VARCHAR(45) NULL DEFAULT NULL,
  `color` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dogs_db`.`awards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dogs_db`.`awards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `title` VARCHAR(45) NULL,
  `dog_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_awards_dogs_idx` (`dog_id` ASC) VISIBLE,
  CONSTRAINT `fk_awards_dogs`
    FOREIGN KEY (`dog_id`)
    REFERENCES `dogs_db`.`dogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
