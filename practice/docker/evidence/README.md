# evidence
https://docs.evidence.dev/getting-started/install-evidence

# 初期設定
```sh
$ mkdir pages
$ mkdir build
$ touch settings.json
```

# pages
pages ディレクトリ配下に hoge.md を作成し、ここに SQL や表示設定を書く

# build
npm run build 時に出力されるディレクトリ

# docker-compose
## evidence コンテナの立ち上げ

```sh
$ docker-compose up -d
```

localhost:3000/settings

evidence の設定画面から DB の接続設定をすると
setting.json をマウントしているので、設定が書き込まれます
次回以降コンテナ立ち上げ時の設定が不要になります
※ このファイルは git 管理に含めないこと

DB 接続設定後に

pages/filename.md

を配置すると

localhost:3000/<filename>

にアクセスできます

## build

```sh
$ docker-compose -f docker-compose-build.yml up
```

build 後に /build にファイルが出力されてコンテナは終了します

## hosting

```sh
$ docker-compose -f docker-compose-nginx.yml up -d
```

localhost
