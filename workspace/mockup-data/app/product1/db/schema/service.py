from pydantic import BaseModel
from datetime import date

class ServiceBase(BaseModel):
    service_id: int | None = None
    name: str = None
    price: float = None
    image: str = None
    active_date: date = None
    inactive_date: date | None = None

class Service(ServiceBase):

    class Config:
        orm_mode = True

class ServiceCreate(ServiceBase):

    class Config:
        orm_mode = True

class ServiceUpdate(ServiceBase):

    class Config:
        orm_mode = True