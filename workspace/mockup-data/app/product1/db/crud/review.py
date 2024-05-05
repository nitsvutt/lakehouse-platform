from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import model, schema
from core.utils import current_sysdate, current_systime

def create_review(review: schema.ReviewCreate, db: Session):
    db_trans = (
        db.query(model.Trans)
        .filter(model.Trans.trans_id == review.trans_id)
        .first()
    )
    if not db_trans:
        raise HTTPException(
            status_code=404,
            detail="Trans not found"
        )
    
    db_review = model.Review(
        trans_id = review.trans_id,
        comment = review.comment,
        score = review.score,
        image = review.image,
        updated_datetime = current_systime()
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def select_all_review(db: Session):
    return db.query(model.Review).all()

def select_review_by_id(review_id: int, db: Session):
    db_review = (
        db.query(model.Review)
        .filter(model.Review.review_id == review_id)
        .first()
    )
    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    return db_review

def select_review_by_trans_id(trans_id: int, db: Session):
    db_review = (
        db.query(model.Review)
        .filter(model.Review.trans_id == trans_id)
        .all()
    )
    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    return db_review

def update_review(review_id: int, review: schema.ReviewUpdate, db: Session):
    db_review = (
        db.query(model.Review)
        .filter(model.Review.review_id == review_id)
        .first()
    )
    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    if review.trans_id is not None:
        db_trans = (
            db.query(model.Trans)
            .filter(model.Trans.trans_id == review.trans_id)
            .first()
        )
        if not db_trans:
            raise HTTPException(
                status_code=404,
                detail="Trans not found"
            )
    
    update_data = review.dict()
    for key, value in update_data.items():
        if value is not None:
            setattr(db_review, key, value)
    setattr(db_review, 'updated_datetime', current_systime())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review(review_id: int, db: Session):
    db_review = (
        db.query(model.Review)
        .filter(model.Review.review_id == review_id)
        .first()
    )
    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    db.delete(db_review)
    db.commit()
    return db_review