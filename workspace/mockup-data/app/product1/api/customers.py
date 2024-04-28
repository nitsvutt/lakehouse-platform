from fastapi import APIRouter

from db.schema import Customer

customers_router = APIRouter()

@customers_router.get(
    "/select",
    response_model=Customer,
    name="Select customers",
    response_model_exclude_none=True
)
async def select_customers():
    return {"name": "A"}