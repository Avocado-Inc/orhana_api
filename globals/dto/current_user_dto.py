from globals.rest import BaseDto


class CurrentUser(BaseDto):
    user_id: str
    role: str
