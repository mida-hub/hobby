from pydantic import BaseSettings
from os.path import join, dirname
import json
import time
import boto3

# Redshift接続情報
class Settings(BaseSettings):
    workgroup_name: str
    database_name: str
    access_key: str
    secret_access_key: str
    s3: str
    iam_role: str

    class Config:
        env_file = join(dirname(__file__), '.env')

settings = Settings()

# 実行するSQLを設定
sql = '''
    select * from public.test;
'''

sql = f"""
    UNLOAD ('select * from public.test')
    TO '{settings.s3}'
    IAM_ROLE '{settings.iam_role}'
    ALLOWOVERWRITE
    FORMAT JSON;
"""

print(sql)

# redshift data api を実行
data_client = boto3.client('redshift-data',
                           aws_access_key_id=settings.access_key,
                           aws_secret_access_key=settings.secret_access_key)
result = data_client.execute_statement(
    WorkgroupName=settings.workgroup_name,
    Database=settings.database_name,
    Sql=sql
)

print(json.dumps(result, indent=4, default=str))

# 非同期処理なので、id を元に処理が完了するのを待つ
id = result['Id']
print(f'id = {id}')

statement = ''
status = ''

while status != 'FINISHED' and status != 'FAILED' and status != 'ABORTED':
    statement = data_client.describe_statement(Id=id)
    status = statement['Status']
    print("Status:", status)
    time.sleep(1)

print('-'*50)
print(json.dumps(statement, indent=4, default=str))

# SELECT文の結果を取得する場合は下記を実行する
# statement = data_client.get_statement_result(Id=id)
# print('-'*50)
# print(json.dumps(statement, indent=4, default=str))
