from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from db.session import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    job_title = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)

class CustomerHist(Base):
    __tablename__ = "customer_hist"

    customer_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    job_title = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)