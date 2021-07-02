from typing import Any
from typing import Optional
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDto


class ProductListQueryDto(BaseDto):
    product_name: Optional[str] = None
    category_id: Optional[UUID] = None
    sub_catergory_id: Optional[UUID] = None
    sort_direction: Any
    sort_key: Any
    page: Any
    limit: Any

    @validator("sort_key")
    def validate_sort_key(cls, v: str):
        print(v[0])
        assert v[0] in [
            "created_at",
            "max_selling_price",
        ], "allowed keys [created_at, max_selling_prices]"
        return v[0]

    @validator("sort_direction")
    def validate_sort_direction(cls, v: str):
        print(type(v))
        assert v[0] in ["-", "+"], "allowed keys [-, +]"
        return v[0]

    @validator("page")
    def validate_page(cls, v: str):
        print(type(v))

        return int(v[0])

    @validator("limit")
    def validate_limit(cls, v: str):
        print(type(v))

        return int(v[0])
