import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date

from db.schema import Service, ServiceCreate, ServiceUpdate
from db.session import get_db
from db.crud import (
    create_service,
    select_all_service,
    select_service_by_id,
    select_service_by_name,
    update_service,
    delete_service
)

service_router = APIRouter()

@service_router.post(
    "/create",
    response_model=Service,
    name="Create service",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_service(service: ServiceCreate, db: Session = Depends(get_db)):
    return create_service(service=service, db=db)

@service_router.get(
    "/get/all",
    response_model=typing.List[Service],
    name="Get all service",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_service(db: Session = Depends(get_db)):
    return select_all_service(db=db)

@service_router.get(
    "/get/service_id={service_id}",
    response_model=Service,
    name="Get service by service id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_service_by_id(service_id: int, db: Session = Depends(get_db)):
    return select_service_by_id(service_id=service_id, db=db)

@service_router.get(
    "/get/name={name}",
    response_model=typing.List[Service],
    name="Get service by name",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_service_by_first_name(name: str, db: Session = Depends(get_db)):
    return select_service_by_name(name=name, db=db)

@service_router.post(
    "/update/service_id={service_id}",
    response_model=Service,
    name="Update service",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_service(service_id: int, service:ServiceUpdate,  db: Session = Depends(get_db)):
    return update_service(service_id=service_id, service=service, db=db)

@service_router.post(
    "/delete/service_id={service_id}",
    response_model=Service,
    name="Delete service",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_service(service_id: int,  db: Session = Depends(get_db)):
    return delete_service(service_id=service_id, db=db)