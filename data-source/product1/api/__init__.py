from api.customer import customer_router
from api.service import service_router
from api.period import period_router
from api.trans import trans_router
from api.review import review_router

__all__ = [
    customer_router,
    service_router,
    period_router,
    trans_router,
    review_router
]