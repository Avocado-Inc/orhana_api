from typing import Optional

from pydantic import validator
from pydantic.schema import EmailStr

from globals.rest import BaseDto


class UserCreateDto(BaseDto):
    mobile_no: str
    name: Optional[str]


class UserUpdateDto(BaseDto):
    name: Optional[str]
    email: Optional[EmailStr]
    profile_pic_url: Optional[str]

    @validator("name", allow_reuse=True)
    def validate_name(cls, v: Optional[str] = None):
        if v:
            assert len(v) > 3, "name should be atleast 3 characters"
            return v
