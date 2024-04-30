from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from db.session import Base

class Service(Base):
    __tablename__ = "service"

    service_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    active_status = Column(Integer)
    created_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)