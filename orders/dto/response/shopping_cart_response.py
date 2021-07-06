from typing import Union
from uuid import UUID

from pydantic import validator

from globals.rest import BaseDbResponse


class ShoppingCartItemResponse(BaseDbResponse):
    id: Union[UUID, str]
    shopping_cart_id: Union[UUID, str]
    item_id: Union[UUID, str]
    quantity: int = 1
    unit_price: float = 0

    @validator("id")
    def validate_id(cls, v: Union[UUID, str]):
        return str(v)

    @validator("shopping_cart_id")
    def validate_shopping_cart_id(cls, v: Union[UUID, str]):
        return str(v)

    @validator("item_id")
    def validate_item_id(cls, v: Union[UUID, str]):
        return str(v)


class ShoppingCartResponse(BaseDbResponse):
    id: Union[UUID, str]
    number_of_items: int
    total: float
