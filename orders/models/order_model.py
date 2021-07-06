from django.db import models

from globals.constants import GlobalModelConstants
from globals.constants import OrderTransitionConstants
from globals.models import BaseModel


class Order(BaseModel):
    shopping_cart = models.ForeignKey("ShoppingCart", on_delete=models.RESTRICT)
    billing_address = models.ForeignKey("users.UserAddress", on_delete=models.RESTRICT)
    shipping_address = models.ForeignKey(
        "users.UserAddress",
        on_delete=models.RESTRICT,
        related_name="shipping_address",
    )

    payment_captured = models.BooleanField(default=False)
    order_status = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L16,
        choices=OrderTransitionConstants.choices,
        default=OrderTransitionConstants.ENUMS.PENDING.value,
    )
