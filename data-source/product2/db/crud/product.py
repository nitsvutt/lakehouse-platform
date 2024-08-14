from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime, hasher

def create_product(product: schema.ProductCreate, db: Session):
    db_product = (
        db.query(model.Product)
        .filter(model.Product.name == product.name)
        .filter(model.Product.active_date == product.active_date)
        .first()
    )
    if db_product:
        raise HTTPException(
            status_code=409,
            detail="Product name and active date exists"
        )
    
    db_product = model.Product(
        name = product.name,
        price = product.price,
        image = product.image,
        active_date = product.active_date,
        inactive_date = product.inactive_date,
        updated_datetime = current_systime()
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def select_all_product(db: Session):
    return db.query(model.Product).all()

def select_product_by_id(product_id: int, db: Session):
    db_product = (
        db.query(model.Product)
        .filter(model.Product.product_id == product_id)
        .first()
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return db_product

def select_product_by_name(name: str, db: Session):
    db_product = (
        db.query(model.Product)
        .filter(model.Product.name == name)
        .all()
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return db_product

def update_product(product_id: int, product: schema.ProductUpdate, db: Session):
    db_product = (
        db.query(model.Product)
        .filter(model.Product.product_id == product_id)
        .first()
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    update_data = product.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_product, key, value)
    setattr(db_product, 'updated_datetime', current_systime())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(product_id: int, db: Session):
    db_product = (
        db.query(model.Product)
        .filter(model.Product.product_id == product_id)
        .first()
    )
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    db.delete(db_product)
    db.commit()
    return db_product