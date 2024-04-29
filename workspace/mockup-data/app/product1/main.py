from fastapi import FastAPI

from api import customers_router
from core import config

product1 = FastAPI()

product1.include_router(
    customers_router,
    prefix="/api/customers",
    tags=["Customers"]
)
