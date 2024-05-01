from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from db import model, schema
from core.utils import current_sysdate, current_systime

def create_service(service: schema.ServiceCreate, db: Session):
    db_service = (
        db.query(model.Service)
        .filter(model.Service.service_id == service.service_id)
        .filter(model.Service.active_date == service.active_date)
        .first()
    )
    if db_service:
        raise HTTPException(
            status_code=409,
            detail="Service exists"
        )
    
    db_service = model.Service(
        service_id = service.service_id,
        name = service.name,
        price = service.price,
        image = service.image,
        active_date = service.active_date,
        inactive_date = service.inactive_date,
        created_datetime = current_systime()
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)

    db_service_hist = model.ServiceHist(
        service_id = db_service.service_id,
        name = db_service.name,
        price = db_service.price,
        image = db_service.image,
        active_date = db_service.active_date,
        inactive_date = db_service.inactive_date,
        created_datetime = db_service.created_datetime
    )
    db.add(db_service_hist)
    db.commit()

    return db_service

def select_all_services(db: Session):
    return db.query(model.Service).all()

def select_service_by_id(system_id: int, db: Session):
    db_service = (
        db.query(model.Service)
        .filter(model.Service.system_id == system_id)
        .first()
    )
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    return db_service

def select_service_by_name(name: str, db: Session):
    db_service = (
        db.query(model.Service)
        .filter(model.Service.name == name)
        .first()
    )
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    return db_service

def update_service(system_id: int, service: schema.ServiceUpdate, db: Session):
    db_service = (
        db.query(model.Service)
        .filter(model.Service.system_id == system_id)
        .first()
    )
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    update_data = service.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_service, key, value)
    setattr(db_service, 'updated_datetime', current_systime())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)

    db_service_hist = model.ServiceHist(
        service_id = db_service.service_id,
        name = db_service.name,
        price = db_service.price,
        image = db_service.image,
        active_date = db_service.active_date,
        inactive_date = db_service.inactive_date,
        created_datetime = db_service.created_datetime,
        updated_datetime = db_service.updated_datetime
    )
    db.add(db_service_hist)
    db.commit()

    return db_service

def delete_service(system_id: int, db: Session):
    db_service = (
        db.query(model.Service)
        .filter(model.Service.system_id == system_id)
        .first()
    )
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    db.delete(db_service)
    db.commit()

    db_service_hist = model.ServiceHist(
        service_id = db_service.service_id,
        name = db_service.name,
        price = db_service.price,
        image = db_service.image,
        active_date = db_service.active_date,
        inactive_date = db_service.inactive_date,
        created_datetime = db_service.created_datetime,
        updated_datetime = current_systime()
    )
    db.add(db_service_hist)
    db.commit()

    return db_service