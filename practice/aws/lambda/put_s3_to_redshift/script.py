import psycopg2
import os
import urllib.parse
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    #get bucket name and file name by s3 put event
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    logger.debug(bucket)
    logger.debug(filename)

    dbname = os.environ['dbname']
    port = os.environ['port']
    user = os.environ['user']
    password = os.environ['password']
    host = os.environ['host']
    aws_iam_role = os.environ['aws_iam_role']
    region = os.environ['region']
    dataset_id = os.environ['dataset_id']
    table_id = os.environ['table_id']

    conn_string = f"dbname='{dbname}' port='{port}' user='{user}' password='{password}' host='{host}'" 
    sql=f"""
        copy {dataset_id}.{table_id} from 's3://{bucket}/{filename}'
        credentials 'aws_iam_role={aws_iam_role}'
        delimiter ' ' region '{region}';
        COMMIT;
        """ 

    # ToDo: connect と execute で関数化する
    logger.debug(sql)
    try:
        logger.debug('db new connect')
        logger.debug(conn_string)
        con = psycopg2.connect(conn_string);
        try:
            logger.debug('db connected')
            cur = con.cursor() 
            logger.debug('query execute')
            cur.execute(sql) 
        except Exception as e:
            logger.error(e)
        finally:
            logger.debug('query finish')
            con.close()
    except Exception as e:
        logger.error(e)
