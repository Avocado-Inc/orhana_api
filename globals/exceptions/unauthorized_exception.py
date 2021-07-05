from fastapi import HTTPException
from fastapi import status


class UnauthorizedException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail=None,
        headers=None,
    ):
        super().__init__(status_code, detail=detail, headers=headers)
