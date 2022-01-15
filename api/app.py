from fastapi import FastAPI, __version__


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Architecture",
        description="Base FastAPI architecture for future projects",
        version=__version__,
        routes=[],
        middleware=[],
        exception_handlers={},
    )
    return app
