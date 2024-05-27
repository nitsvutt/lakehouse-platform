from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Service(Base):
    __tablename__ = "service"

    service_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    updated_datetime = Column(DateTime)