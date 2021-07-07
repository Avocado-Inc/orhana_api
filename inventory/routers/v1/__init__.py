from fastapi import APIRouter

from .category_router import category_router
from .product_router_v1 import product_router

inventory_app_router = APIRouter(prefix="/v1")

inventory_app_router.include_router(product_router, prefix="/product")
inventory_app_router.include_router(category_router, prefix="/category")


__all__ = ["inventory_app_router"]
