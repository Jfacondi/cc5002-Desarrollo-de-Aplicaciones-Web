-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tarea2` DEFAULT CHARACTER SET utf8 ;
USE `tarea2` ;

-- -----------------------------------------------------
-- Table `tarea2`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comuna_region1_idx` (`region_id` ASC),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `tarea2`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`artesano`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`artesano` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `descripcion_artesania` VARCHAR(300) NULL,
  `nombre` VARCHAR(80) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `celular` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_artesano_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_artesano_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `tarea2`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `artesano_id` INT NOT NULL,
  PRIMARY KEY (`id`, `artesano_id`),
  INDEX `fk_foto_artesano1_idx` (`artesano_id` ASC),
  CONSTRAINT `fk_foto_artesano1`
    FOREIGN KEY (`artesano_id`)
    REFERENCES `tarea2`.`artesano` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`tipo_artesania`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`tipo_artesania` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`artesano_tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`artesano_tipo` (
  `artesano_id` INT NOT NULL,
  `tipo_artesania_id` INT NOT NULL,
  INDEX `fk_artesano_tipo_artesano1_idx` (`artesano_id` ASC),
  INDEX `fk_artesano_tipo_tipo_artesania1_idx` (`tipo_artesania_id` ASC),
  PRIMARY KEY (`tipo_artesania_id`, `artesano_id`),
  CONSTRAINT `fk_artesano_tipo_artesano1`
    FOREIGN KEY (`artesano_id`)
    REFERENCES `tarea2`.`artesano` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_artesano_tipo_tipo_artesania1`
    FOREIGN KEY (`tipo_artesania_id`)
    REFERENCES `tarea2`.`tipo_artesania` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `tarea2`.`tipo_artesania`
-- -----------------------------------------------------
START TRANSACTION;
USE `tarea2`;
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (1, 'mármol');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (2, 'madera');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (3, 'cerámica');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (4, 'mimbre');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (5, 'metal');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (6, 'cuero');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (7, 'telas');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (8, 'joyas');
INSERT INTO `tarea2`.`tipo_artesania` (`id`, `nombre`) VALUES (9, 'otro');

COMMIT;

