# jupyter ssl on amazon linux2
cf.https://dev.classmethod.jp/articles/mesoko-r53-cdn/
cf.https://qiita.com/ysKey2/items/0545e13ec05def42ad55
cf.https://qiita.com/nakanishi03/items/3a514026acc7abe25977
cf.https://oji-cloud.net/2019/09/15/post-3017/

# setup
nginx and jupyter の設定は下記を参照
README_lets_encrypt.md

# SSL作業概要
1. お名前ドットコムでドメインを取得する
2. route53に取得済みのドメインのhosted zoneを作成
3. お名前ドットコムでネームサーバーの変更
4. ACMでパブリック証明書の取得
5. ELBの設定

## domain
お名前ドットコムで取得する

## route53
hosted zoneを作成する

type NS の value を控える

## お名前ドットコム
- ネームサーバーの変更
- 他のネームサーバーを使用
  - route53 で作成した hosted zone の type NS のネームサーバーを登録
  - 最大反映が72時間

## ACM
ドメイン証明書申請

## route53
ACMで設定したドメインのcname生成

## ELB
クライアントからはhttpsアクセス
ALBからInstanceはhttpアクセス

## nginx

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    listen 80 default_server;
    server_name your_domain;
    root /usr/share/nginx/html;

    location /jupyter {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_set_header Origin "http://localhost:8888";
    }
}

server {
    listen 443;
    server_name your_domain;
    root /usr/share/nginx/html;

    location /jupyter {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_set_header Origin "http://localhost:8888";
    }
}
