from typing import Optional
from uuid import UUID

from globals.rest import BaseDto


class AddCartItemDto(BaseDto):
    item_id: UUID
    quantity: int = 1
    unit_price: float = 0


class UpdateCartItem(BaseDto):
    quantity: int = 1


class ShoppingCartDto(BaseDto):
    user_id: Optional[UUID]
    number_of_items: int
    total: float
