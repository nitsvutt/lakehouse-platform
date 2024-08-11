from api.v1.customer import customer_router
from api.v1.service import service_router
from api.v1.period import period_router
from api.v1.trans import trans_router
from api.v1.review import review_router

__all__ = [
    customer_router,
    service_router,
    period_router,
    trans_router,
    review_router
]