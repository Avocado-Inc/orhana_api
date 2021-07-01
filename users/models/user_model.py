from django.db import models

from globals.constants import AddressTypeConstants
from globals.models import BaseAddressModel
from globals.models import BaseModel


class User(BaseModel):
    mobile_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, blank=True)
    profile_pic_url = models.URLField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.name}"


class UserAddress(BaseAddressModel):
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
    type_of_address = models.CharField(
        max_length=20,
        choices=AddressTypeConstants.choices,
    )
    is_default = models.BooleanField(default=False, db_index=True)
