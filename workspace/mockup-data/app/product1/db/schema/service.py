from pydantic import BaseModel
from datetime import date, datetime

class ServiceBase(BaseModel):
    name: str = None
    price: float = None
    image: str = None
    active_date: date = None
    inactive_date: date = None

class Service(ServiceBase):
    updated_datetime: datetime = None
    service_id: int = None

    class Config:
        orm_mode = True

class ServiceCreate(ServiceBase):

    class Config:
        orm_mode = True

class ServiceUpdate(ServiceBase):

    class Config:
        orm_mode = True