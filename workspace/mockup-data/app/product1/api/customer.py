import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.schema import Customer, CustomerCreate
from db.session import get_db
from db.crud import create_customer, select_all_customers, select_customer_by_id

customer_router = APIRouter()

@customer_router.post(
    "/create",
    response_model=Customer,
    name="Create customer",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(customer=customer, db=db)

@customer_router.get(
    "/get/all",
    response_model=typing.List[Customer],
    name="Get all customers",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_customers(db: Session = Depends(get_db)):
    return select_all_customers(db=db)

@customer_router.get(
    "/get/id/{customer_id}",
    response_model=Customer,
    name="Get customer by id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    return select_customer_by_id(db=db, customer_id=customer_id)