# airbyte cdc for mysql
https://airbyte.com/tutorials/mysql-change-data-capture-cdc

# setup
## mysql
docker run -p 127.0.0.1:3306:3306 --name airbyte-mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:8
‍
docker exec -it airbyte-mysql /bin/bash
‍
mysql -p

CREATE DATABASE airbyte;
USE airbyte;
‍
CREATE TABLE cars(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO cars VALUES(0, 'mazda');
INSERT INTO cars VALUES(1, 'honda');

CREATE USER 'airbyte'@'%' IDENTIFIED BY 'password';

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'airbyte'@'%';

## airbyte
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
docker-compose up

## sync test
INSERT INTO cars VALUES(3, 'tesla');
DELETE FROM cars WHERE NAME = 'tesla';

## plus alpha
CREATE TABLE orders(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO orders VALUES(0, '111');
INSERT INTO orders VALUES(1, '222');
UPDATE orders SET name = '222222' WHERE id = 1;
INSERT INTO orders VALUES(2, '333');

ALTER TABLE orders ADD status VARCHAR(30);
INSERT INTO orders VALUES(3, '444', 'ok');
