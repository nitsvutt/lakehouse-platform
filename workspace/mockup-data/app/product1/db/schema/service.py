from pydantic import BaseModel

class ServiceBase(BaseModel):
    name: str = None
    price: float = None
    image: str = None
    active_status: int = None 

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