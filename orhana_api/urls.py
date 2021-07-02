"""orhana_api URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from inventory.routers.v1 import V1ProductsRouter
from users.routers.v1 import V1AuthRouter
from users.routers.v1 import V1UserRouter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(V1AuthRouter.urls)),
    path("api/", include(V1UserRouter.urls)),
    path("api/", include(V1ProductsRouter.urls)),
]
