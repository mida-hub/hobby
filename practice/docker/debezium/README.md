# debezium
## mysql
### mysql に debezium の権限を付与する
docker-compose up mysql
docker ps
docker exec -it mysql-container-id bash
mysql -p

GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO 'mysql-user'@'%';

### 各種コンテナ起動
mysql -> debezium -> redis
docker-compose up

debezium が立ち上がらない場合は data/offsets.dat を削除する

### monitoring
docker ps
docker exec -it redis-container-id sh
redis-cli monitor

docker exec it mysql-container-id bash
mysql -p

show databases;
show tables;

CREATE TABLE cars(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO cars VALUES(0, 'mazda');
INSERT INTO cars VALUES(1, 'honda');

CREATE TABLE orders(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO orders VALUES(0, '111');
INSERT INTO orders VALUES(1, '222');
UPDATE orders SET name = '222222' WHERE id = 1;
DELETE FROM orders WHERE id = 1;

ALTER TABLE orders ADD status VARCHAR(30);
INSERT INTO orders VALUES(2, '333', 'ok');

## postgres
### postgres に debezium の権限を付与する
docker-compose up postgres
docker ps
docker exec -it postgres-container-id bash
psql -U postgres-user -d postgres

GRANT USAGE ON SCHEMA postgres TO postgres-user
GRANT SELECT ON ALL TABLES IN SCHEMA postgres TO postgres-user
ALTER DEFAULT PRIVILEGES IN SCHEMA postgres GRANT SELECT ON TABLES TO postgres-user
ALTER USER postgres-user REPLICATION LOGIN

### 各種コンテナ起動
postgres -> debezium -> redis
docker-compose up

### monitoring
docker ps
docker exec -it redis-container-id sh  
redis-cli monitor

docker exec it postgres-container-id bash
psql -U postgres-user -d postgres

db一覧
\l
schema一覧
\dn
table一覧
\dt postgres.*

select schemaname, tablename, tableowner from pg_tables;

CREATE SCHEMA postgres;

DB切り替え
\c postgres

CREATE TABLE postgres.cars(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO postgres.cars VALUES(0, 'mazda');
INSERT INTO postgres.cars VALUES(1, 'honda');

CREATE TABLE postgres.orders(id INTEGER, name VARCHAR(200), PRIMARY KEY(id));
INSERT INTO postgres.orders VALUES(0, '111');
INSERT INTO postgres.orders VALUES(1, '222');
UPDATE postgres.orders SET name = '222222' WHERE id = 1;
DELETE FROM postgres.orders WHERE id = 1;

ALTER TABLE postgres.orders ADD status VARCHAR(30);
INSERT INTO postgres.orders VALUES(2, '333', 'ok');
