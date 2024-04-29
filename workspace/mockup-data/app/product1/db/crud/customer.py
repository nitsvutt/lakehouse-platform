from sqlalchemy.orm import Session
from fastapi import HTTPException
from db import model, schema
from core.utils import current_systime

def create_customer(customer: schema.CustomerCreate, db: Session):
    db_customer = model.Customer(
        first_name = customer.first_name,
        last_name = customer.last_name,
        birth_date = customer.birth_date,
        address = customer.address,
        phone_number = customer.phone_number,
        email = customer.email,
        job_title = customer.job_title,
        active_status = customer.active_status,
        created_datetime = current_systime()
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def select_all_customers(db: Session):
    return db.query(model.Customer).all()

def select_customer_by_id(customer_id: int, db: Session):
    customer = db.query(model.Customer).filter(model.Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return customer