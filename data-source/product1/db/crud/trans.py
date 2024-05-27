from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_trans(trans: schema.TransCreate, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.customer_id == trans.customer_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    db_service = (
        db.query(model.Service)
        .filter(model.Service.service_id == trans.service_id)
        .first()
    )
    if not db_service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    
    db_period = (
        db.query(model.Period)
        .filter(model.Period.period_id == trans.period_id)
        .first()
    )
    if not db_period:
        raise HTTPException(
            status_code=404,
            detail="Period not found"
        )
    
    db_trans = model.Trans(
        customer_id = trans.customer_id,
        service_id = trans.service_id,
        period_id = trans.period_id,
        recorded_date = trans.recorded_date,
        updated_datetime = current_systime()
    )
    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans

def select_all_trans(db: Session):
    return db.query(model.Trans).all()

def select_trans_by_id(trans_id: int, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.trans_id == trans_id)
        .first()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    return db_trans

def select_trans_by_customer_id(customer_id: int, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.customer_id == customer_id)
        .all()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    return db_trans

def select_trans_by_service_id(service_id: int, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.service_id == service_id)
        .all()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    return db_trans

def update_trans(trans_id: int, trans: schema.TransUpdate, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.trans_id == trans_id)
        .first()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    if trans.customer_id is not None:
        db_customer = (
            db.query(model.Customer)
            .filter(model.Customer.customer_id == trans.customer_id)
            .first()
        )
        if not db_customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )
    if trans.service_id is not None:
        db_service = (
            db.query(model.Service)
            .filter(model.Service.service_id == trans.service_id)
            .first()
        )
        if not db_service:
            raise HTTPException(
                status_code=404,
                detail="Service not found"
            )
    if trans.period_id is not None:
        db_period = (
            db.query(model.Period)
            .filter(model.Period.period_id == trans.period_id)
            .first()
        )
        if not db_period:
            raise HTTPException(
                status_code=404,
                detail="Period not found"
            )
    
    update_data = trans.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_trans, key, value)
    setattr(db_trans, 'updated_datetime', current_systime())
    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans

def delete_trans(trans_id: int, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.trans_id == trans_id)
        .first()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    db.delete(db_trans)
    db.commit()
    return db_trans