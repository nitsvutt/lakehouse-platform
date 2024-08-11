import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date

from db.schema import Period, PeriodCreate, PeriodUpdate
from db.session import get_db
from db.crud import (
    create_period,
    select_all_period,
    select_period_by_id,
    select_period_by_name,
    update_period,
    delete_period
)

period_router = APIRouter()

@period_router.post(
    "/create",
    response_model=Period,
    name="Create period",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_period(period: PeriodCreate, db: Session = Depends(get_db)):
    return create_period(period=period, db=db)

@period_router.get(
    "/get/all",
    response_model=typing.List[Period],
    name="Get all period",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_period(db: Session = Depends(get_db)):
    return select_all_period(db=db)

@period_router.get(
    "/get/period_id={period_id}",
    response_model=Period,
    name="Get period by period id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_period_by_id(period_id: int, db: Session = Depends(get_db)):
    return select_period_by_id(period_id=period_id, db=db)

@period_router.get(
    "/get/name={name}",
    response_model=typing.List[Period],
    name="Get period by name",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_period_by_first_name(name: str, db: Session = Depends(get_db)):
    return select_period_by_name(name=name, db=db)

@period_router.post(
    "/update/period_id={period_id}",
    response_model=Period,
    name="Update period",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_period(period_id: int, period:PeriodUpdate,  db: Session = Depends(get_db)):
    return update_period(period_id=period_id, period=period, db=db)

@period_router.post(
    "/delete/period_id={period_id}",
    response_model=Period,
    name="Delete period",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_period(period_id: int,  db: Session = Depends(get_db)):
    return delete_period(period_id=period_id, db=db)