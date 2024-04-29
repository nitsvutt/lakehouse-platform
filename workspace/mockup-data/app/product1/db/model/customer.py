from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from db.session import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    job_title = Column(String)
    active_status = Column(Integer)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)

