from django.db import models

from globals.models import BaseAddressModel
from globals.models import BaseModel


class User(BaseModel):
    mobile_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, blank=True)
    profile_pic_url = models.URLField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)


class UserAddress(BaseAddressModel):
    type_of_address = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False, index=True)
