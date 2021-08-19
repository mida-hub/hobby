# docker-machine install
```
curl -L https://github.com/docker/machine/releases/download/v0.12.2/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
chmod +x /usr/local/bin/docker-machine
```

# GCP認証
```
gcloud auth login
gcloud auth application-default login
```

# GCPプロジェクト設定
```
gcloud config set project
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
```

# GCEでの実行環境作成
```
docker-machine create --driver google \
--google-project $PROJECT_ID \
--google-zone asia-northeast1-a \
--google-machine-type f1-micro \
--google-tags 'http-server' \
--google-machine-image https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/images/ubuntu-1604-xenial-v20210429 \
gcp-host
```

# GCEへのアクセスおよびデプロイ
```
docker-machine ssh gcp-host
sudo docker container run --name webserver -it -p 80:80 asashiho/photoview-image
```
