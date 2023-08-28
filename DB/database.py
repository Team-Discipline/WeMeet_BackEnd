import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DB_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(SQLALCHEMY_DB_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///./we_meet.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 제너레이터
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
