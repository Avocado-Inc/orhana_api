from typing import Any

from rest_framework.response import Response

from .base_response_model import BaseResponse


class JsonResponse(Response):
    def __init__(self, data: Any, status: int, message: str, meta: dict = None):
        if meta is None:
            meta = dict()
        super().__init__(
            data=BaseResponse(
                code=status,
                data=data,
                message=message,
                meta=meta or dict(),
            ).simple_dict(),
            status=status,
            content_type="application/json",
        )
