-- creates database hbtn_0d_usa & table states (in hbtn_0d_usa), id INT unique, 
-- auto generated,not  null & primary key,name VARCHAR(256)not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
