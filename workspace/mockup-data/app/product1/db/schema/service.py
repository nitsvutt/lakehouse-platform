from pydantic import BaseModel
from datetime import date

class ServiceBase(BaseModel):
    name: str = None
    price: float = None
    image: str = None
    active_date: date = None
    inactive_date: date = None

class Service(ServiceBase):
    service_id: int

    class Config:
        orm_mode = True

class ServiceCreate(ServiceBase):

    class Config:
        orm_mode = True

class ServiceUpdate(ServiceBase):

    class Config:
        orm_mode = True