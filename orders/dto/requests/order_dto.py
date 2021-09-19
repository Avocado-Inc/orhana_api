from typing import Optional
from uuid import UUID

from globals.rest import BaseDto


class OrderSessionDto(BaseDto):
    shopping_cart_id: UUID
    user_id: Optional[UUID]


class OrderPlaceRequestDto(BaseDto):
    shopping_cart_id: UUID
    user_id: Optional[UUID]
    billing_address_id: UUID
    shipping_address_id: UUID
