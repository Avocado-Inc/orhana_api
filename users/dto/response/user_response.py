from typing import Optional
from uuid import UUID

from globals.rest import BaseDbResponse


class UserResponse(BaseDbResponse):
    id: UUID
    name: Optional[str]
    mobile_no: str
    email: Optional[str]
    profile_pic_url: Optional[str]
