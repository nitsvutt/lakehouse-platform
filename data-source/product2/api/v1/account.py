import typing
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.schema import Account, AccountCreate, AccountUpdate
from db.session import get_db
from db.crud import (
    create_account,
    select_all_account,
    select_account_by_id,
    select_account_by_username,
    select_account_by_first_name,
    select_account_by_phone_number,
    select_account_by_email,
    update_account,
    delete_account
)

account_router = APIRouter()

@account_router.post(
    "/create",
    response_model=Account,
    name="Create account",
    status_code=status.HTTP_201_CREATED,
    response_model_exclude_none=True
)
async def create_a_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(account=account, db=db)

@account_router.get(
    "/get/all",
    response_model=typing.List[Account],
    name="Get all account",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_all_account(db: Session = Depends(get_db)):
    return select_all_account(db=db)

@account_router.get(
    "/get/account_id={account_id}",
    response_model=Account,
    name="Get account by account id",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_account_by_id(account_id: int, db: Session = Depends(get_db)):
    return select_account_by_id(account_id=account_id, db=db)

@account_router.get(
    "/get/username={username}",
    response_model=Account,
    name="Get account by username",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_account_by_username(username: str, db: Session = Depends(get_db)):
    return select_account_by_username(username=username, db=db)

@account_router.get(
    "/get/first_name={first_name}",
    response_model=typing.List[Account],
    name="Get account by first name",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_account_by_first_name(first_name: str, db: Session = Depends(get_db)):
    return select_account_by_first_name(first_name=first_name, db=db)

@account_router.get(
    "/get/phone_number={phone_number}",
    response_model=typing.List[Account],
    name="Get account by phone number",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_account_by_phone_number(phone_number: str, db: Session = Depends(get_db)):
    return select_account_by_phone_number(phone_number=phone_number, db=db)

@account_router.get(
    "/get/email={email}",
    response_model=typing.List[Account],
    name="Get account by email",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def get_account_by_email(email: str, db: Session = Depends(get_db)):
    return select_account_by_email(email=email, db=db)

@account_router.post(
    "/update/account_id={account_id}",
    response_model=Account,
    name="Update account",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def update_a_account(account_id: int, account:AccountUpdate, db: Session = Depends(get_db)):
    return update_account(account_id=account_id, account=account, db=db)

@account_router.post(
    "/delete/account_id={account_id}",
    response_model=Account,
    name="Delete account",
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def delete_a_account(account_id: int,  db: Session = Depends(get_db)):
    return delete_account(account_id=account_id, db=db)