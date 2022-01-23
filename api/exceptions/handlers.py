from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from starlette.responses import JSONResponse

from . import APIException, NotFoundException, BadRequestException


def assertion_error(_: Request, exception: AssertionError) -> JSONResponse:
    return JSONResponse(status_code=400, content={"message": str(exception)})


def http_exception(_: Request, exception: APIException) -> JSONResponse:
    return JSONResponse(status_code=exception.status_code, content={"message": exception.message})


def validation_error(_: Request, exception: RequestValidationError) -> JSONResponse:
    errors = [
        {"location": validation._loc[0], "name": validation._loc[1], "message": str(validation.exc)}
        for validation in exception.args[0]
    ]
    return JSONResponse(status_code=422, content=errors)


exception_handlers = {
    AssertionError: assertion_error,
    BadRequestException: http_exception,
    NotFoundException: http_exception,
    RequestValidationError: validation_error,
}
