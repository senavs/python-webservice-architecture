from typing import Callable

from starlette.requests import Request
from starlette.responses import JSONResponse

from app.src.exception import APIException


def http_exception_factory(status_code: int) -> Callable:
    def http_exception(_: Request, exception: APIException) -> JSONResponse:
        return JSONResponse(status_code=status_code, content={"message": exception.message})

    return http_exception
