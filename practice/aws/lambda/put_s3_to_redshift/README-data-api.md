# How to Redshift data-api
1. Secrets Manager に登録する
2. AmazonRedshiftFullAccess / AmazonRedshiftDataFullAccess を付与する
3. Lambda上で boto3.client redshift-data を作成する
4. execute statement で任意のSQLを実行
5. VPC外でもVPC内のRedshiftにクエリを発行できるが、VPC内に配置した場合はVPCエンドポイントにredshift-dataを作成すればOK
