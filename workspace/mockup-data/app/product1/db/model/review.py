from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from sqlalchemy.sql import expression
from db.session import Base

class Review(Base):
    __tablename__ = "review"

    review_id = Column(Integer, primary_key=True, server_default=expression.text("True"))
    trans_id = Column(Integer)
    score = Column(Integer)
    comment = Column(String)
    image = Column(String)
    updated_datetime = Column(DateTime)