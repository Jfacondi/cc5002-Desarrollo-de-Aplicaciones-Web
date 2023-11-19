-- -----------------------------------------------------
-- Table `tarea2`.`hincha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`hincha` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `modo_transporte` ENUM("particular", "locomoción pública") NOT NULL,
  `nombre` VARCHAR(80) NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `celular` VARCHAR(15) NULL,
  `comentarios` VARCHAR(80) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_hincha_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_hincha_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `tarea2`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tarea2`.`deporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`deporte` (
	`id`INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(80) NOT NULL,
    PRIMARY KEY (`id`)
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `tarea2`.`hincha_deporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`hincha_deporte` (
  `hincha_id` INT NOT NULL,
  `deporte_id` INT NOT NULL,
  INDEX `fk_hincha_deporte_hincha1_idx` (`hincha_id` ASC),
  INDEX `fk_hincha_deporte_deporte1_idx` (`deporte_id` ASC),
  PRIMARY KEY (`hincha_id`, `deporte_id`),
  CONSTRAINT `fk_hincha_deporte_hincha1`
    FOREIGN KEY (`hincha_id`)
    REFERENCES `tarea2`.`hincha` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hincha_deporte_deporte1`
    FOREIGN KEY (`deporte_id`)
    REFERENCES `tarea2`.`deporte` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

