# public network
## vpn
1. VPN: redshift 用と RDS 用で2つ作る
2. サブネット
3. インターネットゲートウェイ
4. ルートテーブル
5. セキュリティグループ
6. サブネットグループ

## S3
- bucket: sync-mida-test

## IAM
CLI User を作成する(以降は aws-cli-user とする)

- AmazonRedshiftDataFullAccess
- インラインポリシーの追加でredshift-serverless:GetCredentials でワークグループを指定する

## Redshift
### Redshift Serverless setup
https://dev.classmethod.jp/articles/20220805-amazon-redshift-serverless/

### Role
- AmazonRedshiftAllCommandsFullAccess
- AmazonS3FullAccess

### table
```sql
create table public.test (
    name varchar (10),
    age decimal(3,0)
);

insert into public.test values('alice', 20);
commit;
```

### s3 output
```sql
UNLOAD ('select * from public.test')
TO 's3://sync-mida-test/output/'
IAM_ROLE 'arn:aws:iam::aws_account:role/your_role'
ALLOWOVERWRITE
FORMAT JSON;
```

### data api
権限設定

```sql
select * from pg_user;
GRANT USAGE ON SCHEMA public TO "IAM:aws-cli-user";
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "IAM:aws-cli-user";

-- 権限確認
select
  usename
  , schemaname
  , tablename
  , has_table_privilege(usename, schemaname || '.' || tablename, 'select') as select
from
  pg_tables, pg_user
where
  schemaname in ('public')  -- 確認したいスキーマで絞り込む
and
  usename in ('IAM:aws-cli-user')  -- 確認したいユーザで絞り込む
order by
  1, 2, 3
;
```

## DB
