from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    fields = ("order_status", "payment_captured")
    list_display = ("id", "shopping_cart", "payment_captured", "order_status")
