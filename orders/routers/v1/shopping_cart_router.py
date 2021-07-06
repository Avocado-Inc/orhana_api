from typing import List
from uuid import UUID

from django.db.models import F
from django.db.models import Sum
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import parse_obj_as

from globals.dto import CurrentUser
from globals.exceptions import BadRequestException
from globals.exceptions import NotFoundException
from inventory.services import ProductService
from orders.dto.requests import AddCartItemDto
from orders.dto.requests import UpdateCartItem
from orders.dto.response import ShoppingCartItemResponse
from orders.models import ShoppingCart
from orders.models import ShoppingCartItem
from users.services import AuthService

shopping_cart_item_router = APIRouter(tags=["Shopping Cart Item"])


@shopping_cart_item_router.post("/", response_model=ShoppingCartItemResponse)
def add_item_cart(
    body: AddCartItemDto,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    product = ProductService.get_product_by_id(body.item_id)
    if not product:
        raise NotFoundException(detail="No matching product found")
    if product.quantity < 1:
        raise BadRequestException(detail="Out of stock")
    if product.quantity < body.quantity:
        body.quantity = product.quantity
    shopping_cart = ShoppingCart.objects.filter(purchased=False, is_active=True).first()
    if not shopping_cart:
        shopping_cart = ShoppingCart.objects.create(user_id=current_user.user_id)
    cart_item = ShoppingCartItem.objects.filter(
        shopping_cart=shopping_cart,
        shopping_cart__purchased=False,
        shopping_cart__is_active=True,
        user_id=current_user.user_id,
        item_id=body.item_id,
        is_active=True,
    )
    if cart_item:
        cart_item.update(quantity=F("quantity") + body.quantity)
    if not cart_item:
        cart_item = ShoppingCartItem.objects.create(
            item_id=body.item_id,
            quantity=body.quantity,
            unit_price=product.max_selling_price,
            user_id=current_user.user_id,
            shopping_cart=shopping_cart,
        )
    ShoppingCart.objects.filter(id=shopping_cart.id).update(
        number_of_items=F("number_of_items") + body.quantity,
        total=F(
            "total",
        )
        + cart_item.quantity
        + cart_item.unit_price,
    )
    item = ShoppingCartItemResponse.from_orm(cart_item).simple_dict()
    return JSONResponse(
        content=item,
        status_code=status.HTTP_201_CREATED,
    )


@shopping_cart_item_router.patch(
    "/{cart_item_id}",
    response_model=ShoppingCartItemResponse,
)
def update_quantity(
    cart_item_id: UUID,
    body: UpdateCartItem,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    cart_item = ShoppingCartItem.objects.filter(
        id=cart_item_id,
        user_id=current_user.user_id,
        shopping_cart__purchased=False,
        shopping_cart__is_active=True,
    ).first()
    if not cart_item:
        raise NotFoundException()
    ShoppingCartItem.objects.filter(
        id=cart_item_id,
        user_id=current_user.user_id,
    ).update(quantity=body.quantity)
    cart_items = (
        ShoppingCartItem.objects.filter(
            shopping_cart_id=cart_item.shopping_cart.id,
            is_active=True,
        )
        .annotate(
            final_price=F("quantity") + F("unit_price"),
            number_of_items=F("number_of_items"),
        )
        .aggregate(
            final_price=Sum("final_price", number_of_items=Sum("number_of_items")),
        )
    )
    ShoppingCart.objects.filter(
        id=cart_item.shopping_cart,
        shopping_cart__purchased=False,
        shopping_cart__is_active=True,
    ).update(
        total=cart_items.get("final_price"),
        number_of_items=cart_items.get("number_of_items"),
    )
    item = ShoppingCartItemResponse.from_orm(cart_item)
    return JSONResponse(
        content=item.simple_dict(),
        status_code=status.HTTP_200_OK,
    )


@shopping_cart_item_router.get(
    "/{cart_item_id}",
    response_model=ShoppingCartItemResponse,
)
def get_cart_item_by_id(
    cart_item_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    cart_item = ShoppingCartItem.objects.filter(
        id=cart_item_id,
        user_id=current_user.user_id,
        shopping_cart__purchased=False,
        shopping_cart__is_active=True,
    ).first()
    if not cart_item:
        raise NotFoundException()
    item = ShoppingCartItemResponse.from_orm(cart_item)
    return JSONResponse(
        content=item.simple_dict(),
        status_code=status.HTTP_200_OK,
    )


@shopping_cart_item_router.get(
    "/shopping-cart/{shopping_cart_id}",
    response_model=List[ShoppingCartItemResponse],
)
def list_cart_items(
    shopping_cart_id: UUID,
    current_user: CurrentUser = Depends(AuthService.verify_auth_access_token),
):
    cart_items = ShoppingCartItem.objects.filter(
        shopping_cart_id=shopping_cart_id,
        user_id=current_user.user_id,
        is_active=True,
    )
    cart_items = parse_obj_as(List[ShoppingCartItemResponse], list(cart_items))
    if cart_items.__len__():
        return JSONResponse(
            content=[item.simple_dict() for item in cart_items],
            status_code=status.HTTP_200_OK,
        )
    raise NotFoundException(detail="Cart is empty")
