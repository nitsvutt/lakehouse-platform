from pydantic import BaseModel
from datetime import date, datetime

class OrderBase(BaseModel):
    account_id: int = None
    product_id: int = None
    quantity: int = None
    status: str = None
    recorded_date: date = None
    received_address: str = None
    received_image: str = None
    reviewed_score: int = None
    reviewed_comment: str = None
    reviewed_image: str = None

class Order(OrderBase):
    updated_datetime: datetime = None
    received_datetime: datetime = None
    reviewed_datetime: datetime = None
    order_id: int = None

    class Config:
        from_attributes = True

class OrderCreate(OrderBase):

    class Config:
        from_attributes = True

class OrderUpdate(OrderBase):
    received_datetime: datetime = None
    reviewed_datetime: datetime = None

    class Config:
        from_attributes = True