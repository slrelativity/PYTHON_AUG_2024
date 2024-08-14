-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema parties_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `parties_db` ;

-- -----------------------------------------------------
-- Schema parties_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `parties_db` DEFAULT CHARACTER SET utf8 ;
USE `parties_db` ;

-- -----------------------------------------------------
-- Table `parties_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parties_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `parties_db`.`parties`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `parties_db`.`parties` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `what` VARCHAR(45) NULL,
  `location` VARCHAR(145) NULL,
  `date` DATE NULL,
  `all_ages` TINYINT(1) NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_parties_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_parties_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `parties_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
