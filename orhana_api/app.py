import os
from importlib.util import find_spec

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

from orhana_api.settings import METHODS
from orhana_api.settings import ORIGINS
from orhana_api.settings import VERSION
from orhana_api.wsgi import application


def create_app() -> FastAPI:

    app = FastAPI(
        title="APIs for Orhana Website",
        version=VERSION,
    )

    # @app.route("/ping")
    # async def ping_api():
    #     return {"message": "ok"}

    app.mount("/django", WSGIMiddleware(application))
    app.mount(
        "/static",
        StaticFiles(
            directory=os.path.normpath(
                os.path.join(find_spec("django.contrib.admin").origin, "..", "static"),
            ),
        ),
        name="static",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_methods=METHODS,
        allow_headers=["*"],
    )

    from inventory.routers.v1 import inventory_app_router
    from users.routers.v1 import user_app_router
    from orders.routers.v1 import orders_app_router

    app.include_router(user_app_router, prefix="/api")
    app.include_router(inventory_app_router, prefix="/api")
    app.include_router(orders_app_router, prefix="/api")
    return app
