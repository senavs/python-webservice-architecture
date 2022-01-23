from fastapi import FastAPI

from . import __version__
from .exception_handlers import exception_handlers
from .middlewares import RequestTimeMiddleware
from .routes import health, v1


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Architecture",
        description="Base FastAPI architecture for future projects",
        version=__version__,
    )

    register_errors_handler(app)
    register_middlewares(app)
    register_routes(app)

    return app


def register_errors_handler(app: FastAPI):
    for exception, handler in exception_handlers.items():
        app.add_exception_handler(exception, handler)


def register_middlewares(app: FastAPI):
    app.add_middleware(RequestTimeMiddleware)


def register_routes(app: FastAPI):
    app.include_router(health.router)
    app.include_router(v1.router)
