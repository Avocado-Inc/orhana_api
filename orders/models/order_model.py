from django.db import models

from globals.constants import GlobalModelConstants
from globals.constants import OrderTransitionConstants
from globals.models import BaseModel


class OrderSession(BaseModel):
    shopping_cart = models.ForeignKey("ShoppingCart", on_delete=models.CASCADE)
    payment_captured = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    # coupon
    final_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    tax_percentage = models.DecimalField(max_digits=4, decimal_places=2, default=18.0)


class Order(BaseModel):
    order_session = models.ForeignKey(
        "OrderSession",
        on_delete=models.RESTRICT,
        default=None,
    )
    billing_address = models.ForeignKey("users.UserAddress", on_delete=models.RESTRICT)
    shipping_address = models.ForeignKey(
        "users.UserAddress",
        on_delete=models.RESTRICT,
        related_name="shipping_address",
    )
    item = models.ForeignKey(
        "inventory.Product",
        on_delete=models.CASCADE,
        default=None,
    )
    order_status = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L16,
        choices=OrderTransitionConstants.choices,
        default=OrderTransitionConstants.ENUMS.PENDING.value,
    )
    final_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    applied_discount_percentage = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
