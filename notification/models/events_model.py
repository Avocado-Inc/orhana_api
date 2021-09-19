from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel


class Event(BaseModel):
    event_key = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L128,
        unique=True,
        db_index=True,
    )
    immediate = models.BooleanField(default=True)
    after_seconds = models.PositiveBigIntegerField(default=0)
