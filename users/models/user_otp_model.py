from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel


class UserOtp(BaseModel):
    mobile_no = models.CharField(
        max_length=GlobalModelConstants.StandardLengthConstants.MOBILE_NO,
        db_index=True,
    )
    otp = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L8,
        db_index=True,
    )
    is_verified = models.BooleanField(default=False, db_index=True)
    number_of_requests = models.PositiveIntegerField(default=1)
    retries = models.PositiveIntegerField(default=0)
