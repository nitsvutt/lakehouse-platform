from fastapi import FastAPI, Request, Response

from api.v1 import (
    customer_router,
    service_router,
    period_router,
    trans_router,
    review_router
)
from db.session import SessionLocal

product1 = FastAPI()

@product1.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

product1.include_router(
    customer_router,
    prefix="/api/customer",
    tags=["Customer"]
)

product1.include_router(
    service_router,
    prefix="/api/service",
    tags=["Service"]
)

product1.include_router(
    period_router,
    prefix="/api/period",
    tags=["Period"]
)

product1.include_router(
    trans_router,
    prefix="/api/trans",
    tags=["Trans"]
)

product1.include_router(
    review_router,
    prefix="/api/review",
    tags=["Review"]
)