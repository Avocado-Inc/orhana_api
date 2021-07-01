from globals.constants import RoleConstants
from globals.rest import BaseDto


class LoginDto(BaseDto):
    # id_token: str
    otp: str
    mobile_no: str
    role: str = RoleConstants.ENUMS.CUSTOMER.value


class RequestOtpDto(BaseDto):
    # id_token: str
    mobile_no: str
