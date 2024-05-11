from pydantic import BaseModel
from datetime import date, datetime

class CustomerBase(BaseModel):
    first_name: str = None
    last_name: str = None
    birth_date: date = None
    address: str = None
    phone_number: str = None
    email: str = None
    job_title: str = None

class Customer(CustomerBase):
    updated_datetime: datetime = None
    customer_id: int = None

    class Config:
        from_attributes = True

class CustomerCreate(CustomerBase):

    class Config:
        from_attributes = True

class CustomerUpdate(CustomerBase):

    class Config:
        from_attributes = True