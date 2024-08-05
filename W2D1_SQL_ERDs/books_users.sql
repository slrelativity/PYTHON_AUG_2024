-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books_db` ;

-- -----------------------------------------------------
-- Schema books_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_db` DEFAULT CHARACTER SET utf8 ;
USE `books_db` ;

-- -----------------------------------------------------
-- Table `books_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_db`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `number_of_pages` INT NULL,
  `chapters` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `readers_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_books_users1_idx` (`readers_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_users1`
    FOREIGN KEY (`readers_id`)
    REFERENCES `books_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_db`.`publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`publishers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `publisher_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_db`.`books_has_publishers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_db`.`books_has_publishers` (
  `book_id` INT NOT NULL,
  `publisher_id` INT NOT NULL,
  PRIMARY KEY (`book_id`, `publisher_id`),
  INDEX `fk_books_has_publishers_publishers1_idx` (`publisher_id` ASC) VISIBLE,
  INDEX `fk_books_has_publishers_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_has_publishers_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_db`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_books_has_publishers_publishers1`
    FOREIGN KEY (`publisher_id`)
    REFERENCES `books_db`.`publishers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
