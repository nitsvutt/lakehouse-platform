from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime, hasher

def create_account(account: schema.AccountCreate, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.username == account.username)
        .first()
    )
    if db_account:
        raise HTTPException(
            status_code=409,
            detail="Username exists"
        )
    
    db_account = model.Account(
        username = account.username,
        password = hasher.get_password(account.password),
        first_name = account.first_name,
        last_name = account.last_name,
        birth_date = account.birth_date,
        address = account.address,
        phone_number = account.phone_number,
        email = account.email,
        job_title = account.job_title,
        updated_datetime = current_systime()
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def select_all_account(db: Session):
    return db.query(model.Account).all()

def select_account_by_id(account_id: int, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.account_id == account_id)
        .first()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    return db_account

def select_account_by_username(username: str, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.username == username)
        .first()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    return db_account

def select_account_by_first_name(first_name: str, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.first_name == first_name)
        .all()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    return db_account

def select_account_by_phone_number(phone_number: str, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.phone_number == phone_number)
        .all()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    return db_account

def select_account_by_email(email: str, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.email == email)
        .all()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    return db_account

def update_account(account_id: int, account: schema.AccountUpdate, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.account_id == account_id)
        .first()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    if not account.password and hasher.verify_password(account.password, db_account.password):
        raise HTTPException(
            status_code=409,
            detail="Password has no change"
        )
    update_data = account.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_account, key, value)
    setattr(db_account, 'updated_datetime', current_systime())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(account_id: int, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.account_id == account_id)
        .first()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    db.delete(db_account)
    db.commit()
    return db_account