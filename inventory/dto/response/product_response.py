from typing import Optional
from typing import Union
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDbResponse


class ProductImageResponse(BaseDbResponse):
    product_id: UUID
    image_url: str
    is_main: bool


class ProductListResponse(BaseDbResponse):
    id: Union[UUID, str]
    product_name: str
    max_selling_price: float
    image: Optional[ProductImageResponse]

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()

    @validator("product_name")
    def validate_product_name(cls, v: str):
        return v.title().strip()


class ProductResponse(BaseDbResponse):
    id: Union[UUID, str]
    product_name: str
    max_selling_price: float
    quantity: int
    description: Optional[str]

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()

    @validator("product_name")
    def validate_product_name(cls, v: str):
        return v.title().strip()
