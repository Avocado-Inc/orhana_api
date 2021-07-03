from typing import List

from pydantic import parse_obj_as
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users.dto.requests import UserAddressDto
from users.dto.response import UserAddressResponse
from users.services import UserService


class UserAddressViewSet(ViewSet):
    @action(methods=["GET"], detail=False)
    def list_address(self, request: Request, *args, **kwargs):

        current_user = request._request.current_user
        user_addresses = UserService.get_user_addresses(current_user.user_id)
        print(user_addresses[0])
        data = parse_obj_as(List[UserAddressResponse], user_addresses)
        return Response(
            data=[item.simple_dict() for item in data],
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["GET"], detail=True)
    def get_address(self, request: Request, pk, *args, **kwargs):

        current_user = request._request.current_user
        user_address = UserService.get_user_address_by_id(pk, current_user.user_id)
        parse_obj_as(UserAddressResponse, user_address)
        return Response(
            data=user_address.simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["POST"], detail=False)
    def add_address(self, request: Request, *args, **kwargs):
        current_user = request._request.current_user
        try:
            body = UserAddressDto(**request.data)
        except Exception as e:
            import traceback

            traceback.print_exc()
            print(e)
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        user_address = UserService.add_address(body=body, user_id=current_user.user_id)
        return Response(
            data=UserAddressResponse.from_orm(user_address).simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["PUT"], detail=True)
    def update_address(self, request: Request, pk, *args, **kwargs):
        current_user = request._request.current_user
        try:
            body = UserAddressDto(**request.data)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        user_address = UserService.update_address(
            id=pk,
            body=body,
            user_id=current_user.user_id,
        )
        return Response(
            data=UserAddressResponse.from_orm(user_address).simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
