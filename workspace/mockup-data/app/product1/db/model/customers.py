from sqlalchemy import Column, String
from pydantic import BaseModel

class Customer(BaseModel):
    name = Column(String)

