from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from users.services import AuthService


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        if request.path.__contains__("public"):
            return self.get_response(request)
        elif request.path.__contains__("auth"):
            return self.get_response(request)
        else:
            try:
                current_user = AuthService.verify_auth_access_token_middleware(request)
                request.current_user = current_user
                return self.get_response(request)
            except Exception:
                return JsonResponse(
                    data={
                        "message": "unauthorized request",
                    },
                    status=401,
                )
