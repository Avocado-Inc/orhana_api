import uuid

from django.db import models


class BaseModel(models.Model):
    """Base Model for project All models should inherit this model."""

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        db_index=True,
        editable=False,
        default=uuid.uuid4,
    )
    created_by = models.UUIDField(null=True, blank=True)
    updated_by = models.UUIDField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True
