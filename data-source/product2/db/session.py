from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import PRODUCT2_SERVER, PRODUCT2_PORT, PRODUCT2_USER, PRODUCT2_PASSWORD

url = f'mysql+pymysql://{PRODUCT2_USER}:{PRODUCT2_PASSWORD}@{PRODUCT2_SERVER}:{PRODUCT2_PORT}/product2'

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()