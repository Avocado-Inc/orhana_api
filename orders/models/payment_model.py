from django.db import models

from globals.models import BaseModel


class Payment(BaseModel):
    payment_captured = models.BooleanField(default=False)
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
    order_session = models.ForeignKey(
        "orders.OrderSession",
        on_delete=models.RESTRICT,
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_link_generated = models.URLField(null=True, blank=True)
    meta = models.JSONField(default=dict)
    # rzPay
    # coupon
    def __str__(self):
        return f"{self.id} - {self.payment_captured} - {self.user.mobile_no} - Rs {self.total}"
