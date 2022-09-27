# public network
## vpn
1. VPN: redshift 用と RDS 用で2つ作る
2. サブネット
3. インターネットゲートウェイ
4. ルートテーブル
5. セキュリティグループ
6. サブネットグループ
7. VPCエンドポイント: S3 gateway で作成

## S3
- bucket: sync-mida-test

## IAM
CLI User を作成する(以降は aws-cli-user とする)

- AmazonRedshiftDataFullAccess
- インラインポリシーの追加でredshift-serverless:GetCredentials でワークグループを指定する

## Redshift
### Redshift Serverless setup
- https://dev.classmethod.jp/articles/20220805-amazon-redshift-serverless/
- 拡張VPCををオンにする(そうしないと federated query でうまく接続できない)
- Redshift マネージド VPC エンドポイント を作成する

### Role
- AmazonRedshiftAllCommandsFullAccess
- AmazonS3FullAccess

### data api
権限設定

## DB
1. mysqlとして最小インスタンスで作成する
2. 同一VPCのパブリックネットワークに作成する

## Redshift Federated Query
### Secret Manager
DB の user / password を保存する

### IAM
Redshift の IAM role に Secret Manager がアクセスできるようにする

https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/federated-create-secret-iam-role.html

# public network and 2 vpc
## VPC
1. VPCピアリング
2. ルートテーブルの設定
3. セキュリティグループの許可
