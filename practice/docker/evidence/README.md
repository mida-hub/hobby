# evidence
https://docs.evidence.dev/getting-started/install-evidence

# 初期設定
```sh
$ mkdir pages
$ mkdir build
$ touch settings.json
```

# DB の接続設定
settings.json は git 管理には含めないこと

# pages
pages ディレクトリ配下に hoge.md を作成し、ここに SQL や表示設定を書く

# build
npm run build 時に出力されるディレクトリ

# docker-compose
## evidence コンテナの立ち上げ

```sh
$ docker-compose up -d
$ docker-compose down
```

## build

```sh
$ docker-compose -f docker-compose-build.yml up -d
```

build 後にコンテナは終了します

## hosting

```sh
$ docker-compose -f docker-compose-nginx.yml up -d
$ docker-compose -f docker-compose-nginx.yml down
```
