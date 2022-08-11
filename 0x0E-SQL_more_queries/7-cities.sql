-- create database hbtn_0d_usa & table cities (in database hbtn_0d_usa),id INT
-- unique, auto generated, not null & is a primary key,state_id INT,not null
-- &be FOREIGN KEY tht references 2 id of states tbl,name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
