from fastapi.exceptions import RequestValidationError

from app.src.exception import BadRequestException, NotFoundException

from .assertion import assertion_error
from .http import http_exception_factory
from .validation import validation_error

exception_handlers = {
    AssertionError: assertion_error,
    RequestValidationError: validation_error,
    BadRequestException: http_exception_factory(400),
    NotFoundException: http_exception_factory(404),
}
