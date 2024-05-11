from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Account(Base):
    __tablename__ = "account"

    account_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    job_title = Column(String)
    updated_datetime = Column(DateTime)