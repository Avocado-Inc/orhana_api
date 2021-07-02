from typing import Dict
from typing import List

from pydantic import parse_obj_as
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from inventory.dto.requests import ProductListQueryDto
from inventory.dto.response import ProductResponse
from inventory.services import ProductService


class ProductView(ViewSet):
    @action(methods=["GET"], detail=False)
    def list_products(self, request: Request, *args, **kwargs):
        query = None
        try:

            query = ProductListQueryDto(**request.query_params)
        except Exception as e:

            return Response(
                data={"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = ProductService.list_products(query)
        if data.__len__():
            data = parse_obj_as(List[Dict], data)
            return Response(
                data=data,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        return Response(
            data=[],
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["GET"], detail=True)
    def get_product(self, request: Request, pk, *args, **kwargs):
        product = ProductService.get_product_by_id(pk)
        if not product:
            return Response(
                data={"message": "No such products"},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json",
            )

        return Response(
            data=ProductResponse.from_orm(product).simple_dict(),
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
