https://qiita.com/neo_fukafukafukka/items/fb6d7d2fc59289e67560

```
$ docker-compose build --no-cache
$ docker-compose up -d
$ docker exec -it embulk_etl /bin/bash
$ mysql -h mysql_etl -u fuka_user training -p fuka_pass

$ embulk preview conf/departments.yml
$ embulk run conf/departments.yml

$ embulk preview conf/employees.yml
$ embulk run conf/employees.yml
```
