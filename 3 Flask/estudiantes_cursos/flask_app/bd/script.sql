-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_estudiantes_cursos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_estudiantes_cursos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_estudiantes_cursos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_estudiantes_cursos` ;

-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`publicaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`publicaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_publicaciones_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_publicaciones_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_estudiantes_cursos`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`comentarios` (
  `publicacion_id` INT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `post` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `fk_comentarios_publicaciones1_idx` (`publicacion_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_comentarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_comentarios_publicaciones1`
    FOREIGN KEY (`publicacion_id`)
    REFERENCES `esquema_estudiantes_cursos`.`publicaciones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comentarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_estudiantes_cursos`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`Restaurantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`Restaurantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`cursos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_estudiantes_cursos`.`estudiantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_estudiantes_cursos`.`estudiantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `curso_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_estudiantes_cursos1_idx` (`curso_id` ASC) VISIBLE,
  CONSTRAINT `fk_estudiantes_cursos1`
    FOREIGN KEY (`curso_id`)
    REFERENCES `esquema_estudiantes_cursos`.`cursos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
