from typing import List
from uuid import UUID

from .shopping_cart_response import ShoppingCartItemResponse
from globals.constants import OrderTransitionConstants
from globals.rest import BaseDbResponse
from users.dto.response import UserAddressResponse


class OrderResponse(BaseDbResponse):
    id: UUID
    order_session_id: UUID
    billing_address: UserAddressResponse
    shipping_address: UserAddressResponse
    item: ShoppingCartItemResponse
    order_status: OrderTransitionConstants.ENUMS
    final_price: float
    quantity: int = 1
    unit_price = float
    applied_discount_percentage: float


class OrderSessionResponse(BaseDbResponse):
    id: UUID
    final_total: float
    tax_percentage: float
    orders: List[OrderResponse]
