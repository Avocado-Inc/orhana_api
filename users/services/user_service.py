from typing import List
from typing import Tuple
from uuid import UUID

from users.dto.requests import UserAddressDto
from users.dto.requests import UserCreateDto
from users.dto.requests import UserUpdateDto
from users.models import User
from users.models import UserAddress


class UserService:
    @staticmethod
    def _create_user(user: UserCreateDto) -> User:
        """create's basic user with mobile number and other optional details.

        :returns User
        """
        user = User.objects.create(**user.simple_dict())
        return user

    @staticmethod
    def get_user_by_mobile(mobile: str) -> Tuple[User, bool]:
        created = False
        try:
            user = User.objects.get(mobile_no=mobile)
            return user, created
        except Exception:
            created = True
            return (
                UserService._create_user(UserCreateDto(**{"mobile_no": mobile})),
                created,
            )

    @staticmethod
    def get_user_by_id(id: UUID) -> User:
        user = User.objects.get(id=id)
        return user

    @staticmethod
    def update_user(id: UUID, body: UserUpdateDto) -> User:
        user = User.objects.filter(id=id).update(**body.simple_dict())
        user = User.objects.get(id=id)
        return user

    @staticmethod
    def add_address(body: UserAddressDto, user_id: UUID):
        user_address = UserAddress.objects.create(
            **{**body.simple_dict(), "user_id": user_id},
        )
        return user_address

    @staticmethod
    def update_address(id: UUID, body: UserAddressDto, user_id: UUID):
        user_address = UserAddress.objects.filter(id=id).update(
            **{**body.simple_dict(), "user_id": user_id},
        )
        user_address = UserAddress.objects.filter(id=id, user_id=user_id).first()
        return user_address

    @staticmethod
    def get_user_addresses(user_id: UUID) -> List[UserAddress]:
        user_addresses = UserAddress.objects.filter(user_id=user_id).order_by(
            "-created_at",
        )
        return list(user_addresses)

    @staticmethod
    def get_user_address_by_id(id: UUID, user_id: UUID) -> List[UserAddress]:
        user_addresses = UserAddress.objects.filter(id=id, user_id=user_id).first()
        return user_addresses
