import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.schema import Customer, CustomerCreate, CustomerUpdate
from db.session import get_db
from db.crud import (
    create_customer,
    select_all_customers,
    select_customer_by_id,
    select_customer_by_first_name,
    select_customer_by_phone_number,
    select_customer_by_email,
    update_customer,
    delete_customer
)

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
    "/get/id={customer_id}",
    response_model=Customer,
    name="Get customer by id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    return select_customer_by_id(customer_id=customer_id, db=db)

@customer_router.get(
    "/get/first_name={first_name}",
    response_model=Customer,
    name="Get customer by first name",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_customer_by_first_name(first_name: str, db: Session = Depends(get_db)):
    return select_customer_by_first_name(first_name=first_name, db=db)

@customer_router.get(
    "/get/phone_number={phone_number}",
    response_model=Customer,
    name="Get customer by phone number",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_customer_by_phone_number(phone_number: str, db: Session = Depends(get_db)):
    return select_customer_by_phone_number(phone_number=phone_number, db=db)

@customer_router.get(
    "/get/email={email}",
    response_model=Customer,
    name="Get customer by email",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_customer_by_email(email: str, db: Session = Depends(get_db)):
    return select_customer_by_email(email=email, db=db)

@customer_router.post(
    "/update/id={customer_id}",
    response_model=Customer,
    name="Update customer",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_customer(customer_id: int, customer:CustomerUpdate,  db: Session = Depends(get_db)):
    return update_customer(customer_id=customer_id, customer=customer, db=db)

@customer_router.post(
    "/delete/id={customer_id}",
    response_model=Customer,
    name="Delete customer",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_customer(customer_id: int,  db: Session = Depends(get_db)):
    return delete_customer(customer_id=customer_id, db=db)