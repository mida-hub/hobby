# docker practice
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
```
docker container rm $(docker ps -aq)
```

## docker container logs -f
log

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

## docker save/load
docker save image_id > tarfile
docker load < tarfile

## ssh/sftp
```
chmod 0600 xxx.pem
sftp -i xxx.pem ubuntu@ec2.xxx.aws.com
put Dockerfile
ssh -i xxx.pem ubuntu@ec2.xxx.aws.com
sudo apt-get update
sudo apt-get install docker.io
sudo gpasswd -a ubuntu docker
exit
ssh -i xxx.pem ubuntu@ec2.xxx.aws.com

docker build .
docker run -v ~:/work -p 8888:8888 image_id
```

## docker-compose
```
docker build    <->     docker-compose build
docker run      <->     docker-compose up
docker ps       <->     docker-compose ps
docker exec     <->     docker-compose exec
```

## docker-compose up --build -d
buildしてrun

## docker-compose down
stopしてrm

## 断捨離
```
docker system prune
docker system prune --volumes
```

## Mac の DockerEngine の VM に入る
```
docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
```
