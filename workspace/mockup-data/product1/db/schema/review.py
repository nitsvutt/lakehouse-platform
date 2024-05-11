from pydantic import BaseModel
from datetime import date, datetime

class ReviewBase(BaseModel):
    trans_id: int = None
    score: int = None
    comment: str = None
    image: str = None

class Review(ReviewBase):
    updated_datetime: datetime = None
    review_id: int = None

    class Config:
        from_attributes = True

class ReviewCreate(ReviewBase):

    class Config:
        from_attributes = True

class ReviewUpdate(ReviewBase):

    class Config:
        from_attributes = True