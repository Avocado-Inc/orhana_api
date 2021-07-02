from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDbResponse


class ProductImageResponse(BaseDbResponse):
    product_id: UUID
    image_url: str
    is_main: bool


class ProductListResponse(BaseDbResponse):
    id: UUID
    product_name: str
    max_selling_price: float
    image: Optional[ProductImageResponse]
    created_at: datetime

    @validator("product_name")
    def validate_product_name(cls, v: str):
        return v.title().strip()


class ProductResponse(BaseDbResponse):
    id: UUID
    product_name: str
    max_selling_price: float
    quantity: int

    @validator("product_name")
    def validate_product_name(cls, v: str):
        return v.title().strip()
