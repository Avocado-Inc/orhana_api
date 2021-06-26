from globals.rest import BaseDto


class LoginDto(BaseDto):
    id_token: str
    otp: str
    mobile_no: str


class RequestOtpDto(BaseDto):
    id_token: str
    mobile_no: str
