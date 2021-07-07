from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import parse_obj_as

from globals.dto import CurrentUser
from globals.exceptions import NotFoundException
from inventory.dto.response import CategoryResponse
from inventory.dto.response import SubCategoryResponse
from inventory.models import Category
from inventory.models import SubCategory
from users.services import AuthService

category_router = APIRouter(tags=["Category and Sub Category"])


@category_router.get("/", response_model=CategoryResponse)
def list_all_category(
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    categories = Category.objects.filter(is_active=True)
    categories = parse_obj_as(List[CategoryResponse], list(categories))
    return JSONResponse(
        content=[category.simple_dict() for category in categories],
        status_code=status.HTTP_200_OK,
    )


@category_router.get("/subcategories/{category_id}", response_model=SubCategoryResponse)
def list_all_category(
    category_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    category = Category.objects.filter(id=category_id, is_active=True).first()
    if not category:
        raise NotFoundException(detail="Non existent category")
    sub_categories = SubCategory.objects.filter(category_id=category_id, is_active=True)
    sub_categories = parse_obj_as(List[SubCategoryResponse], list(sub_categories))
    return JSONResponse(
        content=[sub_category for sub_category in sub_categories],
        status_code=status.HTTP_200_OK,
    )
