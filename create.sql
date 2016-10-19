create database shop  CHARACTER SET utf8 COLLATE utf8_general_ci;
create user 'shop'@'localhost' identified by '1';
grant all privileges on shop.* to 'shop'@'localhost';