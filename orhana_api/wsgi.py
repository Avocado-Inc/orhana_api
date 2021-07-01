"""WSGI config for orhana_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

default_settings = "orhana_api.settings"

# environment = os.environ.get("ENV", "development")
# if environment == "production":
#     default_settings = 'orhana_api.settings_prod'


os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_settings)


application = get_wsgi_application()
