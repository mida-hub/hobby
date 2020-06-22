# docker practice 1
## docker image pull
docker image pull gihyodocker/echo:latest

## docker container run 
docker container run -t -p 9000:8000 gihyodocker/echo:latest
- t option : assign image name
- p option : port fowarding

dcoker container run -d gihyodocker/echo:latest
- d option : stay background

## docker image build 
docker image build -t example/echo:latest .
docker image ls
docker help

- f option : assign Dockerfile

docker image build -f Dockerfile-test -t example/echo:latest .

- pull option : docker image pull with force

docker image build --pull=true -t example/echo:latest .
docker search --limit 5 mysql

- tag option : assign tag name

docker image tag example/echo:latest example/echo:0.1.0
docker image push stormcattest/echo:latest

## タグのついていないイメージの一括削除
docker image prune

## docker rmi imageid
docker rmi imageid
docker rmi $(docker image ls -q)

## docker container ls
docker container ls
docker container stop
docker container restart echo
docker container rm

## docker container logs
docker container logs
docker container logs [service_name]

- tail

docker container logs -f

docker container exec -it echo sh
docker container cp

## 停止コンテナ一括削除
docker container prune

## 停止コンテナ、タグ無しイメージ、未使用ボリューム、未使用ネットワーク一括削除
docker system prune

docker-compose up -d

## 一回目の立ち上げではbuildを使用する
docker-compose up --build
docker-compose down
docker-compose ps

## イメージ再構築 Dockerfile更新時などに使用する
docker-compose build

## コンテナを立ち上けっぱなしにする
tty: true

# docker practice 2
## dockerイメージを取得
docker pull 

## containerに入る
docker run -it ubuntu bash
docker exec -it container_id bash

## containerから出る
### containerも終了する
exit

### containerを起動したまま抜ける
ctrl+p+q

## container再起動
docker restart container_id

## docker container 登録
docker commit container_id ubuntu:update
docker commit 58ecfe2d6312 ubuntu:update

## docker tag
<hostname>:<port>/<username>/<repository>:<tag>
default:
    - hostname: registry-1.docker.ip
    - username: library

docker tag ubuntu:update <username>/my-first-repo

## docker push
docker push mida12251141/my-first-repo

## docker rmi (remove image)

## docker ps -aq
docker ps の container_id 一覧

## docker container rm
### 一括削除
docker container rm $(docker ps -aq)
