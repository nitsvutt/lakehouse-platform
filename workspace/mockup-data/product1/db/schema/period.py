from pydantic import BaseModel
from datetime import date, datetime

class PeriodBase(BaseModel):
    name: str = None
    factor: float = None
    extra: float = None
    active_date: date = None
    inactive_date: date = None

class Period(PeriodBase):
    updated_datetime: datetime = None
    period_id: int = None

    class Config:
        from_attributes = True

class PeriodCreate(PeriodBase):

    class Config:
        from_attributes = True

class PeriodUpdate(PeriodBase):

    class Config:
        from_attributes = True