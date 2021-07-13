from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import parse_obj_as

from globals.constants import ProductListingSortKey
from globals.constants import SortDirection
from globals.dto import CurrentUser
from globals.exceptions import NotFoundException
from inventory.dto.response import ProductImageResponse
from inventory.dto.response import ProductListResponse
from inventory.dto.response import ProductResponse
from inventory.models import Product
from inventory.services import ProductService
from users.services import AuthService

product_router = APIRouter(tags=["Product"])


@product_router.get("/", response_model=List[ProductListResponse])
def list_products(
    page: int = 0,
    limit: int = 15,
    sort_key: ProductListingSortKey.ENUM = ProductListingSortKey.ENUM.CREATED_AT.value,
    sort_direction: SortDirection.ENUM = SortDirection.ENUM.DESC.value,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    products = list(
        Product.objects.filter(is_active=True).order_by(
            f"{sort_direction.value.strip()}{sort_key.value.strip().lower()}",
        ),
    )
    if products.__len__():
        products = products[page * limit : page * limit + limit]
        products = parse_obj_as(List[ProductListResponse], products)
        return JSONResponse(
            content=[product.simple_dict() for product in products],
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content=[],
            status_code=status.HTTP_200_OK,
        )


@product_router.get("/{product_id}", response_model=ProductResponse)
def get_product_details(
    product_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    product = ProductService.get_product_by_id(product_id)
    if not product:
        raise NotFoundException(detail="No product found")
    return JSONResponse(
        content=ProductResponse.from_orm(product).simple_dict(),
        status_code=status.HTTP_200_OK,
    )


@product_router.get("/{product_id}/images", response_model=List[ProductImageResponse])
def get_product_image_list(
    product_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    product_images = ProductService.get_product_images(product_id)
    if product_images.count():
        product_images = parse_obj_as(List[ProductImageResponse], list(product_images))
    else:
        product_images = []
    return JSONResponse(
        content=[image.simple_dict() for image in product_images],
        status_code=status.HTTP_200_OK,
    )
