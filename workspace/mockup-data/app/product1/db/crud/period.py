from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_period(period: schema.PeriodCreate, db: Session):
    db_period = (
        db.query(model.Period)
        .filter(model.Period.name == period.name)
        .filter(model.Period.active_date == period.active_date)
        .first()
    )
    if db_period:
        raise HTTPException(
            status_code=409,
            detail="Period name and active date exists"
        )
    
    db_period = model.Period(
        name = period.name,
        factor = period.factor,
        extra = period.extra,
        active_date = period.active_date,
        inactive_date = period.inactive_date,
        updated_datetime = current_systime()
    )
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period

def select_all_period(db: Session):
    return db.query(model.Period).all()

def select_period_by_id(period_id: int, db: Session):
    db_period = (
        db.query(model.Period)
        .filter(model.Period.period_id == period_id)
        .first()
    )
    if not db_period:
        raise HTTPException(
            status_code=404,
            detail="Period not found"
        )
    return db_period

def select_period_by_name(name: str, db: Session):
    db_period = (
        db.query(model.Period)
        .filter(model.Period.name == name)
        .all()
    )
    if not db_period:
        raise HTTPException(
            status_code=404,
            detail="Period not found"
        )
    return db_period

def update_period(period_id: int, period: schema.PeriodUpdate, db: Session):
    db_period = (
        db.query(model.Period)
        .filter(model.Period.name == period.name)
        .filter(model.Period.active_date == period.active_date)
        .first()
    )
    if db_period:
        raise HTTPException(
            status_code=409,
            detail="Period name and active date exists"
        )
    db_period = (
        db.query(model.Period)
        .filter(model.Period.period_id == period_id)
        .first()
    )
    if not db_period:
        raise HTTPException(
            status_code=404,
            detail="Period not found"
        )
    
    update_data = period.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_period, key, value)
    setattr(db_period, 'updated_datetime', current_systime())
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period

def delete_period(period_id: int, db: Session):
    db_period = (
        db.query(model.Period)
        .filter(model.Period.period_id == period_id)
        .first()
    )
    if not db_period:
        raise HTTPException(
            status_code=404,
            detail="Period not found"
        )
    db.delete(db_period)
    db.commit()
    return db_period