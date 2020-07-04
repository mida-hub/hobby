# docker practice 1
## docker image pull
```
docker image pull gihyodocker/echo:latest
```
## docker container run 
```
docker container run -t -p 9000:8000 gihyodocker/echo:latest
```

- t option : assign image name
- p option : port fowarding

```
dcoker container run -d gihyodocker/echo:latest
```

- d option : stay background

## docker image build 
```
docker image build -t example/echo:latest .
docker image ls
docker help

- f option : assign Dockerfile

```
docker image build -f Dockerfile-test -t example/echo:latest .
```

- pull option : docker image pull with force

```
docker image build --pull=true -t example/echo:latest .
docker search --limit 5 mysql
```

- tag option : assign tag name

```
docker image tag example/echo:latest example/echo:0.1.0
docker image push stormcattest/echo:latest
```

## タグのついていないイメージの一括削除
```
docker image prune
```

## docker rmi image_id
```
docker rmi image_id
docker rmi $(docker image ls -q)
```

## docker container ls
```
docker container ls
docker container stop
docker container restart echo
docker container rm
```

## docker container logs
```
docker container logs
docker container logs [service_name]
```

- tail

```
docker container logs -f

docker container exec -it echo sh
docker container cp
```

## 停止コンテナ一括削除
```
docker container prune
```

## 停止コンテナ、タグ無しイメージ、未使用ボリューム、未使用ネットワーク一括削除
```
docker system prune

docker-compose up -d
```

## 一回目の立ち上げではbuildを使用する
```
docker-compose up --build
docker-compose down
docker-compose ps
```

## イメージ再構築 Dockerfile更新時などに使用する
```
docker-compose build
```

## コンテナを立ち上けっぱなしにする
```
tty: true
```

# docker practice 2
## dockerイメージを取得
```
docker pull 
```

## 起動中のcontainerに入る
```
docker run -it ubuntu bash
docker exec -it container_id bash
```

## containerから出る
### containerも終了する
exit

### containerを起動したまま抜ける
ctrl+p+q

## container再起動
```
docker restart container_id
```

## docker container 登録
```
docker commit container_id ubuntu:update
docker commit 58ecfe2d6312 ubuntu:update
```

## docker tag
<hostname>:<port>/<username>/<repository>:<tag>
default:
    - hostname: registry-1.docker.ip
    - username: library

docker tag ubuntu:update <username>/my-first-repo

## docker push
```
docker push mida12251141/my-first-repo
```

## docker rmi (remove image)

## docker ps -aq
docker ps の container_id 一覧

## docker container rm
### 一括削除
```
docker container rm $(docker ps -aq)
```

## docker run
run = create + start

## docker run -it
- i: interactive インプット可能
- t: tty 擬似端末

## docker run -d image
コンテナを起動後にdetachする(バックグラウンド)

```
docker run -it -d ubuntu bash
```

## docker run --rm image
コンテナをExit後に削除する

## docker build .
Dockerfile を build する
name:tag

```
docker build -t new_ubuntu:latest .
```

## docker run -it -v
ホストのディレクトリにマウントする

```
docker run -it -v ~/host_folder:/container_folder imageid bash
```

## docker run -it -v -u
ユーザーIDとグループIDを指定してコンテナを起動する

## sysctl -n hw.physicalcpu_max
物理コア数

## sysctl -n hw.logicalcpu_max
論理コア数

## sysctl hw.memsize
メモリ(byte)

## cpu memory 上限指定

```
docker run -it --rm --cpus 4 --memory 2g ubuntu bash
```

## docker inspect container_id
コンテナ情報を取得する

```
docker inspect container_id | grep -i cpu
docker inspect container_id | grep -i memory
```
