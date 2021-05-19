from pydantic import BaseSettings
from os.path import join, dirname

class Settings(BaseSettings):
    host: str
    port: int
    database: str
    db_user: str
    password: str

    class Config:
        env_file = join(dirname(__file__), '.env')

settings = Settings()

params = {
    "host": settings.host,
    "port": settings.port,
    "database": settings.database,
    "user": settings.db_user,
    "password": settings.password
}

print(params)
