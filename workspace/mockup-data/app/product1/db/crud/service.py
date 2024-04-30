from sqlalchemy.orm import Session
from fastapi import HTTPException
from db import model, schema
from core.utils import current_systime

def create_service(service: schema.ServiceCreate, db: Session):
    db_service = model.Service(
        name = service.name,
        price = service.price,
        image = service.image,
        active_status = service.active_status,
        created_datetime = current_systime()
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def select_all_services(db: Session):
    return db.query(model.Service).all()

def select_service_by_id(service_id: int, db: Session):
    db_service = db.query(model.Service).filter(model.Service.service_id == service_id).first()
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    return db_service

def select_service_by_name(name: str, db: Session):
    db_service = db.query(model.Service).filter(model.Service.name == name).first()
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    return db_service

def update_service(service_id: int, service: schema.ServiceUpdate, db: Session):
    db_service = db.query(model.Service).filter(model.Service.service_id == service_id).first()
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
    return db_service

def delete_service(service_id: int, db: Session):
    db_service = db.query(model.Service).filter(model.Service.service_id == service_id).first()
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    db.delete(db_service)
    db.commit()
    return db_service