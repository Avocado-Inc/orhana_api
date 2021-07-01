from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.dto.requests import LoginDto
from users.dto.requests import RequestOtpDto
from users.services import AuthService


class AuthViewSet(ViewSet):
    @action(methods=["POST"], detail=False)
    def request_otp(self, request: Request, *args, **kwargs):
        try:
            otp_request = RequestOtpDto(**request.data)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        otp_response = AuthService.send_otp(otp_request.mobile_no)
        return Response(
            data=otp_response,
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["POST"], detail=False)
    def validate_otp(self, request: Request, *args, **kwargs):
        try:
            login_data = LoginDto(**request.data)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            otp_response = AuthService.login_mobile(login_data)
            return Response(
                data=otp_response,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["POST"], detail=False)
    def validate_access(self, request: Request, *args, **kwargs):

        try:
            validate_access_response = AuthService.verify_auth_access_token(request)
            return Response(
                data=validate_access_response.simple_dict(),
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["GET"], detail=False)
    def refresh_access(self, request: Request, *args, **kwargs):

        try:
            refresh_access_response = AuthService.issue_new_tookens_from_refresh_token(
                request,
            )
            return Response(
                data=refresh_access_response,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
