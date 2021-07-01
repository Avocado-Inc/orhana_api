from typing import Optional
from uuid import UUID

from globals.rest import BaseDbResponse


class UserResponse(BaseDbResponse):
    id: UUID
    name: Optional[str]
    mobile_no: str
    email: Optional[str]
    profile_pic_url: Optional[str]


class UserAddressResponse(BaseDbResponse):
    id: UUID
    address_line_1: str
    address_line_2: Optional[str]
    landmark: Optional[str]
    city: str
    state: str
    zip_code: str
    type_of_address: str
    is_default: bool
