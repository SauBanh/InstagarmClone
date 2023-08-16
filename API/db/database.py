from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./ig_api.db'
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:0962147976@127.0.0.1:3306/api_instagarm"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()