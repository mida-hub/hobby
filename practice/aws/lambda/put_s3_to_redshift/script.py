import psycopg2
import os
import urllib.parse
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_bucket_and_filename(event):
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    logger.debug(f'bucket: {bucket}')
    logger.debug(f'filename: {filename}')

    return bucket, filename

def connect_db():
    host = os.environ['host']
    port = os.environ['port']
    database = os.environ['database']
    user = os.environ['user']
    password = os.environ['password']
    
    con_dict = {
        'host': host,
        'port': port,
        'database': database,
        'user': user,
        'password': password
    }
    logger.debug(f'con_dict: {con_dict}')

    try:
        con_db = psycopg2.connect(**con_dict)
    except Exception as e:
        logger.error(e)
        con_db = None

    return con_db

def get_query(bucket, filename):
    dataset_id = os.environ['dataset_id']
    table_id = os.environ['table_id']
    aws_iam_role = os.environ['aws_iam_role']
    region = os.environ['region']

    query=f"""
        copy {dataset_id}.{table_id} from 's3://{bucket}/{filename}'
        credentials 'aws_iam_role={aws_iam_role}'
        delimiter ' ' region '{region}';
        COMMIT;
        """
    
    logger.debug(f'query: {query}')

    return query

def execute_query(con_db, query):
    try:
        logger.debug('open cursor')
        cur = con_db.cursor()
        logger.debug('execute query')
        cur.execute(query)
    except Exception as e:
        logger.error(e)
    finally:
        con_db.close()

def lambda_handler(event, context):
    bucket, filename = get_bucket_and_filename(event)
    con_db = connect_db()

    if con_db is None:
        return

    query = get_query(bucket, filename)
    execute_query(con_db, query)

# デバッグ用
if __name__ == '__main__':
    import dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dotenv.load_dotenv(dotenv_path)
    query = get_query('bucket', 'test.txt')
    print(f'query: {query}')
