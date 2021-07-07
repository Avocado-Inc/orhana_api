from fastapi import APIRouter
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse

from globals.exceptions import UnauthorizedException
from users.dto.requests import LoginDto
from users.dto.requests import RequestOtpDto
from users.services import AuthService


auth_api_router = APIRouter(tags=["Auth"])


@auth_api_router.post("/request-otp")
def request_otp(otp_request: RequestOtpDto):
    otp_response = AuthService.send_otp(otp_request.mobile_no)
    return JSONResponse(content=otp_response, status_code=status.HTTP_200_OK)


@auth_api_router.post("/validate-otp")
def validate_otp(login_data: LoginDto):
    try:
        otp_response = AuthService.login_mobile(login_data)
        return JSONResponse(content=otp_response, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(
            content={"message": str(e)},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@auth_api_router.get("/refresh-access")
def refresh_access(request: Request):
    try:
        refresh_access_response = AuthService.issue_new_tokens_from_refresh_token(
            request,
        )
        return JSONResponse(
            content=refresh_access_response,
            status_code=status.HTTP_200_OK,
        )
    except Exception as e:
        raise UnauthorizedException(detail=str(e))
