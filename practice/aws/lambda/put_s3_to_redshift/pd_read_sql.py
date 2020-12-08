import psycopg2
import os
import logging
import pandas as pd

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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

def get_query():
    query=f"""
            SELECT * FROM public.test;
        """
    
    logger.debug(f'query: {query}')

    return query

def execute_query(con_db, query):
    try:
        logger.debug('execute query')
        df = pd.read_sql(sql=query, con=con_db)
    except Exception as e:
        logger.error(e)
        df = None
    finally:
        con_db.close()

    return df

if __name__ == '__main__':
    import dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    dotenv.load_dotenv(dotenv_path)
    con_db = connect_db()

    if con_db is not None:
        query = get_query()
        df = execute_query(con_db, query)
        print(f'df: {df}')
    else:
        print('error')
