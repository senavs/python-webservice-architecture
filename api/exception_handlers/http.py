from starlette.requests import Request
from starlette.responses import JSONResponse

from api.exception import APIException


def http_exception(_: Request, exception: APIException) -> JSONResponse:
    return JSONResponse(status_code=exception.status_code, content={"message": exception.message})
