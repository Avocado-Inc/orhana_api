from django.db import models

from globals.constants import GlobalModelConstants
from globals.models import BaseModel


class Product(BaseModel):
    product_name = models.CharField(
        max_length=GlobalModelConstants.CharLengthConstants.L128,
    )
    category = models.ForeignKey("inventory.Category", on_delete=models.CASCADE)
    sub_category = models.ForeignKey("inventory.SubCategory", on_delete=models.CASCADE)
    max_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField()
    main_image = models.ImageField(default=None, null=True, blank=True)
    description = models.TextField(
        max_length=GlobalModelConstants.CharLengthConstants.L8192,
        null=True,
        blank=True,
        default="Product description",
        help_text="Add product description",
    )

    def get_image_url(self):
        return self.main_image.url

    image_url = property(get_image_url)

    def __str__(self):
        return f"{self.product_name} - {self.id}"


class ProductImage(BaseModel):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.id}"

    def get_image_url(self):
        return self.image.url

    image_url = property(get_image_url)
