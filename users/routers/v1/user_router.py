from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from globals.dto import CurrentUser
from users.dto.requests import UserUpdateDto
from users.dto.response import UserResponse
from users.services import AuthService
from users.services import UserService

user_api_router = APIRouter(tags=["User"])


@user_api_router.put("/", response_model=UserResponse)
async def update_profile(
    request: Request,
    body: UserUpdateDto,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user_updated = await UserService.update_user(current_user.user_id, body=body)
    return JSONResponse(
        content=UserResponse.from_orm(user_updated).simple_dict(),
        status_code=status.HTTP_202_ACCEPTED,
    )


@user_api_router.get("/", response_model=UserResponse)
async def my_profile(
    request: Request,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    user = await UserService.get_user_by_id(current_user.user_id)
    return JSONResponse(
        content=UserResponse.from_orm(user).simple_dict(),
        status_code=status.HTTP_202_ACCEPTED,
    )
