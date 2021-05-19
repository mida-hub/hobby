import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("database")
db_user = os.environ.get("db_user")
password = os.environ.get("password")

params = {
    "host": host,
    "port": port,
    "database": database,
    "user": db_user,
    "password": password
}

print(params)
