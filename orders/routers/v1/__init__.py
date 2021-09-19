from fastapi import APIRouter

from .order_router import order_router
from .shopping_cart_router import shopping_cart_item_router

orders_app_router = APIRouter(prefix="/v1")

orders_app_router.include_router(
    shopping_cart_item_router,
    prefix="/shopping-cart-item",
)
orders_app_router.include_router(
    order_router,
    prefix="/order",
)


__all__ = [
    "orders_app_router",
]
