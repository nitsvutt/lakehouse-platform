from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from db.session import Base

class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)
    active_date = Column(Date)
    inactive_date = Column(Date)
    updated_datetime = Column(DateTime)