from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel
from notification.constants import NotificationChannel


class Template(BaseModel):
    event = models.ForeignKey("notification.Event", on_delete=models.RESTRICT)
    channel = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L16,
        choices=NotificationChannel.choices,
    )
    title = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L128,
        null=True,
        blank=True,
    )
    body = models.CharField(max_length=GlobalModelConstants.CharLengthConstants.L4096)
    attributes = models.JSONField(default=dict)
    is_templated = models.BooleanField(default=False)
