from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel
from notification.constants import NotificationType


class Event(BaseModel):
    event_key = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L128,
        unique=True,
        db_index=True,
    )
    immediate = models.BooleanField(default=True)
    after_seconds = models.PositiveBigIntegerField(default=0)
    notification_type = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L32,
        choices=NotificationType.choices,
    )
