# cf
https://stackoverrun.com/ja/q/9643617
https://qiita.com/okadadaisuke/items/3f4094b584dbce3d5b44
https://qiita.com/yifey/items/cd97445ecd7085cea444
https://qiita.com/Bacchus/items/db0750865d1c597e1dc0
https://qiita.com/nsuhara/items/dd780c2622258d10f961

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

# layer
default では psycopg2 を import できないので layer を追加する

```
arn:aws:lambda:ap-northeast-1:898466741470:layer:psycopg2-py38:1
```

Lambda の Python バージョンは 3.8 を選択すること
