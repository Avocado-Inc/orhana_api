from django.contrib import admin

from inventory.models import Category
from inventory.models import Product
from inventory.models import ProductImage
from inventory.models import SubCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        "product_name",
        "category",
        "sub_category",
        "max_selling_price",
        "quantity",
    )

    list_display = ("product_name", "sub_category", "max_selling_price", "is_active")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    fields = ("product", "image", "is_main")
    list_display = ("product", "image", "is_active")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "is_active")
    list_display = ("name", "id", "is_active")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ("name", "category", "is_active")
    list_display = ("name", "id", "category", "is_active")
