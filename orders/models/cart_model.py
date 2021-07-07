from django.db import models

from globals.models import BaseModel


class ShoppingCart(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
    purchased = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_items = models.PositiveSmallIntegerField(default=0)


class ShoppingCartItem(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
    shopping_cart = models.ForeignKey("ShoppingCart", on_delete=models.RESTRICT)
    item = models.ForeignKey("inventory.Product", on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
