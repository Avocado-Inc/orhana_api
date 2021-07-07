import re
from datetime import datetime
from datetime import timedelta

import jwt
from django.core.handlers.wsgi import WSGIRequest
from fastapi import Request

from .user_service import UserService
from globals.dto import CurrentUser
from globals.exceptions import UnauthorizedException
from globals.utils.string import random_number_string
from orhana_api.settings import JWT_AUTH
from users.dto.requests import LoginDto
from users.models import UserRole


class AuthService:
    @staticmethod
    def extract_token(
        request: Request,
    ) -> str:
        """Extracts token from request.

        :param request:
        :return: Token
        """

        token: str = request.headers.get("authorization")
        if not token:
            raise UnauthorizedException()
        return re.sub(JWT_AUTH.get("REGEX"), "", token, 0, re.MULTILINE)

    @staticmethod
    def verify_auth_access_token(request: Request) -> CurrentUser:
        token = AuthService.extract_token(request)
        try:
            decoded = jwt.decode(
                token,
                JWT_AUTH.get("ACCESS_TOKEN_SECRET"),
                algorithms=JWT_AUTH.get("ALGORITHM"),
            )
            decoded.pop("issuer")
            decoded.pop("exp")
        except jwt.exceptions.ExpiredSignatureError:
            raise UnauthorizedException(detail="expired")
        user = UserService.get_user_by_id(decoded.get("user_id"))
        if not user:
            raise UnauthorizedException(detail="user with this token does not exists")
        return CurrentUser(**decoded)

    @staticmethod
    def verify_auth_access_token_middleware(request: WSGIRequest):
        token = request.headers["Authorization"]
        decoded = jwt.decode(
            re.sub(JWT_AUTH.get("REGEX"), "", token, 0, re.MULTILINE),
            JWT_AUTH.get("ACCESS_TOKEN_SECRET"),
            algorithms=JWT_AUTH.get("ALGORITHM"),
        )
        decoded.pop("issuer")
        decoded.pop("exp")
        return CurrentUser(**decoded)

    @staticmethod
    def verify_auth_refresh_token(request: Request) -> dict:
        token = AuthService.extract_token(request)
        decoded = jwt.decode(
            token,
            JWT_AUTH.get("REFRESH_TOKEN_SECRET"),
            algorithms=JWT_AUTH.get("ALGORITHM"),
        )
        return decoded

    @staticmethod
    def issue_new_tokens_from_refresh_token(request: Request) -> dict:
        token = AuthService.extract_token(request)
        decoded: dict = jwt.decode(
            token,
            JWT_AUTH.get("REFRESH_TOKEN_SECRET"),
            algorithms=JWT_AUTH.get("ALGORITHM"),
        )
        decoded.__setitem__(
            "exp",
            datetime.utcnow() + timedelta(seconds=JWT_AUTH.get("ACCESS_EXPIRY")),
        )
        access_token = jwt.encode(
            decoded,
            JWT_AUTH.get("ACCESS_TOKEN_SECRET"),
            algorithm=JWT_AUTH.get("ALGORITHM"),
        )

        return {"access_token": access_token, "refresh_token": token}

    @staticmethod
    def send_otp(mobile_no: str) -> dict:
        otp = random_number_string(n=6)
        # user_otp: UserOtp = UserOtp.objects.filter(
        #     mobile_no=mobile_no,
        #     is_verified=False,
        #     created_at__gte=datetime.utcnow() - timedelta(minutes=5),
        # ).first()
        # if not user_otp:
        #     user_otp: UserOtp = UserOtp.objects.create(mobile_no=mobile_no, otp=otp)
        # if user_otp and user_otp.number_of_requests > 4:
        #     raise Exception()
        # if user_otp:
        #     # send to gupshup/twillio
        #     pass
        return {"message": "Sent otp successfully"}

    @staticmethod
    def _validate_otp(mobile_no: str, otp: str) -> bool:
        return True

    @staticmethod
    def login_mobile(data: LoginDto) -> dict:
        validated = AuthService._validate_otp(data.mobile_no, data.otp)
        if validated:
            user, created = UserService.get_user_by_mobile(data.mobile_no)
            if created:
                user_role = UserRole.objects.create(user=user, role=data.role)
            else:
                user_role = UserRole.objects.filter(user=user, role=data.role).first()
                if not user_role:
                    raise Exception()
            payload = {
                "user_id": str(user.id),
                "role": user_role.role,
                "issuer": "orhana_api",
                "exp": datetime.utcnow()
                + timedelta(seconds=JWT_AUTH.get("ACCESS_EXPIRY")),
            }
            access_token = jwt.encode(
                payload,
                JWT_AUTH.get("ACCESS_TOKEN_SECRET"),
                algorithm=JWT_AUTH.get("ALGORITHM"),
            )

            payload.__setitem__(
                "exp",
                datetime.utcnow() + timedelta(seconds=JWT_AUTH.get("REFRESH_EXPIRY")),
            )

            refresh_token = jwt.encode(
                payload,
                JWT_AUTH.get("REFRESH_TOKEN_SECRET"),
                algorithm=JWT_AUTH.get("ALGORITHM"),
            )
            return {"access_token": access_token, "refresh_token": refresh_token}

        raise Exception()
