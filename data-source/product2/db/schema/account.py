from pydantic import BaseModel
from datetime import date, datetime

class AccountBase(BaseModel):
    first_name: str = None
    last_name: str = None
    birth_date: date = None
    address: str = None
    phone_number: str = None
    email: str = None
    job_title: str = None

class Account(AccountBase):
    username: str = None
    updated_datetime: datetime = None
    account_id: int = None

    class Config:
        from_attributes = True

class AccountCreate(AccountBase):
    username: str = None
    password: str = None

    class Config:
        from_attributes = True

class AccountUpdate(AccountBase):
    password: str = None

    class Config:
        from_attributes = True