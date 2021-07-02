from typing import Optional

from pydantic import validator
from pydantic.schema import EmailStr

from globals.constants import AddressTypeConstants
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


class UserAddressDto(BaseDto):
    address_line_1: str
    address_line_2: Optional[str]
    landmark: Optional[str]
    city: str
    state: str
    zip_code: str
    type_of_address: AddressTypeConstants.ENUMS
    is_default: bool = False
    name: str

    @validator("address_line_1", allow_reuse=True)
    def validate_address_line_1(cls, v: str):
        assert len(address_line_1) > 4, "Address line 1 must be atleast 5 characters"
        return v

    @validator("address_line_2", allow_reuse=True)
    def validate_address_line_2(cls, v: Optional[str] = None):
        if v:
            assert (
                len(address_line_2) > 3
            ), "Address line 1 must be atleast 4 characters"
            return v

    @validator("landmark", allow_reuse=True)
    def validate_landmark(cls, v: Optional[str] = None):
        if v:
            assert len(landmark) > 3, "landmark must be atleast 4 characters"
            return v

    @validator("city", allow_reuse=True)
    def validate_city(cls, v: str):
        assert len(city) > 2, "City  must be atleast 3 characters"
        return v

    @validator("state", allow_reuse=True)
    def validate_state(cls, v: str):
        assert len(state) > 2, "State  must be atleast 3 characters"
        return v

    @validator("zip_code", allow_reuse=True)
    def validate_state(cls, v: str):
        assert 7 > len(zip_code) > 5, "Postcode/zip  must be of 6 characters"
        return v
