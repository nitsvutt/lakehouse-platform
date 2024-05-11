from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Trans(Base):
    __tablename__ = "trans"

    trans_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    customer_id = Column(Integer)
    service_id = Column(Integer)
    period_id = Column(Integer)
    recorded_date = Column(Date)
    updated_datetime = Column(DateTime)