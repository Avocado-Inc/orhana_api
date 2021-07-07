from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=GlobalModelConstants.CharLengthConstants.L16)
    number_of_products = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class SubCategory(BaseModel):
    category = models.ForeignKey("inventory.Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=GlobalModelConstants.CharLengthConstants.L16)
    number_of_products = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.category}"
