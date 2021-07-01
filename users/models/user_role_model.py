from django.db import models

from globals.constants.role_constants import RoleConstants
from globals.models import BaseModel


class UserRole(BaseModel):
    role = models.CharField(max_length=20, choices=RoleConstants.choices)
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
