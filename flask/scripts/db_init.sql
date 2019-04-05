CREATE DATABASE IF NOT EXISTS glo2005 CHARACTER SET utf8;

USE glo2005;

CREATE TABLE IF NOT EXISTS Users(id INTEGER NOT NULL AUTO_INCREMENT,
 username VARCHAR(64) NOT NULL UNIQUE, hashedPassword VARCHAR(60) NOT NULL,
  PRIMARY KEY (id));



