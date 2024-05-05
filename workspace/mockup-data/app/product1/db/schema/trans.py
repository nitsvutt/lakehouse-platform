from pydantic import BaseModel
from datetime import date, datetime

class TransBase(BaseModel):
    customer_id: int = None
    service_id: int = None
    period_id: int = None
    recorded_date: date = None

class Trans(TransBase):
    recorded_date: date = None
    updated_datetime: datetime = None
    trans_id: int = None

    class Config:
        from_attributes = True

class TransCreate(TransBase):

    class Config:
        from_attributes = True

class TransUpdate(TransBase):

    class Config:
        from_attributes = True