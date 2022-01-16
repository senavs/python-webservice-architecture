from fastapi import FastAPI

from . import __version__
from .exceptions import handlers
from .middlewares import RequestTimeMiddleware
from .routes import health


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Architecture",
        description="Base FastAPI architecture for future projects",
        version=__version__,
    )

    register_exception_handlers(app)
    register_middlewares(app)
    register_routes(app)

    return app


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(handlers.RequestValidationError, handlers.validation_error)


def register_middlewares(app: FastAPI):
    app.add_middleware(RequestTimeMiddleware)


def register_routes(app: FastAPI):
    app.include_router(health.router)
