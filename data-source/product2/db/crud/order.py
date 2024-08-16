from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_order(order: schema.OrderCreate, db: Session):
    db_account = (
        db.query(model.Account)
        .filter(model.Account.account_id == order.account_id)
        .first()
    )
    if not db_account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )
    db_product = (
        db.query(model.Product)
        .filter(model.Product.product_id == order.product_id)
        .first()
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    
    db_order = model.Order(
        account_id = order.account_id,
        product_id = order.product_id,
        quantity = order.quantity,
        recorded_date = order.recorded_date,
        received_address = order.received_address,
        received_image = order.received_image,
        received_datetime = current_systime(),
        reviewed_score = order.reviewed_score,
        reviewed_comment = order.reviewed_comment,
        reviewed_image = order.reviewed_image,
        reviewed_datetime = current_systime(),
        updated_datetime = current_systime()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def select_all_order(db: Session):
    return db.query(model.Order).all()

def select_order_by_id(order_id: int, db: Session):
    db_order = (
        db.query(model.Order)
        .filter(model.Order.order_id == order_id)
        .first()
    )
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return db_order

def select_order_by_account_id(account_id: int, db: Session):
    db_order = (
        db.query(model.Order)
        .filter(model.Order.account_id == account_id)
        .all()
    )
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return db_order

def select_order_by_product_id(product_id: int, db: Session):
    db_order = (
        db.query(model.Order)
        .filter(model.Order.product_id == product_id)
        .all()
    )
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return db_order

def update_order(order_id: int, order: schema.OrderUpdate, db: Session):
    db_order = (
        db.query(model.Order)
        .filter(model.Order.order_id == order_id)
        .first()
    )
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    if order.account_id is not None:
        db_account = (
            db.query(model.Account)
            .filter(model.Account.account_id == order.account_id)
            .first()
        )
        if not db_account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )
    if order.product_id is not None:
        db_product = (
            db.query(model.Product)
            .filter(model.Product.product_id == order.product_id)
            .first()
        )
        if not db_product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )
    
    update_data = order.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_order, key, value)
    setattr(db_order, 'updated_datetime', current_systime())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(order_id: int, db: Session):
    db_order = (
        db.query(model.Order)
        .filter(model.Order.order_id == order_id)
        .first()
    )
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    db.delete(db_order)
    db.commit()
    return db_order