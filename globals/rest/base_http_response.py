from typing import Any

from fastapi.responses import JSONResponse

from .base_response_model import BaseResponse


class JsonResponse(JSONResponse):
    def __init__(self, data: Any, status: int, message: str, meta: dict = None):
        if meta is None:
            meta = dict()
        super().__init__(
            content=BaseResponse(
                code=status,
                data=data,
                message=message,
                meta=meta or dict(),
            ).simple_dict(),
            status_code=status,
        )
