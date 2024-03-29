from pprint import pprint
from typing import List
from uuid import UUID

from pydantic import parse_obj_as

from inventory.dto.requests import ProductListQueryDto
from inventory.dto.response import ProductListResponse
from inventory.models import Product
from inventory.models import ProductImage


class ProductService:
    @staticmethod
    def list_products(filters: ProductListQueryDto) -> List[ProductListResponse]:
        filters_dict = filters.simple_dict()
        pprint(filters)
        filters_dict.pop("sort_key")
        filters_dict.pop("sort_direction")
        filters_dict.pop("page")
        filters_dict.pop("limit")
        products = list(
            Product.objects.filter(**filters_dict).order_by(
                f"{filters.sort_direction}{filters.sort_key}",
            ),
        )
        try:
            products = products[
                filters.page * filters.limit : filters.page * filters.limit
                + filters.limit
            ]
            products: List[ProductListResponse] = parse_obj_as(
                List[ProductListResponse],
                products,
            )
            # product_ids = list(map(lambda x: x.id, products))
            # product_images = ProductImage.objects.filter(
            #     product_id__in=product_ids, is_main=True
            # )
            # print(product_images[0].image_url)
            # if product_images.count() != 0:
            #     product_images: List[ProductImageResponse] = parse_obj_as(
            #         List[ProductImageResponse],
            #         list(product_images),
            #     )
            #     print(product_images)
            #     for image in product_images:
            #         for product in products:
            #             if product.id == image.product_id:
            #                 product.image = image
            #                 break

            return products
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_product_by_id(id: UUID, is_active: bool = True):
        product = Product.objects.filter(id=id, is_active=is_active).first()
        return product

    @staticmethod
    def update_product_quantity(id: UUID, quantity: int):
        Product.objects.filter(id=id, is_active=True).update(quantity=quantity)

    @staticmethod
    def get_product_images(id: UUID):
        images = ProductImage.objects.filter(product_id=id, is_active=True)
        return images
