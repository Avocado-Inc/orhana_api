from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse

from globals.dto import CurrentUser
from globals.exceptions import NotFoundException
from inventory.dto.response import ProductResponse
from inventory.services import ProductService
from users.services import AuthService


product_router = APIRouter(tags=["Product"])


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
