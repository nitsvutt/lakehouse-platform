from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Service(Base):
    __tablename__ = "service"

    system_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    service_id = Column(Integer, server_default=expression.text("True"))
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)

class ServiceHist(Base):
    __tablename__ = "service_hist"

    system_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    service_id = Column(Integer)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)