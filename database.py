from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'fastapi_db'
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# base
Base = declarative_base()

# connection
engine = create_engine(DATABASE_URL)

# session factory: avoid expiring objects on commit so refresh/returning work predictably
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
