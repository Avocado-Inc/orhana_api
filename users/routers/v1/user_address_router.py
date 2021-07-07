from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import parse_obj_as

from globals.dto import CurrentUser
from users.dto.requests import UserAddressDto
from users.dto.response import UserAddressResponse
from users.services import AuthService
from users.services import UserService

user_address_api_router = APIRouter(tags=["User Address"])


@user_address_api_router.get("/", response_model=UserAddressResponse)
def list_user_address(
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user_addresses = UserService.get_user_addresses(current_user.user_id)
    data = parse_obj_as(List[UserAddressResponse], user_addresses)
    return JSONResponse(
        content=[item.simple_dict() for item in data],
        status_code=status.HTTP_200_OK,
    )


@user_address_api_router.get("/{address_id}", response_model=UserAddressResponse)
def get_user_address(
    address_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user_address = UserService.get_user_address_by_id(address_id, current_user.user_id)
    user_address = UserAddressResponse.from_orm(user_address)
    return JSONResponse(
        content=user_address.simple_dict(),
        status_code=status.HTTP_200_OK,
    )


@user_address_api_router.post("/", response_model=UserAddressResponse)
def add_user_address(
    body: UserAddressDto,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user_address = UserService.add_address(body=body, user_id=current_user.user_id)
    return JSONResponse(
        content=UserAddressResponse.from_orm(user_address).simple_dict(),
        status_code=status.HTTP_200_OK,
    )


@user_address_api_router.put("/{address_id}", response_model=UserAddressResponse)
def add_user_address(
    address_id: UUID,
    body: UserAddressDto,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user_address = UserService.update_address(
        address_id,
        body=body,
        user_id=current_user.user_id,
    )
    return JSONResponse(
        content=UserAddressResponse.from_orm(user_address).simple_dict(),
        status_code=status.HTTP_200_OK,
    )
