import os
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Redshift接続情報
CLUSTER_NAME=os.environ['cluster']
DATABASE_NAME=os.environ['database']
DB_USER=os.environ['user']

# 実行するSQLを設定
sql = '''
    insert into public.test values('test555', 55); commit;
'''

def lambda_handler(event, context):
    logger.info(sql)

    data_client = boto3.client('redshift-data')
    result = data_client.execute_statement(
        ClusterIdentifier=CLUSTER_NAME,
        Database=DATABASE_NAME,
        DbUser=DB_USER,
        Sql=sql,
    )
    
    logger.info(result)
    
    id = result['Id']
    logger.info('id = {}'.format(id))
