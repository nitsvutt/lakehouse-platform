from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import PRODUCT1_SERVER, PRODUCT1_PORT, PRODUCT1_USER, PRODUCT1_PASSWORD

url = f'postgresql://{PRODUCT1_USER}:{PRODUCT1_PASSWORD}@{PRODUCT1_SERVER}:{PRODUCT1_PORT}/product1'

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()