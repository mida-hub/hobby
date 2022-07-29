import os
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')
