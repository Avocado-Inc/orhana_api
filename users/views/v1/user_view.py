from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.dto.requests import UserUpdateDto
from users.dto.response import UserResponse
from users.services import AuthService
from users.services import UserService


class UserViewSet(ViewSet):
    @action(methods=["PUT"], detail=False)
    def update_profile(self, request: Request, *args, **kwargs):
        try:
            current_user = AuthService.verify_auth_access_token(request)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            body = UserUpdateDto(**request.data)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user = UserService.update_user(current_user.user_id, body)
        return Response(
            data=UserResponse.from_orm(user).simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["GET"], detail=False)
    def my_profile(self, request: Request, *args, **kwargs):
        try:
            current_user = AuthService.verify_auth_access_token(request)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user = UserService.get_user_by_id(current_user.user_id)
        return Response(
            data=UserResponse.from_orm(user).simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
