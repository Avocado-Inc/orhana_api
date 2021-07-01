from rest_framework.routers import DefaultRouter

from users.views.v1 import AuthViewSet
from users.views.v1 import UserViewSet

prefix_auth = "v1/auth"
prefix_user = "v1/user"
v1_auth_router = DefaultRouter()
v1_auth_router.register(f"{prefix_auth}", AuthViewSet, basename="auth_view")

v1_user_router = DefaultRouter()
v1_user_router.register(f"{prefix_user}", UserViewSet, basename="user_view")
