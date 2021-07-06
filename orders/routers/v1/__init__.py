from fastapi import APIRouter

from .shopping_cart_router import shopping_cart_item_router


orders_app_router = APIRouter(prefix="/v1")

orders_app_router.include_router(
    shopping_cart_item_router,
    prefix="/shopping-cart-item",
)


__all__ = [
    "orders_app_router",
]
