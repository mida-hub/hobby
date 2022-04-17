https://zenn.dev/ymasaoka/articles/get-started-with-apache-airflow

# setup
## init
```
docker-compose up
```

## webserver
```
$ docker-compose up -d
$ docker exec -it airflow /bin/bash

airflow users create \
    --username admin \
    --firstname air \
    --lastname flow \
    --role Admin \
    --email test-airflow@test.com
```
