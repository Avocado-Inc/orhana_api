from fastapi import HTTPException
from fastapi import status


class BadRequestException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)
