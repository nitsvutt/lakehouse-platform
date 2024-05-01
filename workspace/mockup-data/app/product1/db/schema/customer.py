from pydantic import BaseModel
from datetime import date

class CustomerBase(BaseModel):
    first_name: str = None
    last_name: str = None
    birth_date: date = None
    address: str = None
    phone_number: str = None
    email: str = None
    job_title: str = None
    active_date: date = None
    inactive_date: date | None = None

class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True

class CustomerCreate(CustomerBase):
    customer_id: int | None = None

    class Config:
        orm_mode = True

class CustomerUpdate(CustomerBase):
    customer_id: int | None = None

    class Config:
        orm_mode = True