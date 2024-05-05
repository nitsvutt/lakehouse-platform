import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date

from db.schema import Trans, TransCreate, TransUpdate
from db.session import get_db
from db.crud import (
    create_trans,
    select_all_trans,
    select_trans_by_id,
    select_trans_by_customer_id,
    select_trans_by_service_id,
    update_trans,
    delete_trans
)

trans_router = APIRouter()

@trans_router.post(
    "/create",
    response_model=Trans,
    name="Create trans",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_trans(trans: TransCreate, db: Session = Depends(get_db)):
    return create_trans(trans=trans, db=db)

@trans_router.get(
    "/get/all",
    response_model=typing.List[Trans],
    name="Get all trans",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_trans(db: Session = Depends(get_db)):
    return select_all_trans(db=db)

@trans_router.get(
    "/get/trans_id={trans_id}",
    response_model=Trans,
    name="Get trans by trans id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_trans_by_id(trans_id: int, db: Session = Depends(get_db)):
    return select_trans_by_id(trans_id=trans_id, db=db)

@trans_router.get(
    "/get/customer_id={customer_id}",
    response_model=typing.List[Trans],
    name="Get trans by customer id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_trans_by_first_customer_id(customer_id: int, db: Session = Depends(get_db)):
    return select_trans_by_customer_id(customer_id=customer_id, db=db)

@trans_router.get(
    "/get/service_id={service_id}",
    response_model=typing.List[Trans],
    name="Get trans by service id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_trans_by_first_service_id(service_id: int, db: Session = Depends(get_db)):
    return select_trans_by_service_id(service_id=service_id, db=db)

@trans_router.post(
    "/update/trans_id={trans_id}",
    response_model=Trans,
    name="Update trans",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_trans(trans_id: int, trans:TransUpdate,  db: Session = Depends(get_db)):
    return update_trans(trans_id=trans_id, trans=trans, db=db)

@trans_router.post(
    "/delete/trans_id={trans_id}",
    response_model=Trans,
    name="Delete trans",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_trans(trans_id: int,  db: Session = Depends(get_db)):
    return delete_trans(trans_id=trans_id, db=db)