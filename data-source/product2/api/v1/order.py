import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date

from db.schema import Order, OrderCreate, OrderUpdate
from db.session import get_db
from db.crud import (
    create_order,
    select_all_order,
    select_order_by_id,
    select_order_by_account_id,
    select_order_by_product_id,
    update_order,
    delete_order
)

order_router = APIRouter()

@order_router.post(
    "/create",
    response_model=Order,
    name="Create order",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_an_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(order=order, db=db)

@order_router.get(
    "/get/all",
    response_model=typing.List[Order],
    name="Get all order",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_order(db: Session = Depends(get_db)):
    return select_all_order(db=db)

@order_router.get(
    "/get/order_id={order_id}",
    response_model=Order,
    name="Get order by order id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    return select_order_by_id(order_id=order_id, db=db)

@order_router.get(
    "/get/account_id={account_id}",
    response_model=typing.List[Order],
    name="Get order by account id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_order_by_first_account_id(account_id: int, db: Session = Depends(get_db)):
    return select_order_by_account_id(account_id=account_id, db=db)

@order_router.get(
    "/get/product_id={product_id}",
    response_model=typing.List[Order],
    name="Get order by product id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_order_by_first_product_id(product_id: int, db: Session = Depends(get_db)):
    return select_order_by_product_id(product_id=product_id, db=db)

@order_router.post(
    "/update/order_id={order_id}",
    response_model=Order,
    name="Update order",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_an_order(order_id: int, order:OrderUpdate,  db: Session = Depends(get_db)):
    return update_order(order_id=order_id, order=order, db=db)

@order_router.post(
    "/delete/order_id={order_id}",
    response_model=Order,
    name="Delete order",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_an_order(order_id: int,  db: Session = Depends(get_db)):
    return delete_order(order_id=order_id, db=db)