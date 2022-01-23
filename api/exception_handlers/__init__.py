from fastapi.exceptions import RequestValidationError

from .assertion import assertion_error
from .http import http_exception
from .validation import validation_error
from ..exception import BadRequestException, NotFoundException

exception_handlers = {
    AssertionError: assertion_error,
    BadRequestException: http_exception,
    NotFoundException: http_exception,
    RequestValidationError: validation_error,
}
