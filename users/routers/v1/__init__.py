from fastapi import APIRouter

from .auth_router import auth_api_router
from .user_address_router import user_address_api_router
from .user_router import user_api_router

user_app_router = APIRouter(prefix="/v1")
user_app_router.include_router(auth_api_router, prefix="/auth")
user_app_router.include_router(user_api_router, prefix="/user")
user_app_router.include_router(user_address_api_router, prefix="/user/address")


__all__ = ["user_app_router"]
