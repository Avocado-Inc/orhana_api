from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    fields = ("order_status", "item")
    list_display = ("id", "order_session", "item", "order_status")
