-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_login-reg
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `users_login-reg` ;

-- -----------------------------------------------------
-- Schema users_login-reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users_login-reg` DEFAULT CHARACTER SET utf8 ;
USE `users_login-reg` ;

-- -----------------------------------------------------
-- Table `users_login-reg`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users_login-reg`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(145) NULL,
  `last_name` VARCHAR(145) NULL,
  `email` VARCHAR(145) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
