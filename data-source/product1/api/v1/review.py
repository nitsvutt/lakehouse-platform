import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date

from db.schema import Review, ReviewCreate, ReviewUpdate
from db.session import get_db
from db.crud import (
    create_review,
    select_all_review,
    select_review_by_id,
    select_review_by_trans_id,
    update_review,
    delete_review
)

review_router = APIRouter()

@review_router.post(
    "/create",
    response_model=Review,
    name="Create review",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(review=review, db=db)

@review_router.get(
    "/get/all",
    response_model=typing.List[Review],
    name="Get all review",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_review(db: Session = Depends(get_db)):
    return select_all_review(db=db)

@review_router.get(
    "/get/review_id={review_id}",
    response_model=Review,
    name="Get review by review id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_review_by_id(review_id: int, db: Session = Depends(get_db)):
    return select_review_by_id(review_id=review_id, db=db)

@review_router.get(
    "/get/trans_id={trans_id}",
    response_model=typing.List[Review],
    name="Get review by trans id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_review_by_first_trans_id(trans_id: int, db: Session = Depends(get_db)):
    return select_review_by_trans_id(trans_id=trans_id, db=db)

@review_router.post(
    "/update/review_id={review_id}",
    response_model=Review,
    name="Update review",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_review(review_id: int, review:ReviewUpdate,  db: Session = Depends(get_db)):
    return update_review(review_id=review_id, review=review, db=db)

@review_router.post(
    "/delete/review_id={review_id}",
    response_model=Review,
    name="Delete review",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_review(review_id: int,  db: Session = Depends(get_db)):
    return delete_review(review_id=review_id, db=db)