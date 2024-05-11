from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Period(Base):
    __tablename__ = "period"

    period_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    name = Column(String)
    factor = Column(Float)
    extra = Column(Float)
    active_date = Column(Date)
    inactive_date = Column(Date)
    updated_datetime = Column(DateTime)