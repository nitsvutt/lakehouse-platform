import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.schema import Product, ProductCreate, ProductUpdate
from db.session import get_db
from db.crud import (
    create_product,
    select_all_product,
    select_product_by_id,
    select_product_by_name,
    update_product,
    delete_product
)

product_router = APIRouter()

@product_router.post(
    "/create",
    response_model=Product,
    name="Create product",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product=product, db=db)

@product_router.get(
    "/get/all",
    response_model=typing.List[Product],
    name="Get all product",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_product(db: Session = Depends(get_db)):
    return select_all_product(db=db)

@product_router.get(
    "/get/product_id={product_id}",
    response_model=Product,
    name="Get product by product id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return select_product_by_id(product_id=product_id, db=db)

@product_router.get(
    "/get/name={name}",
    response_model=typing.List[Product],
    name="Get product by name",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_product_by_name(name: str, db: Session = Depends(get_db)):
    return select_product_by_name(name=name, db=db)

@product_router.post(
    "/update/product_id={product_id}",
    response_model=Product,
    name="Update product",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_product(product_id: int, product:ProductUpdate, db: Session = Depends(get_db)):
    return update_product(product_id=product_id, product=product, db=db)

@product_router.post(
    "/delete/product_id={product_id}",
    response_model=Product,
    name="Delete product",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(product_id=product_id, db=db)