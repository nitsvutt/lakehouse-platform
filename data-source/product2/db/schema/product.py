from pydantic import BaseModel
from datetime import date, datetime

class ProductBase(BaseModel):
    name: str = None
    price: float = None
    image: str = None
    active_date: date = None
    inactive_date: date = None

class Product(ProductBase):
    updated_datetime: datetime = None
    product_id: int = None

    class Config:
        from_attributes = True

class ProductCreate(ProductBase):

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):

    class Config:
        from_attributes = True