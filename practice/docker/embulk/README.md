https://qiita.com/neo_fukafukafukka/items/fb6d7d2fc59289e67560

```
$ docker-compose build --no-cache
$ docker-compose up -d
$ docker exec -it embulk_etl /bin/bash

$ embulk run conf/departments.yml
$ embulk run conf/employees.yml
```
