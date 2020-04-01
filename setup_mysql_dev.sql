CREATE DATABASE IF NOT EXISTS  hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON DATABASE hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON DATABASE performance_schema.* to 'hbnb_dev'@'localhost'
