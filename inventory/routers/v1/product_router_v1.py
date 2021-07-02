from rest_framework.routers import DefaultRouter

from inventory.views.v1 import ProductView

prefix_products = "v1/product"

v1_product_router = DefaultRouter()
v1_product_router.register(f"{prefix_products}", ProductView, basename="product_view")
