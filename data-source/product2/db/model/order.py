from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from db.session import Base

class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    recorded_date = Column(Date)
    received_address = Column(String)
    received_image = Column(String)
    received_datetime = Column(DateTime)
    reviewed_score = Column(Integer)
    reviewed_comment = Column(String)
    reviewed_image = Column(String)
    reviewed_datetime = Column(DateTime)
    updated_datetime = Column(DateTime)