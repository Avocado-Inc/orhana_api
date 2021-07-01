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

    objects = models.QuerySet


class BaseAddressModel(BaseModel):
    """Base Address model for project."""

    address_line_1 = models.CharField(max_length=256)
    address_line_2 = models.CharField(max_length=256, blank=True, null=True)
    landmark = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=32)

    class Meta:
        abstract = True
