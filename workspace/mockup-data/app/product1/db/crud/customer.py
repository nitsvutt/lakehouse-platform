from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_customer(customer: schema.CustomerCreate, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.customer_id == customer.customer_id)
        .filter(model.Customer.active_date == customer.active_date)
        .first()
    )
    if db_customer:
        raise HTTPException(
            status_code=409,
            detail="Customer exists"
        )
    
    db_customer = model.Customer(
        customer_id = customer.customer_id,
        first_name = customer.first_name,
        last_name = customer.last_name,
        birth_date = customer.birth_date,
        address = customer.address,
        phone_number = customer.phone_number,
        email = customer.email,
        job_title = customer.job_title,
        active_date = customer.active_date,
        inactive_date = customer.inactive_date,
        created_datetime = current_systime()
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    db_customer_hist = model.CustomerHist(
        customer_id = db_customer.customer_id,
        first_name = db_customer.first_name,
        last_name = db_customer.last_name,
        birth_date = db_customer.birth_date,
        address = db_customer.address,
        phone_number = db_customer.phone_number,
        email = db_customer.email,
        job_title = db_customer.job_title,
        active_date = db_customer.active_date,
        inactive_date = db_customer.inactive_date,
        created_datetime = db_customer.created_datetime
    )
    db.add(db_customer_hist)
    db.commit()

    return db_customer

def select_all_customers(db: Session):
    return db.query(model.Customer).all()

def select_customer_by_id(system_id: int, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.system_id == system_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_first_name(first_name: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.first_name == first_name)
        .all()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_phone_number(phone_number: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.phone_number == phone_number)
        .all()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def select_customer_by_email(email: str, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.email == email)
        .all()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return db_customer

def update_customer(system_id: int, customer: schema.CustomerUpdate, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.system_id == system_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    update_data = customer.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_customer, key, value)
    setattr(db_customer, 'updated_datetime', current_systime())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    db_customer_hist = model.CustomerHist(
        customer_id = db_customer.customer_id,
        first_name = db_customer.first_name,
        last_name = db_customer.last_name,
        birth_date = db_customer.birth_date,
        address = db_customer.address,
        phone_number = db_customer.phone_number,
        email = db_customer.email,
        job_title = db_customer.job_title,
        active_date = db_customer.active_date,
        inactive_date = db_customer.inactive_date,
        created_datetime = db_customer.created_datetime,
        updated_datetime = db_customer.updated_datetime
    )
    db.add(db_customer_hist)
    db.commit()

    return db_customer

def delete_customer(system_id: int, db: Session):
    db_customer = (
        db.query(model.Customer)
        .filter(model.Customer.system_id == system_id)
        .first()
    )
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    db.delete(db_customer)
    db.commit()

    db_customer_hist = model.CustomerHist(
        customer_id = db_customer.customer_id,
        first_name = db_customer.first_name,
        last_name = db_customer.last_name,
        birth_date = db_customer.birth_date,
        address = db_customer.address,
        phone_number = db_customer.phone_number,
        email = db_customer.email,
        job_title = db_customer.job_title,
        active_date = db_customer.active_date,
        inactive_date = db_customer.inactive_date,
        created_datetime = db_customer.created_datetime,
        updated_datetime = current_systime()
    )
    db.add(db_customer_hist)
    db.commit()

    return db_customer