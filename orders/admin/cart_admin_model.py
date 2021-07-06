from django.contrib import admin

from orders.models import ShoppingCart
from orders.models import ShoppingCartItem


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "purchased", "total", "number_of_items")


@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "shopping_cart", "item", "quantity")
