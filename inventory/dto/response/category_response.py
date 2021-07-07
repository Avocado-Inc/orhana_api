from typing import Union
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDbResponse


class CategoryResponse(BaseDbResponse):
    id: Union[UUID, str]
    name: str
    number_of_products: int = 0

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()


class SubCategoryResponse(BaseDbResponse):
    id: Union[UUID, str]
    category_id: Union[UUID, str]
    name: str
    number_of_products: int = 0

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return v.__str__()

    @validator("category_id")
    def validate_category_id(cls, v: Union[UUID, str]):
        return v.__str__()
