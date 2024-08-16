from fastapi import FastAPI, Request, Response

from api.v1 import (
    account_router,
    product_router,
    order_router
)
from db.session import SessionLocal

product2 = FastAPI()

@product2.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

product2.include_router(
    account_router,
    prefix="/api/account",
    tags=["Account"]
)

product2.include_router(
    product_router,
    prefix="/api/product",
    tags=["Product"]
)

product2.include_router(
    order_router,
    prefix="/api/order",
    tags=["Order"]
)