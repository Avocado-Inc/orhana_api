from typing import Optional
from typing import Union
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDbResponse


class UserResponse(BaseDbResponse):
    id: Union[UUID, str]
    name: Optional[str]
    mobile_no: str
    email: Optional[str]
    profile_pic_url: Optional[str]

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()


class UserAddressResponse(BaseDbResponse):
    id: Union[UUID, str]
    address_line_1: str
    address_line_2: Optional[str]
    landmark: Optional[str]
    city: str
    state: str
    zip_code: str
    type_of_address: str
    is_default: bool

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()
