from uuid import UUID

from users.dto.requests import UserCreateDto
from users.dto.requests import UserUpdateDto
from users.models import User


class UserService:
    @staticmethod
    def _create_user(user: UserCreateDto) -> User:
        user = User.objects.create(**user.simple_dict())
        return user

    @staticmethod
    def get_user_by_mobile(mobile: str) -> User:
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
