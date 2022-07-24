from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DABASE_URL = 'sqlite:///.blog.db'

engine = create_engine(DABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
