from datetime import datetime
from datetime import timedelta
from typing import List

import django.core.exceptions
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic import parse_obj_as
from starlette import status

from globals.dto import CurrentUser
from orders.dto.requests.order_dto import OrderPlaceRequestDto
from orders.dto.response import OrderResponse
from orders.dto.response import OrderSessionResponse
from orders.models import Order
from orders.models import ShoppingCart
from orders.models import ShoppingCartItem
from orders.models.order_model import OrderSession
from users.services import AuthService

order_router = APIRouter(tags=["Order and Order Session"])


@order_router.get("/", response_model=List[OrderResponse])
def list_orders(
    page: int = 1,
    limit: int = 15,
    duration: int = 180,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    """API to list orders of logged in user."""
    past_date = datetime.today().date() - timedelta(days=duration)
    orders = Order.objects.filter(
        is_active=True,
        order_session__user_id=current_user.user_id,
        created_at__gt=past_date,
    ).order_by("-created_at")
    orders = orders[(page - 1) * limit : (page - 1) * limit + limit]
    orders = parse_obj_as(List[OrderResponse], list(orders))
    return JSONResponse(
        content=[order.simple_dict() for order in orders],
        status_code=status.HTTP_200_OK,
    )


@order_router.post("/", response_model=OrderSessionResponse)
def create_order(
    body: OrderPlaceRequestDto,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    shopping_cart = ShoppingCart.objects.filter(
        id=body.shopping_cart_id,
        is_active=True,
        purchased=False,
    ).first()
    shopping_cart_items = ShoppingCartItem.objects.filter(
        shopping_cart=shopping_cart,
        is_active=True,
    )

    try:
        order_session = OrderSession.objects.get(
            shopping_cart__id=body.shopping_cart_id,
            shopping_cart__is_active=True,
            shopping_cart__purchased=False,
            user_id=current_user.user_id,
            final_total=shopping_cart.total,
        )

    except django.core.exceptions.ObjectDoesNotExist:
        order_session = OrderSession.objects.create(
            shopping_cart__id=body.shopping_cart_id,
            shopping_cart__is_active=True,
            shopping_cart__purchased=False,
            user_id=current_user.user_id,
            final_total=shopping_cart.total,
        )
    orders = []
    final_total = 0
    for shopping_cart_item in shopping_cart_items:
        order, created = Order.objects.get_or_create(
            order_session=order_session,
            billing_address_id=body.billing_address_id,
            shipping_address_id=body.shipping_address_id,
            item_id=shopping_cart_item.item.id,
            final_price=shopping_cart_item.quantity * shopping_cart.unit_price,
            quantity=shopping_cart_item.quantity,
            unit_price=shopping_cart_item.unit_price,
            applied_discount_percentage=(
                shopping_cart_item.item.max_selling_price
                - shopping_cart_item.unit_price
            )
            / shopping_cart_item.item.max_selling_price,
        )
        orders.append(OrderResponse.from_orm(order))
        final_total += order.final_price
    order_session.final_total = final_total
    order_session.save()
    order_session_response = OrderSessionResponse(
        id=order_session.id,
        orders=orders,
    )
    return JSONResponse(
        content=order_session_response.simple_dict(),
        status_code=status.HTTP_201_CREATED,
    )
