# cf
## S3からRedshiftにデータを投入する方法
https://stackoverrun.com/ja/q/9643617

## Role関係でハマったら
https://qiita.com/okadadaisuke/items/3f4094b584dbce3d5b44

## Lambda S3 to Dynamo
https://qiita.com/yifey/items/cd97445ecd7085cea444

## Lambda で psycopg2 を使用するために Layer を追加する
https://qiita.com/Bacchus/items/db0750865d1c597e1dc0

## 【GitHub】に載せたくない環境変数の書き方
https://qiita.com/hedgehoCrow/items/2fd56ebea463e7fc0f5b

## pandas.read_sql
https://dev.classmethod.jp/articles/amazon-redshift2pandas_with_psycopg2/

## Lambda の環境変数を暗号化する場合に KMS を使用する方法
https://qiita.com/ryosuk/items/a44f66913f0454ec5a12

## VPN エンドポイント
https://qiita.com/gymnstcs/items/bd63767a1db0973c32c6

# create table
```
create table public.test (
    name varchar (10),
    age decimal(3,0)
);
```

# VPN
redshift の VPN と同じ場所に lambda を配置する必要がある

# role
- AmazonS3FullAccess
- CloudWatchFullAccess
- AmazonRedshiftFullAccess
- AmazonVPCFullAccess
- kmsの自作ポリシー

# layer
default では psycopg2 を import できないので layer を追加する

```
arn:aws:lambda:ap-northeast-1:898466741470:layer:psycopg2-py38:1
```

Lambda の Python バージョンは 3.8 を選択すること
